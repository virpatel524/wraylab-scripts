file1=$(readlink -f $1)
file2=$(readlink -f $2)

nombre=$(basename $file1)
IFS='_' read -ra ADDR <<< $nombre
putout=$(dirname $file1)

pairfq addinfo -i $file1 -p 1 -o $putout/${ADDR[0]}_R1.fastq
pairfq addinfo -i $file2 -p 2 -o $putout/${ADDR[0]}_R2.fastq

gzip $putout/${ADDR[0]}_R1.fastq
gzip $putout/${ADDR[0]}_R2.fastq

