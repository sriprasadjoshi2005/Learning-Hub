"""Run before every push:  python check_content.py
Checks every lesson in content/ and prints a summary. Exits with code 1 if anything is wrong."""
import os
import sys

import content_loader as cl


def main():
    errors, warnings = [], []
    if not os.path.isdir(cl.CONTENT_DIR):
        print("No content/ folder found.")
        return 1

    for name in sorted(os.listdir(cl.CONTENT_DIR)):
        folder = os.path.join(cl.CONTENT_DIR, name)
        if not os.path.isdir(folder) or name.startswith((".", "_")):
            continue
        folder_errors = []
        _, subj = cl._load_folder(folder, folder_errors)
        errors += folder_errors
        lessons = subj["lessons"]
        ids = [l["id"] for l in lessons]

        if ids != list(range(1, len(ids) + 1)):
            errors.append("%s: lesson numbers must run 1,2,3... with no gaps or repeats (found %s)" % (name, ids))
        titles = [l["title"] for l in lessons]
        for t in set(titles):
            if titles.count(t) > 1:
                errors.append("%s: duplicate lesson title %r" % (name, t))

        positions = [0, 0, 0, 0]
        for l in lessons:
            tag = "%s lesson %d (%s)" % (name, l["id"], l["title"])
            if not 2 <= len(l["quiz"]) <= 3:
                errors.append("%s: quiz must have 2 or 3 questions (has %d)" % (tag, len(l["quiz"])))
            if l["words"] < 150:
                warnings.append("%s: only %d words, looks thin" % (tag, l["words"]))
            for q in l["quiz"]:
                positions[q["answer"]] += 1

        total_q = sum(positions)
        if total_q >= 12 and max(positions) / total_q > 0.45:
            warnings.append("%s: correct answers cluster in one position %s (the app shuffles options, but vary them anyway)"
                            % (name, positions))

        by_level = {}
        for l in lessons:
            by_level[l["level"]] = by_level.get(l["level"], 0) + 1
        print("%-20s %3d lessons, %3d questions  %s" % (name, len(lessons), total_q, by_level))

    for w in warnings:
        print("WARNING:", w)
    for e in errors:
        print("ERROR:  ", e)
    print("\n%d error(s), %d warning(s)" % (len(errors), len(warnings)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
