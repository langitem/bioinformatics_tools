#!/usr/bin/python
"""
Given: Two DNA strings s and t (each of length at most 1 kbp).
Return: All locations of t as a substring of s.

Sample Dataset
GATATATGCATATACTT
ATAT
Sample Output
2 4 10
"""
import re
import sys

filename = sys.argv[1]
inputFile = open(filename)

string = ""
substring = ""

lineNumber = 1
for line in inputFile:
	line = line.rstrip('\n')
	line = line.upper()

	if lineNumber == 1:
		string = line
	else:
		substring = line

	lineNumber += 1

positionsList = [] # will hold list of start positions of substring

for match in re.finditer(substring, string):
	positionsList.append(match.start() + 1) # add 1 to make 1-based
	print(str(match.start() + 1))
