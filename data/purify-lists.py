"""
The data fetched from the Melange site has a lot of stuff that we
don't need. So this script purifies the data by removing unneeded
fields.
"""

import os
import re
import json

# What to purify? 'projects' or 'org'?
what = 'projects'

for year in range(2009, 2015):
    if not os.path.isdir(os.path.join(what, str(year))):
        continue

    print("Year: " + str(year))

    # Loop Controls
    nxt, start, end = "", 1, 100

    # A pure list of projects
    pure_list = []

    # Gotta catch 'em all
    while nxt != "done":

        # Path to the current json file
        json_name = os.path.join(os.path.join(what, str(year)),
                                 str(start)+"-"+str(end)+".json")

        print("\t" + json_name)

        with open(json_name) as jsonfile:
            json_data = json.load(jsonfile)

        # This is the old impure data
        impure_list = json_data["data"][nxt]

        # and we're going to purify it
        for imp in impure_list:
            pure = {}
            if what == 'projects':
                pure["mentors"] = imp["columns"]["mentors"]
                pure["organization"] = imp["columns"]["organization"]
                pure["student"] = imp["columns"]["student"]
                pure["title"] = imp["columns"]["title"]
                pure["link"] = imp["operations"]["row"]["link"]
            else:
                ideas = re.match(r'<a href=\"(.*?)\"',
                                 imp["columns"]["ideas"])
                if ideas:
                    pure["ideas"] = ideas.group(1)
                pure["name"] = imp["columns"]["name"]
                pure["org_id"] = imp["columns"]["org_id"]
                pure["tags"] = imp["columns"]["tags"]
                pure["link"] = imp["operations"]["row"]["link"]
            pure_list.append(pure)

        # Next, please
        nxt = json_data["next"]
        start, end = start+100, end+100

    # Dump the data
    with open(os.path.join(what, str(year)+".json"), "w") as pure_json:
        if what == 'projects':
            json.dump({"year": year, "projects": pure_list}, pure_json)
        else:
            json.dump({"year": year, "orgs": pure_list}, pure_json)

# Whew!!
print("All Done!")
