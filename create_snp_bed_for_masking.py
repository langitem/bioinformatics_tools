#!/usr/bin/python
"""
Author: Emanuel Langit


"""

import argparse

# --- Start Functions ---#

def get_maf(myList):
	listSize = len(myList)

	# Use loop and start at last element of the list.
	# If the element is has no value (""), then keep going back until
	# it does have value. This is done because the file from UCSC has empty
	# elements in its tab-delimitted file.

	listLength = len(myList)
	maf = ""

	#if myList[listLength-1] == "":
	#	print 'empty'
	
	while maf == "":
		maf = myList[listLength-1]
		if maf == "":
			listLength = listLength-1


	
	
	return maf

# --- End Functions ---#

parser = argparse.ArgumentParser(description='Program to create SNP bed file ')
parser.add_argument('inputFile', metavar='arg1', help = 'file downloaded from UCSC with SNP information', type=argparse.FileType('r'))
parser.add_argument('MAF', metavar='arg2', help='minimum MAF', type=float)
args = parser.parse_args()

#print args.inputFile.readlines()

#print(args.inputFile.read())

for line in args.inputFile:
	line = line.rstrip("\n")
	lineList = line.split("\t")

	maf = get_maf(lineList)

	print "%s\t%s\t%s\t%s" % (lineList[1], lineList[2], lineList[3], maf)



args.inputFile.close()


