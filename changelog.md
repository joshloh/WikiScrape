# WikiScrape Project changelog
- Authors: Denton Phosavanh, Joshua Loh
- For: Self-improvement
- Latest Version: 0.3.1
---
## GLOSSARY
[x] - currently not used

## Upcoming Changes/Goals

### Things to add or change
- Run test cases on more pages
- Make an array of potential end cases instead of a fixed number
- Some kind of output for the searches to see the path from start to beginning
- Recognition of links within tables (and possibly other structures)
	- Example: Running it on [this page](https://en.wikipedia.org/wiki/List_of_chemical_compounds_with_unusual_names) at depth 1 will only register 13 outgoing links, whereas there should be hundreds.
	- As a side-note, we also want to avoid links in templates such as at the bottom of [this page](https://en.wikipedia.org/wiki/AK-102), so we need a way to distinguish between them
- Use `argparse` package to parse arguments
	- Implement flags for switching on/off output
	- Actually make use of the verbosity flag
- Not including any links from the `See also` area
- I suspect we didn't implement DFS correctly. It looks like BFS right now...
	- An example run
		```
		$ python3 get_links3.py -v 1 -a dfs -d 2 -s Br%C3%BCgger_%26_Thomet_GL06 -t Australia
		Namespace(algorithm='dfs', depth=2, start='Br%C3%BCgger_%26_Thomet_GL06', target='Australia', verbosity=1)
		Visiting: Br%C3%BCgger_%26_Thomet_GL06
				Visiting: 40_mm_grenade
				Visiting: Ammunition
				Visiting: Br%C3%BCgger_%26_Thomet
				Visiting: Grenade_launcher
				Visiting: Heckler_%26_Koch_HK69A1
				Visiting: M79_grenade_launcher
				Visiting: Non-lethal_weapon
				Visiting: Thun
		```
	- However, I think after `40 mm grenade`, it should go into the first link in `40 mm grenade`, not the second link in the `GL06` page (which is `Ammunition`)


### Known bugs
- ~~Pages with "Wikipedia:" and "Help:" being included in the outgoing link list when they shouldn't be~~
- ~~Pages are pre-emptively added to `visited_links` so they aren't explored properly in DFS~~
- Unable to visit pages named similarly to `Brügger & Thomet`. Spacing and possibly the umlaut is an issue
	- Possibly using `unidecode` library to sort out the umlaut?


## [0.3.1] - 2017-04-26
### Added
- Strips everything after the last `#` character in a Wikipedia link. This addresses the item:
	- Prevent the consideration of pages such as [Germant#Law](https://en.wikipedia.org/wiki/Germany#Law) and [Germany#Music](https://en.wikipedia.org/wiki/Germany#Music) as "different" pages
	- However, this introduces another bug - duplicate pages in the `link_array` that gets returned from `get_links`
- notable tests file (found in `docs/notable_tests.txt`)

### Changed
- capital 'W' for Wikipedia in the `get_links` error message
- using a set instead of an array in `get_links`
- changed `streamline` to therefore assume the input param is a set
- uncommented `dfs` found exit condition


## [0.3.0] - 2016-12-21
### Added
- Use of argparse to parse arguments. 
	- Possible arguments:
		- a/algorithm - which page to search for
		- d/depth - how deep dfs should go
		- s/start - start page of the search
		- t/target - target page of the search
		- v/verbosity - how much output should be made
	- Added `description` and `epilog` fields for the argparse constructor
- Exception handling inside `get_links` when creating `page`

### Changed
- Removed a bunch of commented out code and unused code
- Added Denton to `LICENCE`


## [0.2.3] - 2016-12-13
### Added
- A Python3 port for `get_links3.py`


## [0.2.2] - 2016-12-06
### Added
- Extra parameter in main, used for DFS depth

### Changed
- Fixed DFS bug (moved adding to visited_links to earlier in the function)


## [0.2.1] - 2016-12-06
### Added
- SoupStrainer optimisation
	- SoupStrainer extracts only `<p>` tags, `find_all()` still used for `<a>` tags

### Changed
- Removed target in DFS (just commented out for now)


## [0.2.0] - 2016-12-05
### Added
- BFS implementation
	- The current BFS implementation searches for "Aboriginal_peoples_in_Canada" (from "Sun_Dance")
	- BFS works, but there still are more things to be added
	- BFS outputs the children to stdout as the parent expands all children

### Changes
- Uncommented sort, makes it easier to predict and interpret output


## [0.1.0] - 2016-12-05
### Added
- File directories
	- Codebase
		- get_links.py [x]
		- get_links2.py
		- main.sh [x]
		- Makefile [x]
		- streamline.sh [x]
	- Documentation
		- benchmarks.docx
		- changelog.md
		- ideas.txt
		- initial_ideas.docx
		- reference.docx

### Changes
- Implemented DFS
	- DFS prints the parent as it visits it, and prints all the children when the parent has finished expanding
- Added functionality for searching for a wiki page, but currently hard-coded
- Removed sorting
- Delegated get_links to a helper function (so it can be used for BFS and DFS)
- Fixed a bug for pages starting with "Wikipedia:" and "Help:"