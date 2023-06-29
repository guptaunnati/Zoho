# Implement a program that expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of lines of code in that file, excluding comments and blank lines. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py, or if the specified file does not exist, the program should instead exit via sys.exit. 

import sys

def main():
    if len(sys.argv) != 2:
        print("Error: Incorrect number of arguments")
        sys.exit(1)

    file_name = sys.argv[1]
    
    if not file_name.endswith(".py"):
        print("Error: Incorrect file type")
        sys.exit(1)

    try:
        line_count = count_lines(file_name)
        print("Line count:", line_count)
    except FileNotFoundError:
        print("Error: File not found")
        sys.exit(1)

def count_lines(file_name):
    with open(file_name, "r") as f:
        code = f.readlines()
        count = 0
        multi_line_comment=False
        for line in code:
            line = line.strip()
            
            if line.startswith('"""'):
                multi_line_comment=True

            if line.endswith('"""'):
                multi_line_comment=False
                continue

            if line and not line.startswith("#") and not multi_line_comment:
                count += 1
        return count

if __name__ == "__main__":
    main()