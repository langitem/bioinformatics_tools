#!/usr/bin/python
"""
Author: Emanuel Langit
Given a list of URLs (which should have been generated using the
create_mrna_snp_url.py script, this application will print to 
stdout in tab delimited format: mRNA accession, rs ID, and mRNA position)
"""

import sys
import urllib2
import time
import re

urlListFile = sys.argv[1]
urlList = open(urlListFile)

for url in urlList:
	url = url.rstrip("\n")
	response = urllib2.urlopen(url)
	time.sleep(5)
	htmlPage = response.read()
	htmlLines = htmlPage.split("\n")

	#accession = ""
	#mRnaSnpPos = ""
	#rsID = ""

	for line in htmlLines:
		if "currently shown" in line:
			#accession = re.sub(r'^.*?nuccore/', '', line)
			#accession = re.sub(r'\".*$', '', accession)
			accession = re.sub(r'^.*?bgcolor=\"yellow', '', line)
			accession = re.sub(r'^.*?nuccore/', '', accession)
			accession = re.sub(r'\".*$', '', accession)
		

		# if the line contains an RS ID:
		#	assign the number in the mRNA column
		if "snp_ref.cgi?rs=" in line:
			mRnaSnpPos = re.sub(r'^.*currpage=1\">', '', line)
			mRnaSnpPos = re.sub(r'<.*', '', mRnaSnpPos)
			mRnaSnpPos = int(mRnaSnpPos)
			mRnaSnpPos -=1
			rsID = re.sub(r'^.*snp_ref.cgi\?rs=', 'rs', line)
			rsID = re.sub(r'\".*$', '', rsID)

			# print(accession + "\t" + str(mRnaSnpPos) + "\t" + rsID)

		
		# if the line contains "contig reference":
		#	print accession, mRnaSnpPos, and the length of the string
		#	in the dbSNP allele column
		if "contig reference" in line:
			referenceAllele = re.sub(r'^.*contig reference<\/td>', '', line)
			referenceAllele = re.sub(r'^.*?>', '', referenceAllele)
			referenceAllele = re.sub(r'<.*$', '', referenceAllele)

			if "bp)" in referenceAllele:
				referenceAlleleLength = re.sub(r'\(', '', referenceAllele)
				referenceAlleleLength = re.sub(r'bp\)', '', referenceAlleleLength)
			else:
				referenceAlleleLength = len(referenceAllele)
				referenceAlleleLength = str(referenceAlleleLength)

			print(accession + "\t" + str(mRnaSnpPos) + "\t" + referenceAlleleLength + "\t" + rsID)
			


urlList.close()