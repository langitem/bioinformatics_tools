#!/usr/bin/python
"""
Author: Emanuel Langit


"""

import argparse
parser = argparse.ArgumentParser(description='Program to create SNP bed file ')
parser.add_argument('inputFile', metavar='arg1', help = 'file downloaded from UCSC with SNP information', type=argparse.FileType('r'))
parser.add_argument('MAF', metavar='arg2', help='minimum MAF', type=float)
args = parser.parse_args()

#print args.inputFile.readlines()

#print(args.inputFile.read())

for line in args.inputFile:
	line = line.rstrip("\n")
	lineList = line.split("\t")
	lineListSize = len(lineList)
	print lineListSize
	#print line


args.inputFile.close()


def get_maf(myList):
	listSize = len(myList)

	# Use loop and start at last element of the list.
	# If the element is has no value (""), then keep going back until
	# it does have value. This is done because the file from UCSC has empty
	# elements in its tab-delimitted file.

	return