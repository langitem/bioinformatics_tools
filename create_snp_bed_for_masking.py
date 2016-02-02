#!/usr/bin/python
"""
Author: Emanuel Langit


"""

import argparse
parser = argparse.ArgumentParser(description='Program to create SNP bed file ')
parser.add_argument('inputFile', metavar='arg1', help = 'file downloaded from UCSC with SNP information', type=argparse.FileType('r'))
parser.add_argument('MAF', metavar='arg2', help='minimum MAF', type=float)
args = parser.parse_args()



