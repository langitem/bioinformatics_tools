#!/usr/bin/python
# Author: Emanuel Langit
"""
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp)
in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several
 possible consensus strings exist, then you may return any one of them.)

Sample Dataset

>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT


Sample Output

ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6

"""

import sys
import numpy as np

inputFile = sys.argv[1]

fastaFile = open(inputFile)
sequenceEntryNumber = 0
currentSeqEntry = ""
sequenceLength = 0

# create numpy 2d array without specifying its size:


for line in fastaFile:
	line = line.rstrip('\n')
	line = line.upper()

	# if the line starts with '>' skip it and go to the next line
	if line.startswith('>'):
		sequenceEntryNumber +=1

		# skip this line and go to the next if this is the first sequence entry:
		if sequenceEntryNumber == 1:
			continue
		else:
			# convert the last sequence entry into a list
			currentSeqList = list(currentSeqEntry)

			# add the list as a row to the matrix if it already exists, otherwise
			# create the matrix
			# NOTE: if the matrix is empty, then vstack cannot be used
			if sequenceEntryNumber == 2:
				sequenceLength = len(currentSeqEntry)
				sequenceMatrix = [currentSeqList]
			else:
				if len(currentSeqEntry) != sequenceLength:
					print("Length of sequences are not equal!")
					sys.exit(0)

				sequenceMatrix = np.vstack([sequenceMatrix, currentSeqList])


			# reset the current sequence entry
			currentSeqEntry = ""

			
	else:
		# remove all whitespace characters from the line:
		line = ''.join(line.split())

		# append the line to currentSeqEntry
		currentSeqEntry += line

fastaFile.close()

# File is finished being read, still need to process the last sequence entry:
currentSeqList = list(currentSeqEntry)
sequenceMatrix = np.vstack([sequenceMatrix, currentSeqList])


# Now traverse the matrix and record the number of each nucleotide for each horizontal position
# Traversing through each column

numColumns = sequenceLength
numRows = sequenceEntryNumber

aList = ([0] * numColumns)
cList = ([0] * numColumns)
gList = ([0] * numColumns)
tList = ([0] * numColumns)
consensusList = [None] * numColumns
#print(consensusList)

for j in range(numColumns):

	numAs, numCs, numGs, numTs = (0,)*4

	for i in range(numRows):

		if sequenceMatrix[i][j] == 'A':
			aList[j] += 1
			numAs += 1
		elif sequenceMatrix[i][j] == 'C':
			cList[j] += 1
			numCs += 1
		elif sequenceMatrix[i][j] == 'G':
			gList[j] += 1
			numGs += 1
		elif sequenceMatrix[i][j] == 'T':
			tList[j] += 1
			numTs += 1

	# Determine consensus nucleotide for this column:
	# print(str(numAs) + " " + str(numCs) + " " + str(numGs) + " " + str(numTs))
	countDictionary = {'A': numAs, 'C': numCs, 'G': numGs, 'T': numTs}
	consensusNucleotide = 'A'
	highestNum = 0
	nucleotideNumList = [numAs, numCs, numGs, numTs]
	# Iterate through the dictionary:
	for nucleotide, num in countDictionary.iteritems():
		if highestNum < num:
			highestNum = num
			consensusNucleotide = nucleotide

	consensusList[j] = consensusNucleotide


#print the consensus sequence:
print(''.join(str(x) for x in consensusList))

# print the matrix:
print("A: " + ' '.join(str(x) for x in aList))
print("C: " + ' '.join(str(x) for x in cList))
print("G: " + ' '.join(str(x) for x in gList))
print("T: " + ' '.join(str(x) for x in tList))
#print(consensusList)


