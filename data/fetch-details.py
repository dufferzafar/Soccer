"""
Scrape Project details from Melange webpages.
"""

import sys

# What to fetch? 'projects' or 'org'?
try:
    if sys.argv[1] in ['projects', 'org']:
        what = sys.argv[1]
    else:
        raise
except:
    print("To fetch projects:\tpython fetch-details.py projects")
    print("To fetch orgs:\t\tpython fetch-details.py org")
    quit()

def download_or_read(out, link, url):
    content = ""
    if os.path.isfile(out):
        print("\t Reading: " + link)
        with open(out) as out:
            content = out.read()
    else:
        print("\t Downloading: " + link)
        response = requests.get(url)
        content = response.text
        with open(out, "w") as out:
            out.write(content.encode('utf-8', 'replace'))

    return content

import os
import json
import requests
from lxml import html

out_dir = what + "-details"
if not os.path.isdir(out_dir):
    os.mkdir(out_dir)

root = "http://www.google-melange.com"

for year in range(2009, 2015):
    print("Year: " + str(year))

    # Create the output folder if it doesn't already exist
    if not os.path.isdir(os.path.join(out_dir, str(year))):
        os.mkdir(os.path.join(out_dir, str(year)))

    # Read the json file
    json_name = os.path.join(os.path.join(what, str(year)+".json"))

    with open(json_name) as jsonfile:
        json_data = json.load(jsonfile)

    # Ever heard about Spaghetti code?
    orgs_or_projects = 'orgs' if what == 'org' else 'projects'
    index = -1 if what == 'org' else -2

    items = json_data[orgs_or_projects]
    for item in items:
        url = root + item['link']
        out_file = os.path.join(out_dir, str(year),
                                url.split('/')[index]+".html")

        content = download_or_read(out_file, item['link'], url)
        parsed_body = html.fromstring(content)

        if what == 'projects':
            desc = parsed_body.xpath('/html/body/div[1]/div[2]/div'
                                     '/div[2]/div/div/p[3]/text()')[0]

            item['description'] = desc.strip()
        else:
            desc = parsed_body.xpath('/html/body/div[1]/div[2]/div/div[2]'
                                     '/div/div[3]/div/div[1]')[0]

            try:
                home = parsed_body.xpath('/html/body/div[1]/div[2]/div/div[2]/div'
                                         '/div[3]/div/div[2]/a[2]/@href')[0]
            except:
                home = parsed_body.xpath('/html/body/div[1]/div[2]/div/div[2]/div'
                                         '/div[3]/div/div[2]/a/@href')[0]

            item['description'] = desc.text_content().strip()
            item['homepage'] = home.strip()


    json_name = os.path.join(os.path.join(out_dir, str(year)+".json"))
    with open(json_name, "w") as jsonfile:
        json.dump({"year": year, orgs_or_projects: items}, jsonfile)

# Whew!!
print("All Done!")
