#!/usr/bin/python
"""
Author: Emanuel Langit
Description: This program takes as input a tab-delimited file downloaded from UCSC
that contains SNP information (i.e., chromosomal positions, allele frequencies)
and a minimum minor allele frequency. A bed file is then printed to STDOUT of the
chromosome, start, stop, and frequencies.
"""

import argparse
import re

# --- Start Functions ---#

def accept_or_reject(myList, mafCutOff):

	# allele frequencies are in the second to the last column:
	listSize = len(myList)
	freqColumn = myList[listSize - 2]
	freqColumn = freqColumn.rstrip(",")
	freqColumnList = freqColumn.split(',')

	largestFreq = 0
	for frequency in freqColumnList:

		# if frequency isn't numeric, exit the loop:
		if (re.search('[a-zA-Z]', frequency)) or frequency == "":
			largestFreq = 0;
			break
		else:
			frequency = float(frequency)

		if frequency > largestFreq:
			largestFreq = frequency

	answer = ""

	if largestFreq == 0:
		answer = "reject"
	else:
		currentMaf = 1 - largestFreq
		if currentMaf >= mafCutOff:
			answer = "accept"
		else:
			answer = "reject"

	return answer

# --- End Functions ---#

parser = argparse.ArgumentParser(description='Program to create SNP bed file based on given minor allele frequency')
parser.add_argument('inputFile', metavar='arg1', help = 'file downloaded from UCSC with SNP information', type=argparse.FileType('r'))
parser.add_argument('MAF', metavar='arg2', help='minimum MAF', type=float)
args = parser.parse_args()


for line in args.inputFile:
	line = line.rstrip("\n")
	lineList = line.split("\t")

	freqColIndex = len(lineList) - 2

	maf = accept_or_reject(lineList, args.MAF)

	if accept_or_reject(lineList, args.MAF) == "accept":
		print "%s\t%s\t%s\t%s\t%s" % (lineList[1], lineList[2], lineList[3], lineList[4], lineList[freqColIndex].rstrip(","))


args.inputFile.close()