import os 
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--ibdfile', help="VCF file for use")
args = parser.parse_args()
file = args.ibdfile



data = list(csv.reader(open(file),delimiter='\t'))
name = file.split('/')[-1].split('.')[0]


twowaydict = {}

for alpha in data[1:]:
	twowaydict.setdefault(alpha[0], []).append([float(alpha[-1]), alpha[1]])
	twowaydict.setdefault(alpha[1], []).append([float(alpha[-1]), alpha[0]])


newfle = open('/nfs/wraycompute/vir/hmmidb_output/{}_selecteds.txt'.format(name),'w')

for alpha in twowaydict:
	tmpfle = open('/nfs/wraycompute/vir/hmmidb_output/basedonhmmidb_samplelistgatk/{}.list'.format(alpha),'w')
	tmp = twowaydict[alpha][:10]
	tmp = sorted(tmp, key=lambda x: x[0], reverse=True)
	whoiwant = [a[-1] for a in tmp]
	lasts = [alpha,] + whoiwant
	newfle.write('\t'.join(lasts) + '\n')

	tmpfle.write('{}\n'.format(alpha))
	for beta in tmp:
		tmpfle.write(beta[-1] + '\n')
	tmpfle.close()
newfle.close()


