"""
A script to fetch json data from Melange's website.

I found out the URL by simply looking at the XHR requests being sent
from the project list page.
"""

import os
import json
import urllib.request as UR
import urllib.parse as UP

# What to fetch? 'projects' or 'org'?
what = 'projects'

if not os.path.isdir(what):
    os.mkdir(what)

# The melange website
root = "http://www.google-melange.com"

# Let the game begin
for year in range(2009, 2015):

    print("Year: " + str(year))

    # Loop Controls
    nxt, start, end = "", 1, 100

    # Create the folder if it doesn't already exist
    if not os.path.isdir(os.path.join(what, str(year))):
        os.mkdir(os.path.join(what, str(year)))

    # The Ideas URL
    ideas = "/gsoc/projects/list/google/gsoc" + str(year) + "?"

    # Gotta catch 'em all
    while nxt != "done":

        # Path to the current json file
        json_name = os.path.join(os.path.join(what, str(year)),
                                 str(start)+"-"+str(end)+".json")

        # I don't know what some of these parameters mean
        # but the thing that matters is - It works!
        params = UP.urlencode({'fmt':'json', 'limit':'100', 'idx':'0',
                               '_':'1403807190239', "start": nxt})

        # Download only missing pieces of the puzzle
        if os.path.isfile(json_name):
            print("\tExisting file: " + json_name)
            with open(json_name, "r") as json_file:
                json_data = json.load(json_file)
        else:
            url = root + ideas + params
            print("\tDownloading file: " + json_name + ", from: " + url)
            with open(json_name, "w") as json_file:
                site = UR.urlopen(url)
                json_data = json.loads(site.read().decode())
                json.dump(json_data, json_file, sort_keys=True, indent=2)

        # Next, please
        nxt = json_data["next"]
        start, end = start+100, end+100

# Whew!!
print("All Done!")
