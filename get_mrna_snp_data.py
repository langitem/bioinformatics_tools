#!/usr/bin/python
"""
Author: Emanuel Langit
Given a list of URLs (which should have been generated using the
create_mrna_snp_url.py script, this application will print to 
stdout in tab delimited format: RS ID, mRNA accession, chr position,
and mRNA position)
"""

import sys
import urllib2
import time

urlListFile = sys.argv[1]
urlList = open(urlListFile)

for line in urlList:
	line = line.rstrip("\n")
	print line



urlList.close()