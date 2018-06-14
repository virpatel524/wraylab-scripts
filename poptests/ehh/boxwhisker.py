import os 
import csv
import argparse
import sys
import matplotlib; matplotlib.use('PDF')
import matplotlib.pyplot as plt
import seaborn as sns
import scipy


parser = argparse.ArgumentParser()
parser.add_argument('--dir1', help="where interval file stored")
parser.add_argument('--dir2', help="where other interval file stored")
parser.add_argument('--dir1name', help="name for graph for dir1")
parser.add_argument('--dir2name', help="name for graph for dir2")
args = parser.parse_args()


interval1 = list(csv.reader(open(os.path.join(args.dir1, 'intervals.txt')),delimiter='\t'))
interval2 = list(csv.reader(open(os.path.join(args.dir2, 'intervals.txt')),delimiter='\t'))



set1 = []
set2 = []

for beta in interval1:
	set1.append(float(beta[-1]))


for beta in interval2:
	set2.append(float(beta[-1]))


xval = []
yval = []

for beta in interval1:
	xval.append(float(beta[-1]))
	yval.append('real')

for beta in interval2:
	xval.append(float(beta[-1]))
	yval.append('random')

ax = sns.violinplot(x=xval, y=yval, order=["real", "random"])

plt.savefig('test.pdf')