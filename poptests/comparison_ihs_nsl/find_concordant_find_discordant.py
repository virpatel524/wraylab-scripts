import os
import sys
import csv
import argparse
import subprocess


parser = argparse.ArgumentParser()
parser.add_argument('--pop', help="populationname")
args = parser.parse_args()



ihspath = os.path.join('/newhome/vdp5/projects/vivax_cambodia/data/poptests/ihs/', args.pop, 'master.100bin.txt')