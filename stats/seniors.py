"""
A list of students who were selected more than once.
"""

import json

students = {}

# Load all data from json files to a list of dicts
for year in range(2009, 2015):
    with open("../data/projects/%d.json" % year) as inp:
        data = json.load(inp)

        for project in data['projects']:
            # Use a student's username rather than full name
            stu = project['link'].split('/')[-2]

            if stu in students:
                students[stu].append(year)
            else:
                students[stu] = [year]

# Students selected more than once
seniors = {s: students[s] for s in students if len(students[s]) > 2}

# Sort based on number of years a student was selected
seniors_sorted = sorted(seniors.items(), key=lambda x: len(x[1]), reverse=True)

# Print
for s in seniors_sorted:
    print(s[0], s[1])
