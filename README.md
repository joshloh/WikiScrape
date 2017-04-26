# WikiScrape project readme file
## Requirements
- Python 2.x OR Python 3.x (our 2.x version is being discontinued, so Python 3.x preferred)
- BeautifulSoup4
	- Pip
		- If using Cygwin, needs the `python-setuptools` package
		- Install pip by running `easy_install-2.x pip` (where `2.x` is the Python2 version that is installed, or `3.x` if using `get_links3.py`)
		- Install BeautifulSoup by running `pip install beautifulsoup4` or using `pip3`
- unidecode

## Instructions
- **NOTE**: `get_links3.py` is the one we're rolling with. `get_links2.py` exists, but is no longer being worked on.
- Download the repository
- Run `python3 get_links3.py [-h] [-a {dfs,bfs}] [-d DEPTH] [-s START] [-t TARGET] [-v VERBOSITY]`
- OR `python get_links2.py [-h] [-a {dfs,bfs}] [-d DEPTH] [-s START] [-t TARGET] [-v VERBOSITY]`
- e.g. `python3 get_link3.py -s Sun_Dance -t Australia -a bfs`
- Searches until every outgoing link from [START] until:
	- it finds reaches the Wikipedia article for [TARGET]
	- it reaches the [DEPTH] (if using dfs)
	- there are no more unexplored articles to search (unreachable)
	
- For argument help, run `python3 get_links3.py -h`

- Exit status:
	- 0: Everything worked as planned
	- 2: Error parsing arguments
	- 3: urllib.error.HTTPError
	- 4: General exception from urllib.request
	
## Output
- Prints to std output in the form of

```
Article Name
	link1
	link2
	...
	...
	linkn
	Link1 Article Name
		linkA
		linkB
		...
		...
	Link2 Article Name

etc.
```