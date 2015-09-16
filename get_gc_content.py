#!/usr/bin/python
"""
Script that takes a sequence file in FASTA format and returns
the GC content of each sequence entry

Author: Emanuel Langit
email: emanuel.langit@fastmail.fm
"""

from __future__ import division
from __future__ import print_function 
import sys
import re

def getGcContent(seq):
	length = len(seq)
	gCount = seq.count('G')
	cCount = seq.count('C')
	gc_content = round((gCount + cCount) / length, 4)
	return gc_content

filename = sys.argv[1]

fastaFile = open(filename)

started = 0
nucleotideSeq = ""

for line in fastaFile:
	line = line.rstrip('\n')
	if not(re.search('[a-zA-Z0-9]', line)):
		continue

	if line.startswith('>'):
		if started == 1:
			print("\t" + str(getGcContent(nucleotideSeq)))

		line = line.replace('>', '', 1)
		lineArray = line.split()
		print(lineArray[0], end="")
		nucleotideSeq = ""
		
	else:
		line = line.upper()
		nucleotideSeq += line
		
	started = 1

fastaFile.close()
