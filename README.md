
![Soccer Logo](/site/img/logo.png)

A better way to find GSoC projects and organizations.

The current (working) prototype is live at: http://dufferzafar.github.io/soccer/

The logo uses the 'Soccer Ball' by Jake Schirmer from The Noun Project, colored amateurishly by me.

## Current Status

Currently the application is just a prototype.

I had plans to complete this before the next GSoC so people can actually use it, but I don't currently have the time that needs to be put into this project.

If you are interested in this, you can just fork the thing and ask me if you need any kind of help.

I'd really love to see this turn into something.

## Running Locally

* Make sure you have node setup. Test by running `node` & `npm`.

* Clone the repo: `git clone http://github.com/dufferzafar/soccer`

* `cd soccer`
* `npm install`

* `cd site`
* `bower install`

* `gulp`

## Todo

* The app currently uses the old datasets that don't contain the project/org descriptions. Efficiently loading the new dataset will be a bit challenging.

You can run the script to scrape the data yourself or download it from [releases](https://github.com/dufferzafar/soccer/releases/).

* The UI needs to be slick. It should be able to display as much data as possible without affecting usability.

* The search bar should allow filters, like `org:metabrainz year:2014 sort:asc`
*to show all metabrainz projects for the year 2014 in an ascending order (by project title)*

* Apart from the search, soccer had another motive too, and that was to dig into the data and find out valuable insights like, the ratio of web dev projects to other categories, how many of the students turn into mentors.
