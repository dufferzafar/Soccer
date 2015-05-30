"""
Returns the number of time a student got selected for GSoC.
"""

import json
import sys

years = []
count = 0
try:
    if sys.argv[1]:
        handle = sys.argv[1]
    else:
        raise
except:
    print("Give the handle of student as arguement.")
    quit()

# Load all data from json files to a list of dicts
for year in range(2009, 2015):
    with open("../data/projects/%d.json" % year) as inp:
        data = json.load(inp)

        for project in data['projects']:
            # Use a student's username rather than full name
            stu = project['link'].split('/')[-2]

            if handle == stu:
                count = count + 1
                years.append(year)
                break


if count == 1:
    print '%s has been selected %d time' % (handle, count)
    # print 'For the following year - %d' % years
    print 'For the following year', years

else:
    print '%s has been selected %d times' % (handle, count)
    print 'For the following years', years
