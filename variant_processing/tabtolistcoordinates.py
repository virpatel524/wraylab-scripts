import os
import csv
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--tabinput', help="Tab file input")
parser.add_argument('--output_location', help='Where should we throw out coords')
args = parser.parse_args()


data = list(csv.reader(open(args.tabinput),delimiter='\t'))

coords = []


for alpha in data[1:]:
    coords.append('{}:{}-{}'.format(alpha[0], alpha[1], alpha[1]))

offset = open(args.output_location, 'w')

for alpha in coords:
    offset.write(alpha + '\n')

offset.close()

