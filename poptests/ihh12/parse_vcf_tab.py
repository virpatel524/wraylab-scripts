import os
import subprocess
import argparse
import csv
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--tabfile', help="VCF file for use")
parser.add_argument('--pop', help="VCF file for use")
args = parser.parse_args()


datasrc = os.path.join('/home/vdp5/projects/vivax_cambodia/data/poptests/ihh12', args.pop)