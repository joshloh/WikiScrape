# Code written by:
# Joshua Loh, Denton Phosavanh
# 2016

# Webcraping
import urllib.request, urllib.error, urllib.parse  # Load web page
from bs4 import BeautifulSoup   # Easier scraping
from bs4 import SoupStrainer    # More efficient loading

# Other
import argparse
import textwrap
import sys
from unidecode import unidecode # Strip diactritics from characters
from queue import *

# Takes in a set, and returns a sorted list
def streamline(a):
	a = list(a)
	a.sort()
	return a


# From a string in the form of "Wikipedia_Article_Name",
# create the BeautifulSoup object of it, and return
# a list of all the links that it contains
def get_links(s):
	# Set up the scraper
	wiki = "https://en.wikipedia.org/wiki/" + s
	
	try:
		page = urllib.request.urlopen(wiki)
	except urllib.error.HTTPError:
		print("An error occurred in opening this page")
		print("This is most likely due to either of two reasons:")
		print("a) Your internet connection isn't internetting")
		print("b) The Wikipedia page %s does not exist" % wiki)
		exit(3)
	except Exception:
		import traceback
		exit(4)
	else:
		# only load the parts of the page contained in a <p>
		soup = BeautifulSoup(page, "html.parser", parse_only=SoupStrainer("p"))

	# Stores the name of all the outgoing Wiki pages
	link_array = set() #  Use a set to avoid duplicate entries

	# Extract every <a> that is in a <p>, store them in link_array
	para_links = soup.find_all("a")
	for para_link in para_links:
		link = para_link.get("href")
		# Only pull (relevant parts of) relevant pages
		if link.startswith("/wiki/") and (not link[6:].startswith("Wikipedia:")) and (not link[6:].startswith("Help:")):
			# Strip everything after the last `#` symbol 
			# in the link (Wikipedia fragment identifier)
			last_octothorpe = link.rfind('#')
			if last_octothorpe == -1: # No octothorpe
				link_array.add(link[6:])
			else:
				link_array.add(link[6:last_octothorpe])

	# Return the result.
	# Call this if you want it sorted,
	# otherwise just return link_array
	return streamline(link_array)


# Recursive depth-first search
def dfs(site, depth, DEPTH_LIMIT, target, verbosity):
	# Base cases, have reached depth limit, or found target
	if depth >= DEPTH_LIMIT:
		return	
	elif site == target:
		print("Got to " + site + " at depth " + str(depth))
		exit(12)
		
	global visited_links
	visited_links.add(site)
	indent = "\t"*depth
	print(indent + "Visiting: " + site)

	# Output all the links that can be seen from this page
	indent += "\t"
	link_array = get_links(site)
	for l in link_array:
		print(indent + l)

	# recursion (Another sneaky base case)
	for l in link_array:
		if not l in visited_links:
			dfs(l, depth+1, DEPTH_LIMIT, target, verbosity)

# Iterative breadth-first search
def bfs(site, target, verbosity):
	global visited_links
	fringe = Queue()
	fringe.put(site)
	print(site)
	# Keep searching until have run out of potential expansions
	while (not fringe.empty()):
		current_link = fringe.get()
		# print(current_link)
		link_array = get_links(current_link)
		for l in link_array:
			print("Child: " + l)
			# Check for exit state
			if l == "Aboriginal_peoples_in_Canada" or l == target:
				print("Found")
				exit(13)

			# If a node has not already been visited, queue for expansion
			if not l in visited_links:
				fringe.put(l)
				visited_links.add(l)


def argparse_setup():
	parser = argparse.ArgumentParser(
		formatter_class=argparse.RawDescriptionHelpFormatter,
		# Describe the program and arguments briefly
		description=textwrap.dedent("""\
			Finds a path between pages [start] and [target] on Wikipedia
			Set options on how the program will run
			Default values:
			---------------
			 a : bfs
			 d : 2
			 s : Sun_Dance
			 t : Adolf_Hitler
			 v : 1
			---------------
			"""),
			
		# Gloss over exit details
		epilog=textwrap.dedent("""\
			Exit status:
			------------
			 0 : Everything worked as planned
			 2 : Error parsing arguments
			 3 : urllib.error.HTTPError
			 4 : General exception from urllib.request
			""")
	)
	
	# Which search to use
	parser.add_argument(
		"-a", "--algorithm",
		default = "bfs",
		choices = ["dfs", "bfs"],
		help = "which search to use"	
	)
	
	# dfs depth
	parser.add_argument(
		"-d", "--depth",
		default = 2,
		type = int,
		help = "maximum search depth of dfs. use in conjunction with dfs)"
	)
	
	# Starting page
	parser.add_argument(
		"-s", "--start",
		default = "Sun_Dance",
		help = "which page to start the search from (formatted to Wikipedia standards)"
	)
	
	# Target page
	parser.add_argument(
		"-t", "--target",
		default = "Adolf_Hitler",
		help = "the page for which to search"
	)
	
	# Level of output
	parser.add_argument(
		"-v", "--verbosity",
		default = 1,
		type = int,
		help = "the level of output to use (higher => more output)"
	)
	
	return parser


#+-------------------------------
#| main
#+-------------------------------
# Parse the program's arguments
parser = argparse_setup()
args = parser.parse_args()
if args.verbosity >= 1:
	print(args)
	
args.start = unidecode(args.start)

# Keep track of which links have been visited
visited_links = set()
visited_links.add(args.start)

# Run either dfs or bfs, depending on arguments
if args.algorithm == "dfs":
	dfs(args.start, 0, args.depth, args.target, args.verbosity)
else:
	bfs(args.start, args.target, args.verbosity)