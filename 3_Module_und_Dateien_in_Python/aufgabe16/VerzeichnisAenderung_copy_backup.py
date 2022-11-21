import string
import sys
import os
import datetime
import time

print("Geben sie ein Verzeichnis und ein Zeitintervall in Stunden an:\n")

verzeichnis = sys.argv[1]
intervalInput = sys.argv[2]

print("Wurzel des Verzeichnis", verzeichnis)
print("Zeitintervall", intervalInput)
print("Datei und Zeitpunkt der letzten Änderung:")
print(" ")
intervalInSeconds = intervalInput * 3600

t = time.time()
print("Zeit nicht konvertiert:", t)
currentTime = datetime.datetime.fromtimestamp(t)
print("Konvertierte Zeit", currentTime)

# statinfo = []

for root, dirs, files in os.walk(verzeichnis):

    for filename in files:

        print(os.path.join(root, filename))
        m_time = os.path.getmtime(os.path.join(root, filename))
        dt_m = datetime.datetime.fromtimestamp(m_time)

        # print("Modified on", m_time)
        print("Modified on", dt_m)
        print(" ")

        # m_time = os.path.getmtime(filename)
        # dt_m = datetime.datetime.fromtimestamp(m_time)
        # print("Modified on", dt_m)
#     # Get Filepath vllt und verbinden mit Zeit?
#     # evtl Funktion dafür erstellen?
#     # Zeitintervall in Abhängigkeit von Systemzeit machen


# for filenames in os.walk(verzeichnis):
#     m_time = os.path.getmtime(verzeichnis)
#     dt_m = datetime.datetime.fromtimestamp(m_time)
#     print("Modified on", dt_m)


def creation_date(verzeichnis):
    # https://stackoverflow.com/questions/237079/how-do-i-get-file-creation-and-modification-date-times
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    return os.path.getctime(verzeichnis)
