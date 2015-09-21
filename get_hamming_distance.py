#!/usr/bin/python
# Emanuel Langit
"""
Given: Two DNA strings s and t of equal length (not exceeding 1 kbp) in FASTA file format
Return: The Hamming distance dH(s,t).
"""

import sys
import re

filename = sys.argv[1]
fastaFile = open(filename)

sequenceRecordNumber = 0
nucleotideSeq1 = ""
nucleotideSeq2 = ""
seqId1 = ""
seqId2 = ""

count = 0

for line in fastaFile:
	line = line.rstrip('\n')

	# if the line does not contain an alphanumeric character, skip it and go to
	# the next line:
	if not(re.search('[a-zA-Z0-9]', line)):
		continue

	# if current line is the defline:
	if line.startswith('>'):
		count += 1
		line = line.replace('>', '', 1)
		deflineArray = line.split()
		#print(deflineArray[0])

		if count == 1:
			seqId1 = deflineArray[0]
		elif count == 2:
			seqId2 = deflineArray[0]
		else:
			print("File contains more than 2 sequence entries! " + str(count))
			sys.exit()

	else:
		if count == 1:
			nucleotideSeq1 += line
		elif count ==2:
			nucleotideSeq2 += line
	
fastaFile.close()

# Check if sequences are the same length:
len1 = len(nucleotideSeq1)
len2 = len(nucleotideSeq2)

if len(nucleotideSeq1) != len(nucleotideSeq2):
	print("Sequences are not equal in length! " + str(len1) + " " + str(len2))
	sys.exit()

# convert nucleotide sequences to lists:
list1 = list(nucleotideSeq1)
list2 = list(nucleotideSeq2)

# compare sequences by iterating through lists:
i = 0
distance = 0
for nucleotide in list1:
	if nucleotide != list2[i]:
		distance += 1

	i += 1

print(str(distance))