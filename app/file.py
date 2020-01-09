"""
Helpers for files.
"""

def read_file_upper(filename):
    """Read a file as an uppercase string."""
    with open(filename) as file:
        contents = file.read().strip().upper()
    return contents
