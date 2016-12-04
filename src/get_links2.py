# Code written by:
# Joshua Loh
# Denton Phosavanh
# 2016

import urllib2
from bs4 import BeautifulSoup
import sys
from Queue import *

# Takes in a list of strings, removes duplicates (and sorts)
def streamline(a):
	a = list(set(a))
	a.sort()
	return a

# From a string in the form of "Wikipedia_Article_Name",
# create the BeaitifuilSoup object of it, and return
# a list of all the links that it contains
def get_links(s):
	# Set up the scraper
	wiki = "https://en.wikipedia.org/wiki/" + s
	page = urllib2.urlopen(wiki)
	soup = BeautifulSoup(page, "html.parser")

	# Stores the name of all the outgoing Wiki pages
	link_array = []

	# Extract every <a> that is in a <p>, store them in link_array
	every_para = soup.find_all("p")
	for para in every_para:
		# print para.get_text()
		para_links = para.find_all("a")
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
		exit(11)
	elif s == "Adolf_Hitler" or s == "Hitler":
		print("YEAH YEAH YEAH YEAH YEAH YEAH YEAH")
		print("Got to " + s + " at depth " + str(depth))
		exit(12)

	indent = "\t"*depth
	print indent + "Visiting: " + s

	# Output all the links that can be seen from this page
	indent += "\t"
	link_array = get_links(s)
	for l in link_array:
		print(indent + l)

	# Shortcut search for Hitler
	global visited_links
	for l in link_array:
		if l == "Adolf_Hitler" or l == "Hitler":
			dfs(l, depth+1, DEPTH_LIMIT)

	# recursion
	# Another sneaky base case
	for l in link_array:
		if not l in visited_links:
			visited_links.add(l)
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


#+-------------------------------
#| main
#+-------------------------------
# If no argument is passed, exit
if len(sys.argv) < 2:
	print "Error, invalid number of arguments."
	print "Example usage: " + sys.argv[0] + " Article_Name"
	sys.exit()

# Keep track of which links have been visited
visited_links = set()
visited_links.add(sys.argv[1])
dfs(sys.argv[1], 0, 1)
# bfs(sys.argv[1])