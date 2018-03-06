import csv
fle = open('/Users/virpatel/Desktop/PVT01.fasta','r')
data = list(csv.reader(fle,delimiter='\t'))


newlst = {}
chromid = ''

for alpha in data:
	if alpha == []: continue
	if alpha[0][0] == '>':
		chromid = alpha[0].split(' ')[0].split('.')[0]
		newlst[chromid] = []
	else:
		newlst.setdefault(chromid,[]).append(alpha[0])

fle.close()


fle = open('/Users/virpatel/Desktop/PVT01.fasta','w')

for alpha in newlst:
	fle.write('{}\n'.format(alpha))
	fle.write('{}\n'.format(''.join(newlst[alpha])))

fle.close()