#!/usr/bin/python
import urllib2
import time

class GeneIdWebPage:
	"""
	Class that represents a SNP webpage for a gene ID
	"""

	# geneIdWebPageUrl = ""



	def __init__(self, geneId):
		self.geneId = str(geneId)
		self.geneIdWebPageUrl = "http://www.ncbi.nlm.nih.gov/SNP/snp_ref.cgi?locusId=" + self.geneId
		self.mRnaDictionaryEntry = {}

	def scrapeWebpageForEachMrna(self): # function that scrapes relevant data for current mRNA
		#print self.geneIdWebPageUrl
		response = urllib2.urlopen(self.geneIdWebPageUrl)
		time.sleep(5)
		data = response.read()
		linesOfHtml = data.split("\n") # each value is an HTML line in the web page for this mRNA

		for line in linesOfHtml: # for each line of HTML in the web page for this mRNA
			if ("currently shown" or "View snp on GeneModel") in line:
				fields = line.split(">")
				for field in fields:
					

		return



def main():
	import sys

	geneListFile = sys.argv[1]
	geneList = open(geneListFile)

	for line in geneList:
		line = line.rstrip('\n')
		line = line.replace(" ", "")
		if line.isdigit(): # NCBI gene IDs are numbers only
			geneIdWebPageExample = GeneIdWebPage(line)
			geneIdWebPageExample.scrapeWebpageForEachMrna()
			

	geneList.close()


if __name__ == '__main__':
	main()