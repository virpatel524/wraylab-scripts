import os 
import sys
import csv
from shutil import copyfile

inputfile = list(csv.reader(open('/newhome/vdp5/projects/vivax_cambodia/data/other/vcf_coordiantes_11.23.17.txt'),delimiter='\t'))
dictoldnew = {}

for alpha in inputfile:
	dictoldnew[alpha[-1]] = alpha[0]





for subdir, dirs, files in os.walk('/nfs/wraycompute/vir/variant_storage/bychrom/outputselscan/'):
    for file in files:
        fle = os.path.join(subdir, file)
        if '.out' in fle:
        	num = fle.split('/')[-1].split('.')[0].split('chrom')[-1]
        	newflename = fle.replace(num, dictoldnew[num])
        	copyfile(fle, newflename)
        	os.remove(fle) 





