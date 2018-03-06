fle=${1}
plink --vcf ${1}.vcf --out ${1} --double-id --allow-extra-chr   
plink --allow-extra-chr --bfile ${fle} --indep-pairwise 50 10 0.1
mv plink.prune.in ${fle}.plink.prune.in
plink  --allow-extra-chr --bfile ${fle} --extract ${fle}.plink.prune.in --make-bed --out ${fle}.prunedData

for K in 1 2 3 4 5;

do admixture --haploid="*" --cv ${fle}.prunedData.bed $K | tee ${fle}.log${K}.out; done