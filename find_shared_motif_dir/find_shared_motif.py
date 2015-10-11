#!/usr/bin/python
"""
Author: Emanuel Langit

Given: A collection of k (k<=100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

Sample Dataset
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA

Sample Output
AC
"""

import sys

inputFile = sys.argv[1]

fastaFile = open(inputFile)
currentSeqEntry = ""
startedReading = False
sequenceList = [] # List data structure that will hold invidual sequence entries

for line in fastaFile:
	line = line.rstrip('\n')

	# if line starts with a '>' skip it and start a new sequence record
	if line.startswith('>'):
		# If this is not the first defline:
		if (startedReading):
			sequenceList.append(currentSeqEntry)

		currentSeqEntry = ""
		startedReading = True

		continue
	else:
		# make all nucleotides upper case:
		line = line.upper()


		# remove any whitespaces:
		line = line.replace(" ", "")

		# append line to current sequence record
		currentSeqEntry += line

fastaFile.close()

# append last sequence entry to the list:
sequenceList.append(currentSeqEntry)

# Determine which sequence entry is the shortest:
started = False
shortestSequenceLength = 0
shortestSeq = ""
for currentSeq in sequenceList:
	currentSeqLength = len(currentSeq)
	if (currentSeqLength < shortestSequenceLength) or (started == False):
		shortestSequenceLength = currentSeqLength
		shortestSeq = currentSeq

	started = True


# Create a list of all possible contiguous sequences of the shortest sequence entry
# from largest to smallest using a sliding window algorithm:
possibleSeqs = []
for currentSeqLen in range(shortestSequenceLength, 0, -1):
	tmpList = [shortestSeq[i:i+currentSeqLen] for i in xrange(len(shortestSeq)-(currentSeqLen - 1))]
	possibleSeqs = possibleSeqs + tmpList


# Iterate over the list of possible sequences and check for occurrence in all of the other
# sequence entries
for motif in possibleSeqs:
	score = 0
	#print(sequenceList)
	for sequenceEntry in sequenceList:
		#print(motif + " " + sequenceEntry)
		if motif in sequenceEntry:
			#print(motif + " " + sequenceEntry)
			score +=1


	if score == len(sequenceList):
		print(motif)
		sys.exit(0)

