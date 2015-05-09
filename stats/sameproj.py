"""
Projects which have more than one students assigned to them.
"""

import json

projects = dict()

# Load all data from json files to a list of dicts
for year in range(2009, 2015):
    with open("../data/projects/%d.json" % year) as inp:
        data = json.load(inp)

        for project in data['projects']:

            stu = project['student']
            tit = project['title']

            if tit in projects:
                projects[tit].append(stu)
            else:
                projects[tit] = [stu]

# Projects with more than one student
same = {s: projects[s] for s in projects if len(projects[s]) > 1}

for s in same:
    print(s, same[s])
