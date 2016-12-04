#!/bin/bash/

python get_links.py $1 > bin.txt
sort -u bin.txt