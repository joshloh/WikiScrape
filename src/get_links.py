# Code written by:
# Joshua Loh
# Denton Phosavanh
# 2016

import urllib2
from bs4 import BeautifulSoup
import sys

# if no argument is passed, exit
if len(sys.argv) < 2:
	print "Error, invalid number of arguments."
	print "Example usage: " + sys.argv[0] + " Article_Name"
	sys.exit()

wiki = "https://en.wikipedia.org/wiki/" + sys.argv[1]
page = urllib2.urlopen(wiki)
soup = BeautifulSoup(page, "html.parser")
# print(soup.prettify())

all_para = soup.find_all("p")
for para in all_para:
	# print para.get_text()
	para_links = para.find_all("a")
	for para_link in para_links:
		link = para_link.get("href")
		if link.startswith("/wiki/"):
			# print para_link.get_text()
			print link[6:]
			# print

# all_links = soup.find_all("a")
# for link in all_links:
# 	print "LINK NAME"
# 	name = link.get_text()
# 	if name == "":
# 		print "n/a"
# 	else:
# 		print name
# 	print "LINK URL"
# 	print link.get("href")
# 	print