#!/usr/bin/python3
""" Module that executes a function that appends a line """


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing a specific string.

    Arguments:
    filename -- the name of the file (default: "")
    search_string -- the string to search for in each line of the file (default: "")
    new_string -- the string to insert after each line containing the search string (default: "")

    Returns:
    None
    """
    lines = []
    with open(filename, "r") as file:
        for line in file:
            lines.append(line)
            if search_string in line:
                lines.append(new_string + "\n")

    with open(filename, "w") as file:
        file.writelines(lines)
