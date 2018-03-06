from Bio import SeqIO

fle = open('/newhome/vdp5/data/reference_genomes/PVP01.gbk', 'r')
output = open('/newhome/vdp5/data/reference_genomes/PVP01.gbk.fasta', 'w')

for seq_record in SeqIO.parse(fle, 'genbank'):

	for seq_feature in seq_record.features:
		if seq_feature.type == 'CDS':
			beta = seq_feature.location.extract(seq_record).seq
			output.write('>{}\n'.format(seq_feature.qualifiers["locus_tag"][0]))
			output.write('{}\n'.format(beta))

output.close()
fle.close()