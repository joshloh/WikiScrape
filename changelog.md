# WikiScrape Project changelog
- Authors: Denton Phosavanh Joshua Loh
- For: Self-improvement
- Latest Version: 0.1.1
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
- Only parsing relevant parts of each page as per https://www.crummy.com/software/BeautifulSoup/bs4/doc/#parsing-only-part-of-a-document Should boost efficiency significantly

### Known bugs
- ~~Pages with "Wikipedia:" and "Help:" being included in the outgoing link list when they shouldn't be~~	

## [0.1.1] - 2016-12-05
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