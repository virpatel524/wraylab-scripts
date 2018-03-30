import argparse
import csv
import os
import sys


data = list(csv.reader(open('/newhome/vdp5/projects/vivax_cambodia/data/poptests/fst/MT-CV_hudsonfst_topset.txt'),delimiter='_'))
newfle = open('/newhome/vdp5/projects/vivax_cambodia/data/poptests/fst/MT-CV_hudsonfst_loci.list', 'w')



for item in data:
	newfle.write('{}:{}-{}\n'.format(item[0], item[1], item[1]))

newfle.close()
