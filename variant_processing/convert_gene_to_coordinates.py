import os 
from Bio import SeqIO
import sys
import csv
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--vcffile', help="VCF file for use to break things down")
parser.add_argument('--genename', help="gene name to extract")
parser.add_argument('--outputdir', help="directory in which to output new vcf")

args = parser.parse_args() 


genbank_file = "/newhome/vdp5/data/reference_genomes/PVP01.gbk" 
for record in SeqIO.parse(genbank_file, "genbank"):
	for f in record.features:
		if f.type == "gene" and "locus_tag" in f.qualifiers:
			locus_tag = f.qualifiers["locus_tag"][0]
			if locus_tag  == args.genename:
				chrom =  record.name
				start = int(f.location.start)
				end = int(f.location.end)
				if start < 10000:
					start = 1
					end = end + 10000
				else:
					start = start - 10000
					end  = end + 10000
				newstr = 'java -jar /newhome/vdp5/source_code/GenomeAnalysisTK.jar -T SelectVariants -V {} -R $PVP01REF -o {}/{}_10000upandback.vcf -L {}'.format(args.vcffile, args.outputdir, args.genename, '{}:{}-{}'.format(chrom, start,end))
				process = subprocess.Popen([newstr,], stdout=subprocess.PIPE,shell=True)
				process.wait()