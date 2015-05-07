"""
A list of organizations that are consistently being selected for past n years.
"""

import json

orgs = {}

# Load all data from json files to a list of dicts
for year in range(2009, 2015):
    with open("../data/org/%d.json" % year) as inp:
        data = json.load(inp)
        orgs[year] = set([org['org_id'] for org in data['orgs']])

years = list(orgs)

# Stores the big players
big = {0: set()}

# Todo: Is this code Pythonic enough?
rank = 1
for year in years[:-1]:

    # Begin with entries of this year
    big[rank] = orgs[year]

    # Intersect orgs selected in the past years
    for year in years[years.index(year):]:
        big[rank] &= orgs[year]

    # Filter out previous year entries
    for previous in range(1, rank):
        big[rank] -= big[previous]

    rank += 1

# Print out results
print("\nThese are the orgs which have most chances of getting selected.\n")
for rank in big:
    if rank == 0:
        continue

    print("Selected from %d - %d:" %
          (years[rank - 1], years[-1]), sorted(big[rank]))
    print()
