# Day 05: Python File Handling

## 1. Core Syntax & Modes
We use the Context Manager (`with open`) because it automatically handles closing the file stream, preventing memory leaks.

| Mode | Operation | Behavior |
| :--- | :--- | :--- |
| `'r'` | Read | Default mode. Opens file for reading. Errors out if file doesn't exist. |
| `'w'` | Write | Creates a new file or Overwrites/Wipes an existing file completely. |
| `'a'` | Append | Creates a new file or Adds text to the absolute end of an existing file. |

## 2. Reading Mechanics
*   `f.read(size)`: Reads the entire file, or up to the specified `size` in bytes.
*   `f.readline()`: Reads a single line from the file moving the cursor to the next line.
*   `f.readlines()`: Reads the entire file and stores every line as a string inside a Python **List**.
*   **Best Practice (Looping):** Iterating directly over the file object (`for line in f:`) reads line-by-line without overloading memory.

## 3. Cursor Manipulation (Crucial Interview Topic)
*   `f.tell()`: Returns an integer representing the **current position** of the file pointer (in bytes) from the start of the file.
*   `f.seek(offset)`: Moves the file pointer cursor to a specific byte location. `f.seek(0)` resets the cursor to the absolute beginning of the file.

## 4. Code Recipe: Copying a File
```python
with open("source.md", "r") as reader:
    with open("destination.txt", "w") as writer:
        for line in reader:
            writer.write(line)