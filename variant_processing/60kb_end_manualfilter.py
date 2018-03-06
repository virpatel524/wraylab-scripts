import csv

newlst = []
import csv
from Bio import SeqIO
for seq_record in SeqIO.parse("/newhome/vdp5/data/reference_genomes/PVP01.gbk", "genbank"):
	chrom =  seq_record.name
	if len((seq_record)) > 1000000:
		newlst.append('{}:{}-{}'.format(chrom,0,60000))
		newlst.append('{}:{}-{}'.format(chrom, len(seq_record) - 60000, len(seq_record)))

newfle = open('../../data/low_comp/end_telmoere_coord.list', 'w')


for alpha in newlst:
	print alpha
	newfle.write(alpha + '\n')

newfle.close()
