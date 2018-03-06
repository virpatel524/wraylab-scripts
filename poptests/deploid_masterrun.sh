while read p; do
  	cd /newhome/vdp5/source_code/DEploid/utilities/
  	Rscript /newhome/vdp5/source_code/DEploid/utilities/dataExplore.r -vcf /nfs/wraycompute/vir/variant_storage/indiv_samples/${p}_refined.vcf -o /nfs/wraycompute/vir/variant_storage/indiv_samples/outliers/${p}_outliers_ -plaf /home/vdp5/projects/vivax_cambodia/data/poptests/deploid/indiv_plaf/${p}_scenariominor_plaf.txt
  	dEploid -vcf /nfs/wraycompute/vir/variant_storage/indiv_samples/${p}_refined.vcf -o /nfs/wraycompute/vir/variant_storage/indiv_samples/deploidout/${p} -plaf /home/vdp5/projects/vivax_cambodia/data/poptests/deploid/indiv_plaf/${p}_scenariominor_plaf.txt -noPanel  -exclude /nfs/wraycompute/vir/variant_storage/indiv_samples/outliers/${p}_outliers_PotentialOutliers.txt
done < $1