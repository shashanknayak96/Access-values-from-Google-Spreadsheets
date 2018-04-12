import requests
import csv 
import os

mydir = (os.path.dirname(os.path.realpath(__file__)))
os.chdir(mydir)
url = "<LINK TO THE PUBLISHED CSV FILE>"

r = requests.get(url, allow_redirects=True)
open('LatLngData.csv', 'wb').write(r.content)

print("Completed downloading the file...")
input("Press any key to close the window!")
