#!/rhome/langitem/bin/Python-2.7.10/python
"""
Script that takes a FASTA file containing DNA
and converts it to RNA

Author: Emanuel Langit
email: emanuel.langit@fastmail.fm
"""

import sys
import re

filename = sys.argv[1]

fastaFile = open(filename)

for line in fastaFile:
	line = line.rstrip('\n')
	if not(re.search('[a-zA-Z0-9]', line)):
		continue

	if line.startswith('>'):
		print(line + ", RNA")
	else:
		line = line.replace("T", "U")
		line = line.replace("t", "u")
		print(line)

