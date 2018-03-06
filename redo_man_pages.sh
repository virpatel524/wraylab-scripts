tar -zxvf $1
nombre=$(basename $1)
filename="${nombre%.*}"
filename="${filename%.*}"
IFS='_' read -ra newnam <<< $filename
suche="IRanges-master"
cd $suche/man

for zeta in ./*.Rd; do
	grep "\name{" $zeta > ${zeta}_tmp
	echo "\\title{tmp}" >> ${zeta}_tmp
	cat ${zeta}_tmp
	mv ${zeta}_tmp $zeta
done
cd ../..
tar -czvf $1 $suche
