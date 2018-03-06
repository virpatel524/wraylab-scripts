library('SNPRelate')
genofile <- snpgdsOpen('/nfs/wraycompute/vir/variant_storage/countrylevel/5iter_allvariants_filtered.rareremove.deploidcorrected.notrelevantremoved.chromcorrected.CAMBODIA.ann.gds')

pop_code <- unlist(read.table('/newhome/vdp5/projects/vivax_cambodia/data/txt_files/lists_gatk/cambodia_only_#VCF1.experimentorigins.txt'))

set.seed(1000)
snpset <- snpgdsLDpruning(genofile, ld.threshold=0.5)
snpset.id <- unlist(snpset)

sample.id <- read.gdsn(index.gdsn(genofile, "sample.id"))
pca <- snpgdsPCA(genofile, snp.id=snpset.id, num.thread=2)

pc.percent <- pca$varprop*100
head(round(pc.percent, 2))

tab <- data.frame(sample.id = pca$sample.id,
    pop = factor(pop_code)[match(pca$sample.id, sample.id)],
    EV1 = pca$eigenvect[,1],    # the first eigenvector
    EV3 = pca$eigenvect[,3],    # the third eigenvector
    stringsAsFactors = FALSE)
pdf('/home/vdp5/projects/vivax_cambodia/data/figures/population_figures/pca_eg1_eg3_#VCF1_ld0.5.CAMBODIA.pdf')
plot(tab$EV3, tab$EV1, col=as.integer(tab$pop), xlab="eigenvector 3", ylab="eigenvector 1")
legend("topright", legend=levels(tab$pop), pch="o", col=1:nlevels(tab$pop))
dev.off()
