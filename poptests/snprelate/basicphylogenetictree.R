library('SNPRelate')
library('gdsfmt')
genofile <- snpgdsOpen('/nfs/wraycompute/vir/variant_storage/5iter_allvariants_filtered.heteroremove.rareremove.deploidcorrected.vcf.gds')
# (genofile <- snpgdsOpen(snpgdsExampleFileName()))
print(genofile)

test <- get.attr.gdsn(index.gdsn(genofile, "snp.annot"))
print(typeof(test))



