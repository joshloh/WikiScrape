# WikiScrape Project changelog
- Authors: Denton Phosavanh Joshua Loh
- For: Self-improvement
- Latest Version: 0.2.2
---
## GLOSSARY
[x] - currently not used

## Upcoming Changes/Goals

### Things to add or change
- Run test cases on more pages
- Implement flags for switching on/off output
- Make an array of potential end cases instead of a fixed number
- Some kind of output for BFS to see the path from start to beginning
- Prevent the consideration of pages such as `https://en.wikipedia.org/wiki/Germany#Law` and `https://en.wikipedia.org/wiki/Germany#Music` as "different" pages
- Recognition of links within tables (and possibly other structures)
	- Example: Running it on [this page](List_of_chemical_compounds_with_unusual_names) at depth 1 will only register 13 outgoing links, whereas there should be hundreds.
	- As a side-note, we also want to avoid links in templates such as at the bottom of [this page](https://en.wikipedia.org/wiki/AK-102), so we need a way to distinguish between them
- Allow user to specify "target" page (i.e. not restricted Hitler)

### Known bugs
- ~~Pages with "Wikipedia:" and "Help:" being included in the outgoing link list when they shouldn't be~~
- ~~Pages are pre-emptively added to `visited_links` so they aren't explored properly in DFS~~

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