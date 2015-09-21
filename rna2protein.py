#!/usr/bin/python
"""
Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
Return: The protein string encoded by s.
"""

import sys
import re

# function to translate RNA sequence into protein:
def translateRnaSeq2protein(nucSeq):
	print(nucSeq) # remove this later


filename = sys.argv[1]
fastaFile = open(filename)
currentNucleotideSeq = ""

for line in fastaFile:
	# skip line if it doesn't contain any alphanumeric characters:
	if not(re.search('[a-zA-Z0-9]', line)):
		continue
		
	line = line.rstrip('\n')
	
	started = 0 # variable to check if first sequence entry read
	# if current line is a defline:
	if line.startswith('>'):
		if started == 1:
			print(translateRnaSeq2protein(nucSeq))

		print(line + ", protein translation")
		started = 1
		print("started: " + str(started))
	else:
		line = line.strip()
		currentNucleotideSeq += line
	
		

fastaFile.close()