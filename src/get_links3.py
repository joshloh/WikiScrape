# Code written by:
# Joshua Loh
# Denton Phosavanh
# 2016

# Webscraping
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

# Other
import argparse
import sys
from queue import *

# Takes in a list of strings, removes duplicates (and sorts)
def streamline(a):
	a = list(set(a))
	a.sort()
	return a

# From a string in the form of "Wikipedia_Article_Name",
# create the BeautifulSoup object of it, and return
# a list of all the links that it contains
def get_links(s):
	# Set up the scraper
	wiki = "https://en.wikipedia.org/wiki/" + s
	page = urllib.request.urlopen(wiki)
	# soup = BeautifulSoup(page, "html.parser")
	soup = BeautifulSoup(page, "html.parser", parse_only=SoupStrainer("p"))

	# Stores the name of all the outgoing Wiki pages
	link_array = []

	# Extract every <a> that is in a <p>, store them in link_array
	# every_para = soup.find_all("p")
	# for para in every_para:
	# 	# print para.get_text()
	para_links = soup.find_all("a")
	for para_link in para_links:
		link = para_link.get("href")
		# Only pull (relevant parts of) relevant pages
		if link.startswith("/wiki/") and (link[6:].startswith("Wikipedia:") == False) and (link[6:].startswith("Help:") == False):
			link_array.append(link[6:])

	# Return link_array
	return streamline(link_array)

# Recursive DFS
def dfs(s, depth, DEPTH_LIMIT):
	# Base cases, have reached depth limit, or found Hitler
	if depth >= DEPTH_LIMIT:
		return
		# exit(11)
	# elif s == "Adolf_Hitler" or s == "Hitler":
	# 	print("YEAH YEAH YEAH YEAH YEAH YEAH YEAH")
	# 	print("Got to " + s + " at depth " + str(depth))
	# 	exit(12)
	global visited_links
	visited_links.add(s)
	indent = "\t"*depth
	print(indent + "Visiting: " + s)

	# Output all the links that can be seen from this page
	indent += "\t"
	link_array = get_links(s)
	for l in link_array:
		print(indent + l)

	# Shortcut search for Hitler
	# for l in link_array:
	# 	if l == "Adolf_Hitler" or l == "Hitler":
	# 		dfs(l, depth+1, DEPTH_LIMIT)

	# recursion
	# Another sneaky base case
	for l in link_array:
		if not l in visited_links:
			dfs(l, depth+1, DEPTH_LIMIT)

def bfs(s):
	global visited_links
	fringe = Queue()
	fringe.put(s)
	print(s)
	# Keep searching until have run out of potential expansions
	while (not fringe.empty()):
		current_link = fringe.get()
		# print(current_link)
		link_array = get_links(current_link)
		for l in link_array:
			print("Child: " + l)
			# Check for exit state
			if l == "Aboriginal_peoples_in_Canada" or l == "Hitler":
				print("Found")
				exit(13)

			# If a node has not already been visited, queue for expansion
			if not l in visited_links:
				fringe.put(l)
				visited_links.add(l)


def argparse_setup():
	parser = argparse.ArgumentParser()
	
	# Which search to use
	parser.add_argument(
		"-s", "--search",
		default = "bfs",
		choices = ["dfs", "bfs"],
		help = "which search to use (default: bfs)"	
	)
	
	# dfs depth
	parser.add_argument(
		"-d", "--depth",
		default = 2,
		type = int,
		help = "the depth to which dfs should search (default = 2). use in conjunction with dfs)"
	)
	
	parser.add_argument(
		"-p", "--page",
		default = "Sun_Dance",
		help = "which page to start the search from (formatted to Wikipedia standards)"
	)
	
	# Level of output
	parser.add_argument(
		"-v", "--verbosity",
		default = 1,
		type = int,
		choices = [0, 1, 2, 3, 4, 5],
		help = "the level of output to use (0 is low, 5 is high)"
	)
	
	return parser
	
#+-------------------------------
#| main
#+-------------------------------
# If no argument is passed, exit
# if len(sys.argv) < 3:
	# print("Error, invalid number of arguments.")
	# print("Example usage: " + sys.argv[0] + " [Article_Name] [DFS_DEPTH]")
	# sys.exit()

parser = argparse_setup()
args = parser.parse_args()
print(args)

# Keep track of which links have been visited
visited_links = set()
visited_links.add(args.page)

if args.search == "dfs":
	dfs(args.page, 0, args.depth)
else:
	bfs(args.page)
	
# visited_links.add(sys.argv[1])
# dfs(sys.argv[1], 0, int(sys.argv[2]))
# bfs(sys.argv[1])