#!/usr/bin/python
"""
Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
		in FASTA format
Return: The protein string encoded by s.
"""

import sys
import re

# function to translate RNA sequence into protein:
def translateRnaSeq2protein(nucSeqString):
	# print(nucSeq) # remove this later
	
	aminoAcidCode = { 'UUU': 'F', 'UCU': 'S', 'UAU': 'Y', 'UGU': 'C',
             'UUC': 'F', 'UCC': 'S', 'UAC': 'Y', 'UGC': 'C',
             'UUA': 'L', 'UCA': 'S', 'UAA': '*', 'UGA': '*',
             'UUG': 'L', 'UCG': 'S', 'UAG': '*', 'UGG': 'W',
             'CUU': 'L', 'CCU': 'P', 'CAU': 'H', 'CGU': 'R',
             'CUC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R',
             'CUA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R',
             'CUG': 'L', 'CCG': 'P', 'CAG': 'Q', 'CGG': 'R',
             'AUU': 'I', 'ACU': 'T', 'AAU': 'N', 'AGU': 'S',
             'AUC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S',
             'AUA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R',
             'AUG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R',
             'GUU': 'V', 'GCU': 'A', 'GAU': 'D', 'GGU': 'G',
             'GUC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G',
             'GUA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G',
             'GUG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G'
        }
	
	proteinSeq = ""
	
	# convert sequence to a list:
	nucleotideList = list(nucSeqString)
	
	# traverse list and translate every 3 nucleotides into an amino acid
	counter = 1
	currentCodon = ""
	for nucleotide in nucleotideList:
		currentCodon  += nucleotide
		if counter < 3:
			counter +=1
		else:
			proteinSeq += aminoAcidCode[currentCodon]
			currentCodon = ""
			counter = 1
			
	return proteinSeq


filename = sys.argv[1]
fastaFile = open(filename)
currentNucleotideSeq = ""

started = 0 # variable to check if first sequence entry read

for line in fastaFile:
	# skip line if it doesn't contain any alphanumeric characters:
	if not(re.search('[a-zA-Z0-9]', line)):
		continue
		
	line = line.rstrip('\n')
	
	# if current line is a defline:
	if line.startswith('>'):
		if started == 1:
			print(translateRnaSeq2protein(currentNucleotideSeq))
			currentNucleotideSeq = ""

		print(line + ", protein translation")
		started = 1
	else:
		line = line.strip() # remove spaces if they exist
		line = line.upper()
		currentNucleotideSeq += line

fastaFile.close()

print(translateRnaSeq2protein(currentNucleotideSeq))


