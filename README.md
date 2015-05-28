
![Soccer Logo](/site/img/logo.png)

A better way to find GSoC projects and organizations.

The current (working) prototype is live at: http://dufferzafar.github.io/Soccer/

The logo uses the 'Soccer Ball' by Jake Schirmer from The Noun Project, colored amateurishly by me.


## Running Locally

* Make sure you have node setup. Test by running `node` & `npm`.

* Clone the repo: `git clone http://github.com/dufferzafar/soccer`

* `cd soccer`
* `npm install`

* `cd site`
* `bower install`

* `gulp`

## Known Issues

* The only legitimate error that you may face while trying to build this project is the `gulp version mismatch` i.e the version of gulp that is used in this project may differ from the version present on your system.

Here is the [**Solution**](https://github.com/gulpjs/gulp/issues/171)

## Todo

* Fetch  data for the following years -
    * 2005-2008 https://developers.google.com/open-source/soc/
    * 2015

* Think of a way of displaying the stats information like - students who've been selected more than once, etc.

* The app currently uses the old datasets that don't contain the project/org descriptions. Efficiently loading the new dataset will be a bit challenging.

You can run the script to scrape the data yourself or download it from [releases](https://github.com/dufferzafar/soccer/releases/).

* The UI needs to be slick. It should be able to display as much data as possible without affecting usability.

* The search bar should allow filters, like `org:metabrainz year:2014 sort:asc`
*to show all metabrainz projects for the year 2014 in an ascending order (by project title)*
