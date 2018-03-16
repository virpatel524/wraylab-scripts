import os
import sys
import csv
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--dir', help="Directory for play")
parser.add_argument('--lk', help="lk files")

args = parser.parse_args()



for alpha in os.listdir('{}'.format(args.dir)):
	if 'headeredited' in alpha:
		splitter = os.path.join(args.dir, '.'.join(alpha.split('.')[:-4]) + '.')
		print splitter
		newstr = 'convert -seq {} -prefix {}'.format(os.path.join('{}'.format(args.dir),alpha), splitter)
		# print newstr
		process = subprocess.Popen([newstr,], stdout=subprocess.PIPE,shell=True)
		process.wait()

		newstr = 'interval -seq {} -loc {} -prefix {} -its 100000 -bpen 5 -samp 2000 -lk {}'.format(splitter + 'sites.txt', splitter + 'locs.txt', splitter, args.lk)
		process = subprocess.Popen([newstr,], stdout=subprocess.PIPE,shell=True)