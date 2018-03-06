from Bio import SeqIO
import csv
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--genebank', help="GBK file for use")
parser.add_argument('--output', help="output file")


args = parser.parse_args()


newfile = open(args.output,'w')



for record in SeqIO.parse(args.genebank, "genbank"):
    for f in record.features:
        if f.type == "gene":
        	print f.qualifiers
        	newfile.write('{}\n'.format(f.qualifiers['locus_tag'][0]))

newfile.close()



