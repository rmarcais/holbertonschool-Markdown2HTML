#!/usr/bin/python3
"""
0.Start a script

Script that takes an argument 2 strings.
"""

import os
import re
import sys

def parse(line, type, isPreviousP):
    """Function that parses a piece of string and returns the generated HTML"""
    line = " ".join(line)
    if re.match(".*\*\*.+\*\*.*", line):
        line = line.replace("**", "<b>", 1)
        line = line.replace("**", "</b>", 2)
    elif re.match(".*__.+__.*", line):
        print("hello")
        line = line.replace("__", "<em>", 1)
        line = line.replace("__", "</em>", 2)
    if type == "li":
        return "<li>" + line + "</li>"
    elif not isPreviousP and type == '':
        return "<p>\n" + line
    elif isPreviousP:
        return "<br/>\n" + line
    elif type == "h":
        return line

def parseline(lines):
    """Function that parses the line and returns the generated HTML"""
    generated_html = ""
    closed_ul = True
    closed_ol = True
    is_previous_p = False
    close_p = False
    for line in lines:
        if line == "\n":
            if is_previous_p:
                generated_html += "</p>\n"
            is_previous_p = False
            close_p = False
            continue
        new_line = line.split()
        if re.match("#+", new_line[0]):
            if len(line) > 1:
                size_h = len(new_line[0])
            generated_html += "<h{}>".format(size_h) + parse(new_line[1:], 'h', False) + "</h{}>".format(size_h)
            close_p = True
        elif "-" == new_line[0]:
            if closed_ul:
                generated_html += "<ul>\n" + parse(new_line[1:], 'li', False)
                closed_ul = False
            else:
                generated_html += parse(new_line[1:], 'li', False)
            close_p = True
        elif "*" == new_line[0]:
            if closed_ol:
                generated_html += "<ol>\n" + parse(new_line[1:], 'li', False)
                closed_ol = False
            else:
                generated_html += parse(new_line[1:], 'li', False)
            close_p = True
        else:
            if not closed_ul:
                generated_html += "</ul>\n"
                closed_ul = True
            elif not closed_ol:
                generated_html += "</ol>\n"
                closed_ol = True
            generated_html += parse(new_line, '', is_previous_p)
            is_previous_p = True
            close_p = True
        generated_html += "\n"
    if not closed_ul:
        generated_html += "</ul>\n"
        closed_ul = True
    elif not closed_ol:
        generated_html += "</ol>\n"
        closed_ol = True
    if close_p and is_previous_p:
        generated_html += "</p>\n"
        close_p = True
    return generated_html
            



if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)
    elif not os.path.exists(sys.argv[1]):
        print("Missing {}".format(sys.argv[1]), file=sys.stderr)
        sys.exit(1)

    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    with open(sys.argv[2], 'w') as f:
        generated_html = parseline(lines)
        f.write(generated_html)

    sys.exit(0)
