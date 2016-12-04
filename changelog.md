# WikiScrape Project changelog
- Authors: Denton Phosavanh Joshua Loh
- For: Self-improvement
- Latest Version: 0.1.0
---
## GLOSSARY
[x] - currently not used

## Upcoming Changes/Goals

### Things to add or change
- Run test cases on more pages
- Implement BFS
- Implement flags for switching on/off output
- Make an array of potential end cases instead of a fixed number

### Known bugs
- ~~Pages with "Wikipedia:" and "Help:" being included in the outgoing link list when they shouldn't be~~	


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
- Added functionality for searching for a wiki page, but currently hard-coded
- Removed sorting
- Delegated get_links to a helper function (so it can be used for BFS and DFS)
- Fixed a bug for pages starting with "Wikipedia:" and "Help:"