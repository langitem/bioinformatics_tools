#!/usr/bin/python
"""
Author: Emanuel Langit

Given a list of NCBI gene IDs, this application will perform a web
scrape of NCBI's dbSNP pages. URLs will then be created for each of the mRNAs
belonging to that gene, which will be used to retrieve SNP information for
each mRNA.

Example:
For the gene ID: 9575, the URL http://www.ncbi.nlm.nih.gov/SNP/snp_ref.cgi?locusId=9575
will be scraped. The mRNAs listed on that page will then be used to create the URLs:
http://www.ncbi.nlm.nih.gov/SNP/snp_ref.cgi?geneId=9575&ctg=NT_022853.16&mrna=XM_011534411.1&prot=XP_011532713.1&orien=reverse
http://www.ncbi.nlm.nih.gov/SNP/snp_ref.cgi?geneId=9575&ctg=NT_022853.16&mrna=XM_011534410.1&prot=XP_011532712.1&orien=reverse

etc.
"""

import sys
import urllib2

geneListFile = sys.argv[1]
geneList = open(geneListFile)

baseUrl = 'http://www.ncbi.nlm.nih.gov/SNP/snp_ref.cgi?locusId='

for line in geneList:
	line = line.rstrip('\n')
	line = line.replace(" ", "")
	url = baseUrl + line

geneList.close()