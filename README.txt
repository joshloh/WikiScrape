Download the repository
Run python get_links2.py [WIKIPEDIA_ARTICLE_NAME]
e.g. python get_link2.py Sun_Dance
This will search every outgoing link from Sun Dance recursively
Searches until
- it finds the Wikipedia article for Adolf Hitler
- it reachesd the depth limit (currently hard-coded)
- there are no more unique articles to search
Prints to std output in the form of

Article Name
	link1
	link2
	.
	.
	linkn
	Link1 Article Name
		linkA
		linkB
		.
		.
	Link2 Article Name

etc.

TO CUSTOMISE:

- Depth limit can be modified by changing dfs call parameters
- Search page is currently hard-coded. Can change by searching for every instance of "Adolf Hitler" and changing to the desired search article
	- This will be made easier in future versions, most liely as an additional argument
- To run BFS, comment out the DFS call and uncomment the BFS call