import sys
import os
import datetime
import time

verzeichnis = sys.argv[1]
intervalInput = sys.argv[2]

print("Wurzel des Verzeichnis:", verzeichnis)
print("Zeitintervall:", intervalInput, "Stunden")
print("Datei und Zeitpunkt der letzten Änderung:")
print(" ")

intervalInSeconds = int(intervalInput) * 3600
t = time.time()
# print("Zeit nicht konvertiert:", t)
currentTime = datetime.datetime.fromtimestamp(t)
# print("Konvertierte Zeit", currentTime)

for root, dirs, files in os.walk(verzeichnis):

    for filename in files:
        m_time = os.path.getmtime(os.path.join(root, filename))
        dt_m = datetime.datetime.fromtimestamp(m_time)
        if (m_time <= t - intervalInSeconds):
            beep = 0
        else:
            print(os.path.join(root, filename))
            # print("Modified on", m_time)
            print("Modified on", dt_m)
            print(" ")


# Used Resources
# https://www.google.com/search?q=python+check+modified+files+in+timespan&rlz=1C1ONGR_deDE974DE999&sxsrf=ALiCzsawsxkTGQyOj8RS3kvfdfqCYqeXxA%3A1666693254243&ei=hrhXY-6nDo_Axc8P4-6fqAw&ved=0ahUKEwjugvmalPv6AhUPYPEDHWP3B8UQ4dUDCA8&uact=5&oq=python+check+modified+files+in+timespan&gs_lcp=Cgdnd3Mtd2l6EAMyBQghEKABMgUIIRCgAToKCAAQRxDWBBCwAzoNCAAQ5AIQ1gQQsAMYAToGCAAQFhAeOggIABAWEB4QCjoICCEQFhAeEB06BwghEKABEApKBAhNGAFKBAhBGABKBAhGGAFQ8G5YgIMBYPOHAWgBcAF4AIABjwGIAcYPkgEEMC4xN5gBAKABAcgBDcABAdoBBggBEAEYCQ&sclient=gws-wiz
# https://pynative.com/python-file-creation-modification-datetime/
# https://pynative.com/python/datetime/
# https://stackoverflow.com/questions/237079/how-do-i-get-file-creation-and-modification-date-times
# https://www.tutorialspoint.com/python/os_stat.htm
# https://docs.python.org/3/library/stat.html
# https://stackoverflow.com/questions/65769364/program-to-check-all-last-modified-files-in-a-folder-using-python
# https://www.google.com/search?q=python+walk+through+directory+and+subdirectories&rlz=1C1ONGR_deDE974DE999&oq=python+walk+through+&aqs=chrome.2.69i57j0i512j0i20i263i512j0i512l2j0i22i30l5.3768j0j7&sourceid=chrome&ie=UTF-8
# https://www.geeksforgeeks.org/how-to-iterate-over-files-in-directory-using-python/?id=discuss
# https://www.w3resource.com/python-exercises/python-basic-exercise-64.php
# https://www.google.com/search?q=python+print+modified+date+and+time+of+file&oq=python+print+modified+date+and+time+of+file&aqs=chrome..69i57.13320j0j4&sourceid=chrome&ie=UTF-8
# https://docs.python.org/3/library/os.path.html
# https://docs.python.org/3/library/time.html
# https://pynative.com/python-current-date-time/#:~:text=Get%20Current%20Time%20in%20Python,-There%20are%20many&text=time()-,Use%20the%20time.,the%20current%20time%20in%20seconds.
