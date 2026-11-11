"""Loads lessons from content/<subject>/NN-title.md (and, if present, the old content.py).

Every lesson ends up as:
  {"id", "title", "level", "content" (HTML), "quiz": [{"question", "options", "answer", "explanation"}]}
All text fields are ready-to-display HTML.
"""
import html
import os
import re

import markdown as md

CONTENT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content")
LEVELS = ("foundation", "intermediate", "advanced", "exam")
LEVEL_LABELS = {
    "foundation": "Foundation",
    "intermediate": "Intermediate",
    "advanced": "Advanced",
    "exam": "Entrance exam",
    "": "",
}


class ContentError(Exception):
    pass


# ---------- Markdown + math ----------

_BLOCK = re.compile(r"\$\$(.+?)\$\$", re.S)
_INLINE = re.compile(r"(?<![\\$])\$(?=\S)([^$\n]+?)(?<=\S)\$")


def render_md(text, inline=False):
    """Markdown -> HTML. $...$ and $$...$$ become KaTeX delimiters; write \\$ for a literal dollar."""
    stash = []

    def keep(s):
        stash.append(s)
        return "zzmath%dzz" % (len(stash) - 1)

    text = text.replace("\\$", "zzdollarzz")
    text = _BLOCK.sub(lambda m: keep("\\[" + html.escape(m.group(1).strip(), quote=False) + "\\]"), text)
    text = _INLINE.sub(lambda m: keep("\\(" + html.escape(m.group(1), quote=False) + "\\)"), text)
    out = md.markdown(text, extensions=["tables", "fenced_code", "sane_lists"])
    if inline:
        out = re.sub(r"^<p>(.*)</p>$", r"\1", out.strip(), flags=re.S)
    out = re.sub(r"zzmath(\d+)zz", lambda m: stash[int(m.group(1))], out)
    return out.replace("zzdollarzz", "$")


# ---------- parsing ----------

def _front_matter(text, path):
    text = text.replace("\r\n", "\n").lstrip("\ufeff")
    if not text.startswith("---"):
        raise ContentError("%s: file must start with a --- front-matter block" % path)
    end = text.find("\n---", 3)
    if end == -1:
        raise ContentError("%s: front-matter block is not closed with ---" % path)
    meta = {}
    for line in text[3:end].strip().splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip().lower()] = v.strip()
    return meta, text[end + 4:].strip("\n")


_Q = re.compile(r"^\d+\.\s+(.*)$")
_OPT = re.compile(r"^\s*[-*]\s+\[([ xX])\]\s+(.*)$")
_EXP = re.compile(r"^\s*>\s?(.*)$")


def _parse_quiz(block, path):
    questions, cur, mode = [], None, None
    for raw in block.splitlines():
        line = raw.rstrip()
        if not line.strip():
            mode = None
            continue
        o, e, q = _OPT.match(line), _EXP.match(line), _Q.match(line)
        if o and cur is not None:
            cur["options"].append(o.group(2).strip())
            if o.group(1) in "xX":
                cur["correct"].append(len(cur["options"]) - 1)
            mode = None
        elif e and cur is not None:
            cur["exp"] = (cur["exp"] + " " + e.group(1)).strip()
            mode = "e"
        elif q and not line.startswith(" "):
            cur = {"q": q.group(1).strip(), "options": [], "correct": [], "exp": ""}
            questions.append(cur)
            mode = "q"
        elif cur is not None and mode == "q":
            cur["q"] += " " + line.strip()
        elif cur is not None and mode == "e":
            cur["exp"] += " " + line.strip()
        else:
            raise ContentError("%s: cannot understand quiz line: %r" % (path, line))
    out = []
    for i, c in enumerate(questions, 1):
        if len(c["options"]) != 4:
            raise ContentError("%s: question %d needs exactly 4 options (has %d)" % (path, i, len(c["options"])))
        if len(c["correct"]) != 1:
            raise ContentError("%s: question %d needs exactly one [x] option (has %d)" % (path, i, len(c["correct"])))
        if not c["exp"]:
            raise ContentError("%s: question %d has no explanation (add a > line)" % (path, i))
        if len(set(c["options"])) != 4:
            raise ContentError("%s: question %d has duplicate options" % (path, i))
        out.append({
            "question": render_md(c["q"], inline=True),
            "options": [render_md(x, inline=True) for x in c["options"]],
            "answer": c["correct"][0],
            "explanation": render_md(c["exp"], inline=True),
        })
    return out


def parse_lesson(path):
    fname = os.path.basename(path)
    m = re.match(r"^(\d+)-.+\.md$", fname)
    if not m:
        raise ContentError("%s: file name must look like 01-topic-name.md" % path)
    with open(path, encoding="utf-8") as f:
        meta, body = _front_matter(f.read(), path)
    if not meta.get("title"):
        raise ContentError("%s: missing title" % path)
    level = meta.get("level", "").lower()
    if level not in LEVELS:
        raise ContentError("%s: level must be one of %s" % (path, ", ".join(LEVELS)))
    parts = re.split(r"^##\s+Quiz\s*$", body, maxsplit=1, flags=re.M)
    if len(parts) != 2:
        raise ContentError("%s: missing a '## Quiz' section" % path)
    return {
        "id": int(m.group(1)),
        "title": meta["title"],
        "level": level,
        "content": render_md(parts[0].strip()),
        "words": len(parts[0].split()),
        "quiz": _parse_quiz(parts[1], path),
    }


def _load_folder(folder, errors):
    key = os.path.basename(folder)
    meta = {}
    meta_path = os.path.join(folder, "_subject.md")
    if os.path.exists(meta_path):
        with open(meta_path, encoding="utf-8") as f:
            meta, _ = _front_matter(f.read(), meta_path)
    lessons = []
    for fname in sorted(os.listdir(folder)):
        if fname.startswith("_") or not fname.endswith(".md"):
            continue
        try:
            lessons.append(parse_lesson(os.path.join(folder, fname)))
        except ContentError as exc:
            errors.append(str(exc))
    lessons.sort(key=lambda l: l["id"])
    return key, {
        "name": meta.get("name", key.replace("_", " ").title()),
        "description": meta.get("description", ""),
        "order": int(meta.get("order", 100)),
        "lessons": lessons,
    }


def _load_legacy():
    """Old content.py, if it is still in the project. Its text is already HTML."""
    try:
        from content import SUBJECTS as old
    except Exception:
        return {}
    subjects = {}
    for i, (key, s) in enumerate(old.items(), 1):
        subjects[key] = {
            "name": s["name"],
            "description": "",
            "order": i,
            "lessons": [
                {"id": l["id"], "title": l["title"], "level": "", "content": l["content"], "words": 0,
                 "quiz": [{"question": q["question"], "options": q["options"], "answer": q["answer"],
                           "explanation": ""} for q in l["quiz"]]}
                for l in s["lessons"]
            ],
        }
    return subjects


def load_all():
    """Returns (subjects ordered dict, list of error strings). Folders in content/ override content.py."""
    errors = []
    subjects = {}
    if os.path.isdir(CONTENT_DIR):
        for name in sorted(os.listdir(CONTENT_DIR)):
            folder = os.path.join(CONTENT_DIR, name)
            if os.path.isdir(folder) and not name.startswith((".", "_")):
                key, subj = _load_folder(folder, errors)
                subjects[key] = subj
    ordered = dict(sorted(subjects.items(), key=lambda kv: (kv[1]["order"], kv[1]["name"])))
    for s in ordered.values():
        s["by_id"] = {l["id"]: l for l in s["lessons"]}
    return ordered, errors
