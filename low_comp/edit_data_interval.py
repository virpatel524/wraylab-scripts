import csv


data = list(csv.reader(open('../../data/low_comp/pvp01.dustmasker.interval'),delimiter='\t'))

newlst = []



curr_chrom = ''


for alpha in data:
	if alpha[0][0] == '>':
		curr_chrom = alpha[0].split('|')[-1][:-1]
		continue
	else:
		tmp  = alpha[0].split(' ')
		print tmp
		zeta = '{}:{}-{}'.format(curr_chrom, tmp[0], tmp[-1])
		print zeta

newfle = open('../../data/low_comp/pvp01.dustmasker.interval.list', 'w')

for alpha in newlst:
	newfle.write(alpha + '\n')

newfle.close()

