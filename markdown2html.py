#!/usr/bin/python3
"""
0.Start a script

Script that takes an argument 2 strings.
"""

import os
import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)
    elif not os.path.exists(sys.argv[1]):
        print("Missing {}".format(sys.argv[1]), file=sys.stderr)
        sys.exit(1)
    else:
        sys.exit(0)
