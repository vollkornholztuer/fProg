from html.parser import HTMLParser
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]


def filterHTML(input_file, output_file):
    datei = open(input_file)
    content = datei.read()
    datei.close()

    writemode = True
    output = ""
    for char in content:
        if char == "<":
            output += char
            writemode = True
        elif char == ">":
            output += char
            writemode = False
        elif writemode:
            output += char

    n = open(output_file, "w")
    n.write(output)
    n.close()


filterHTML(input_file, output_file)
