import os
import csv
import sys
import argparse
import operator 

parser = argparse.ArgumentParser()
parser.add_argument('--csvfile', help="CSV file")
parser.add_argument('--peaks', help="peakfiles")

args = parser.parse_args()

num2chrom = {}

num2chromdata = list(csv.reader(open('/newhome/vdp5/projects/vivax_cambodia/data/txt_files/extradata/numchrom_to_pvp01.txt'),delimiter='\t'))



for sica in num2chromdata:
	num2chrom[int(sica[1])] = sica[0]

datadict = []
totalsetsorted = {}
masterset = []

datadict =  list(csv.reader(open(args.csvfile),delimiter=','))[1:]


tempstorage = []
dat = datadict
for beta in dat:
	tmp = beta
	tmp[-1] = float(tmp[-1])
	tempstorage.append(tmp)
tempstorage = sorted(tempstorage, key=operator.itemgetter(3), reverse=True)
newset = tempstorage[:100]
masterdct = newset

peakfile = list(csv.reader(open(args.peaks),delimiter='\t'))
newlst = []


for beta in peakfile:
	newlst.append([beta[0], int(beta[3]), int(beta[1]), int(beta[2])])

for theta in masterdct:
	for tanda in newlst:
		chrom = num2chrom[int(theta[2])]
		ind = int(theta[1])
		if tanda[0] == chrom:
			if ind > tanda[-2] and ind < tanda[-1]:
				print ind, tanda[1]

