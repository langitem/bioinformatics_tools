#!/usr/bin/python
"""
Script to convert a tab-delimitted file into a fasta file.
The first field is the defline, and the second field is the sequence

Author: Emanuel Langit
email: emanuel.langit@fastmail.fm
"""
import sys

filename = sys.argv[1]

tblFile = open(filename)

for line in tblFile:
	revisedLine1 = line.rstrip("\n")
	revisedLine2 = revisedLine1.replace("\t", "\n")
	print(">" + revisedLine2) 

tblFile.close()
