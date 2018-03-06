import gzip
import csv
import argparse
import sys

parser = argparse.ArgumentParser(description="script to convert an all sites vcf to FASTA format. FASTA description will be the sample name in the VCF header.Only does one chromosome/region at a time.")
parser.add_argument("-v", "--vcf", action="store", required=True, help="Input VCF file. Should be a multisample vcf, though it should theoretically work with a single sample.")
parser.add_argument("-o", "--out", action="store", required=True, help="Output filename")
parser.add_argument("-c", "--chromosome", action="store", required=True, help="Chromosome to output. Should be something in the first column of the vcf.")
parser.add_argument("-g", "--gzip", action="store_true", required=False, help="Set if the VCF is gzipped.")

args = parser.parse_args()

vcf_in = args.vcf
out_name = args.out
out_chr = args.chromosome

sample_names = []
sample_seqs = []

if args.gzip:
    opener = gzip.open
else:
    opener = open

with opener(vcf_in, 'r') as tsvin:
    tsvin = csv.reader(tsvin, delimiter='\t')

    for row in tsvin:
        if any('##' in strings for strings in row):
            continue
        if any('#CHROM' in strings for strings in row):
            sample_names = row[9:]
            for sample in sample_names:
                sample_seqs.append([""])
            continue

        chrom,pos,id,ref,alt,qual,filter,info,format=row[0:9]
        haplotypes = row[9:]

        if chrom == out_chr:
            alt_list = alt.split(",")
            for index,haplotype in enumerate(haplotypes):
#                if haplotype == '0|0':
                if haplotype.split(":")[0] == '0':
                    base = ref
#                elif haplotype == ".|.":
                elif haplotype.split(":")[0] == ".":
                    base = "N"
                else:
                    call = haplotype.split(":")[0]
                    print call
                    base = alt_list[int(call)-1]
                sample_seqs[index][0] = sample_seqs[index][0]+base
        else:
            continue

fasta_out = open(out_name, 'w')
for i in range(len(sample_seqs)):
    fasta_out.write(">"+str(sample_names[i])+"\n"+sample_seqs[i][0]+"\n")
fasta_out.close()