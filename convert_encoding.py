"""Convert encoding of the config file.

Usage: python convert_encoding.py <utf-8 | utf-16>
"""

import sys
from pathlib import Path


def get_contents(path):
    """Read file contents, and display encoding that was used."""
    try:
        contents = path.read_text()
        print("File currently uses utf-8 encoding.")
    except UnicodeDecodeError:
        print("File currently uses utf-16 encoding.")
        contents = path.read_text(encoding='utf-16')

    return contents


# Read current file and encoding.
path = Path(".platform.app.yaml")
contents = get_contents(path)

# Rewrite file with specified encoding.
new_encoding = sys.argv[1]
path.write_text(contents, encoding=new_encoding)

# Verify new encoding.
contents = get_contents(path)