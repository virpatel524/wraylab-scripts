import os
import sys
import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument('--dir', help="Directory with output files")
args = parser.parse_args()


def findvalues(indexer, start, matrix):
	upperbound = 0
	lowerbound = 0
	curind = start
	ehh = float(matrix[start][indexer])
	while ehh > 0.2:
		curind -= 1
		if curind < 0: break
		ehh = float(matrix[curind][indexer])

	lowerbound = curind + 1

	curind = start
	ehh = float(matrix[start][indexer])
	while ehh > 0.2: 
		curind += 1
		if curind == len(matrix): break
		ehh = float(matrix[curind][indexer])

	upperbound = curind - 1

	return upperbound, lowerbound



newfle = open(os.path.join(args.dir, 'intervals.txt'), 'w')


for beta in os.listdir(args.dir):
	if '.out' in beta and 'colormap' not in beta:
		nombre = beta.split('.')[0]
		dataset = list(csv.reader(open(os.path.join(args.dir, beta)),delimiter='\t'))
		for index, alpha in enumerate(dataset):
			if int(alpha[0]) == 0:
				mainind = index
		hap0_upper, hap0_lower = findvalues(2, mainind, dataset)
		hap1_upper, hap1_lower = findvalues(3, mainind, dataset)


		if hap0_upper - hap0_lower > hap1_upper - hap1_lower:
			realrange = int(dataset[hap0_upper][0]) - int(dataset[hap0_lower][0])
			newfle.write('{}\t{}\t{}\t{}\n'.format(nombre, hap0_lower, hap0_upper, realrange))
		else:
			realrange = int(dataset[hap1_upper][0]) - int(dataset[hap1_lower][0])
			newfle.write('{}\t{}\t{}\t{}\n'.format(nombre, hap1_lower, hap1_upper, realrange))


newfle.close()
