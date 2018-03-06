filewewant=${1}
output=${2}


#hardcoded to filter out 50 percent plus missingness, but easily modified for other scenarios. 

vcftools --vcf ${filewewant} --missing-indv

mawk '!/IN/' out.imiss | cut -f5 > totalmissing
gnuplot << \EOF 
set terminal dumb size 120, 30
set autoscale 
unset label
set title "Histogram of % missing data per individual"
set ylabel "Number of Occurrences"
set xlabel "% of missing data"
#set yr [0:100000]
binwidth=0.01
bin(x,width)=width*floor(x/width) + binwidth/2.0
plot 'totalmissing' using (bin($1,binwidth)):(1.0) smooth freq with boxes
pause -1
EOF


mawk '$5 > 0.40' out.imiss | cut -f1 > lowDP.indv
vcftools --vcf ${filewewant} --remove lowDP.indv --recode --recode-INFO-all --out ${output}


rm -rf out.imiss
rm -rf lowDP.indv
rm -rf out.log
rm -rf totalmissing

