"""
Returns the number of times an organization got selectd for GSoC.
"""

import json

name = raw_input("Enter the name of the org:")
name = name.lower()

years = []
count = 0


# Load all data from json files to a list of dicts
for year in range(2009, 2015):
    with open("../data/org/%d.json" % year) as inp:
        data = json.load(inp)

        for org in data['orgs']:
            orgn = org['name'].lower()

            if name in orgn:
                count = count + 1
                years.append(year)
                break


if count == 1:
    print '%s has been selected %d time' % (name, count)
    # print 'For the following year - %d' % years
    print 'For the following year', years

else:
    print '%s has been selected %d times' % (name, count)
    print 'For the following years', years
