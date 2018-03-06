import os 
import sys
import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument('-dir')
args = vars(parser.parse_args())


fulldict = {}

for beta in os.listdir(args['dir']):
	dat = list(csv.reader(open(os.path.join(args['dir'], beta)),delimiter='\t'))
	fulldict[beta.split('_')[0]] = dat


fullfle = open('../../data/test_coverage.txt','w')

fullfle.write('Chr\tStart\tStop\t')

nombres = sorted(fulldict.keys())


fullfle.write('\t'.join(nombres) + '\n')

newlst = []

chromo = ''
start = ''
end = ''


for zeta in nombres:
	zipper = zip(*fulldict[zeta])
	newlst.append(zipper[3])
	chromo = zipper[0]
	start = zipper[1]
	end = zipper[2]


newlst = zip(*newlst)

for i in range(0, len(chromo)):
	fullfle.write('{}\t{}\t{}\t{}\n'.format(chromo[i], start[i], end[i], '\t'.join(newlst[i])))







# for alpha in nombres:
# 	for beta in fulldict[alpha]:
# 		print beta

fullfle.close()