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
		if '.txt' in alpha: continue
		splitter = os.path.join(args.dir, '.'.join(alpha.split('.')[:-1]) + '.')
		print splitter
		# newstr = 'convert -seq {} -prefix {} -nout 50'.format(os.path.join('{}'.format(args.dir),alpha), splitter)
		# process = subprocess.Popen([newstr,], stdout=subprocess.PIPE,shell=True)
		# process.wait()

		newstr = '/newhome/vdp5/source_code/LDhat/stat -input {}rates.txt -prefix {} -loc {}locs.txt'.format(splitter, splitter, splitter)
		process = subprocess.Popen([newstr,], stdout=subprocess.PIPE,shell=True)
		process.wait()


