#!/usr/bin/python

class GeneIdWebPage:
	"""
	Class that represents a SNP webpage for a gene ID
	"""

	# geneIdWebPageUrl = ""

	def __init__(self, geneId):
		self.geneId = str(geneId)
		self.geneIdWebPageUrl = "http://www.ncbi.nlm.nih.gov/SNP/snp_ref.cgi?locusId=" + geneId



# class mRnaWebPage: