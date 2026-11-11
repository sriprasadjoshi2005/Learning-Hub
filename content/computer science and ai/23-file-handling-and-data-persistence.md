---
title: File Handling and Data Persistence
level: intermediate
---

File handling allows programs to store, retrieve, modify, and organize information using files. Data persistence ensures that information remains available even after a program terminates.

## 1. Understanding Files

A file is a named collection of information stored on a storage device.

Files allow programs to preserve information beyond their execution period.

Common examples include:
- Text documents.
- Images.
- Audio files.
- Videos.
- Configuration files.
- Database backups.
- Application logs.

## 2. File Types

Files can be broadly classified into two categories.

### Text Files

Text files store information as readable characters.

Examples include:
- TXT
- CSV
- JSON
- XML
- HTML

### Binary Files

Binary files store information as bytes and may represent data that is not directly readable as ordinary text.

Examples include:
- Images.
- Audio files.
- Executable programs.
- Compressed archives.
- Certain document formats.

## 3. File Operations

Common file operations include:

| Operation | Description |
| --- | --- |
| Create | Creates a new file |
| Open | Makes a file available for processing |
| Read | Retrieves stored information |
| Write | Stores information in a file |
| Append | Adds information to existing content |
| Close | Releases the opened file resource |
| Delete | Removes a file |

## 4. File Opening Modes

Python provides different file-opening modes.

| Mode | Meaning |
| --- | --- |
| `r` | Opens a file for reading |
| `w` | Opens a file for writing and replaces existing content |
| `a` | Opens a file for appending |
| `x` | Creates a new file and fails if it already exists |
| `rb` | Opens a binary file for reading |
| `wb` | Opens a binary file for writing |

The choice of mode determines how a program interacts with a file.

## 5. Reading Files

Reading retrieves information stored in a file.

Example:

```python
file = open("notes.txt", "r")
content = file.read()
print(content)
file.close()
```

Common reading methods include:

- `read()`: Reads file content.
- `readline()`: Reads one line.
- `readlines()`: Returns lines as a list.

## 6. Writing Files

Writing stores information in a file.

Example:

```python
file = open("notes.txt", "w")
file.write("Computer Science is fascinating.")
file.close()
```

Opening an existing file in write mode replaces its previous content.

This behaviour makes it important to select the correct mode.

## 7. Appending Data

Appending adds new information without removing existing content.

Example:

```python
file = open("notes.txt", "a")
file.write("\nArtificial Intelligence is an important field.")
file.close()
```

Appending is useful for:
- Application logs.
- Activity records.
- Historical data.
- Repeated data collection.

## 8. Using the With Statement

Python provides the `with` statement for safer resource management.

Example:

```python
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
```

The file is automatically closed when the block finishes, even if an exception occurs.

This approach is generally preferred over manually closing files.

## 9. File Handling and Exceptions

Files may be unavailable because they do not exist, permissions are insufficient, or storage operations fail.

Example:

```python
try:
    with open("records.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("The requested file does not exist.")
except PermissionError:
    print("Permission denied.")
```

Exception handling helps applications respond to file-related problems safely.

## 10. Structured Data Storage

Programs frequently store structured information rather than plain paragraphs.

### CSV

CSV stands for Comma-Separated Values.

It stores tabular information using rows and fields.

Example:

```text
Name,Age,Score
Asha,20,85
Ravi,21,92
Meera,19,88
```

CSV is commonly used for spreadsheets and data exchange.

### JSON

JSON stands for JavaScript Object Notation.

It stores structured information using objects and arrays.

Example:

```json
{
    "name": "Asha",
    "age": 20,
    "subjects": ["Mathematics", "Computer Science"]
}
```

JSON is widely used in web applications, APIs, and configuration files.

Python can process JSON using its built-in `json` module.

```python
import json

student = {
    "name": "Asha",
    "age": 20
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)
```

## 11. Data Persistence

Data persistence refers to retaining information beyond the lifetime of a program.

Without persistence, information stored only in temporary memory may disappear when the program terminates.

Common persistence methods include:

- Text files.
- CSV files.
- JSON files.
- Relational databases.
- NoSQL databases.
- Cloud storage systems.

## 12. File Handling Best Practices

- Select the correct file mode.
- Close files after use or use context managers.
- Handle missing files and permission errors.
- Validate data before storing it.
- Avoid overwriting important information accidentally.
- Use suitable formats for structured data.
- Protect sensitive information.

## Common Exam Traps

- Write mode can replace existing file content.
- Append mode preserves existing content and adds new data.
- Binary files are not necessarily readable as ordinary text.
- The with statement manages file closure automatically.
- CSV represents tabular data, while JSON supports structured objects and arrays.
- Data persistence allows information to survive program termination.

## Quiz

1. Which file mode is used to add information without replacing existing content?
   - [ ] r
   - [ ] w
   - [x] a
   - [ ] x

   > Append mode adds new information to the end of an existing file.

2. Which Python statement automatically manages file closure?
   - [ ] import
   - [ ] return
   - [ ] raise
   - [x] with

   > The with statement uses a context manager to release the file resource automatically.

3. Which format is commonly used to represent structured data using objects and arrays?
   - [ ] TXT
   - [ ] BMP
   - [x] JSON
   - [ ] MP3

   > JSON represents structured information using objects, arrays, strings, numbers, and other supported values.