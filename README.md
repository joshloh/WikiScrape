# WikiScrape project readme file
## Requirements
- Python 2.x OR Python 3.x
- BeautifulSoup4
	- Pip
		- If using Cygwin, needs the `python-setuptools` package
		- Install pip by running `easy_install-2.x pip` (where `2.x` is the Python2 version that is installed)
		- Install BeautifulSoup by running `pip install beautifulsoup4`

## Instructions
- Download the repository
- Run `python get_links2.py [WIKIPEDIA_ARTICLE_NAME]`
- OR `python3 get_links2.py [WIKIPEDIA_ARTICLE_NAME]`
- e.g. `python get_link2.py Sun_Dance`
- This will search every outgoing link from Sun Dance recursively
- Searches until
	- it finds the Wikipedia article for the target page (currently hard-coded to Adolf Hitler)
	- it reachesd the depth limit (currently hard-coded)
	- there are no more unexplored articles to search
	
### Output
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

### To Customise
- Depth limit can be modified by changing `dfs` call arguments
- Target page is currently hard-coded. Can change by searching for every instance of "Adolf Hitler" and changing to the desired search article
	- This will be made easier in future versions, most liely as an additional argument
- To run BFS, comment out the DFS call and uncomment the BFS call (in main)