# https://www.youtube.com/watch?v=DzzXB9XhBg4
# https://stackoverflow.com/questions/55660330/how-to-get-date-created-and-date-modified-while-using-os-walk4
# https://www.tutorialspoint.com/python/os_stat.htm
# https://www.tutorialspoint.com/python/os_walk.htm
# https://stackoverflow.com/questions/10989005/do-i-understand-os-walk-right
# https://www.geeksforgeeks.org/os-walk-python/


import string
import sys
import os

print("Geben sie ein Verzeichnis und ein Zeitintervall in Stunden an:\n")

verzeichnis = sys.argv[1]
intervall = sys.argv[2]

print(verzeichnis)
print(intervall)

statinfo = []

# for dirpath, dirnames, filenames in os.walk(verzeichnis):
#     print(
#         f"Root: {dirpath}\n"
#         f"Sub-directories: {dirnames}\n"
#         f"Files: {filenames}\n\n"
#     )
#     # Get Filepath vllt und verbinden mit Zeit?
#     # evtl Funktion dafür erstellen?


def creation_date(verzeichnis):
    # https://stackoverflow.com/questions/237079/how-do-i-get-file-creation-and-modification-date-times
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    return os.path.getctime(verzeichnis)


# for dirpath in os.walk(verzeichnis):
#     print(f"Root: {dirpath}\n)
