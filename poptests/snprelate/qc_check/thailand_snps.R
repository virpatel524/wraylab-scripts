library('SNPRelate')
genofile <- snpgdsOpen('/nfs/wraycompute/vir/variant_storage/countrylevel/5iter_allvariants_filtered.rareremove.deploidcorrected.notrelevantremoved.chromcorrected.THAILAND.ann.gds')

pop_code <- unlist(read.table('/newhome/vdp5/projects/vivax_cambodia/data/txt_files/lists_gatk/thailand_only_#VCF1.experimentorigins.txt'))

set.seed(1000)
snpset <- snpgdsLDpruning(genofile, ld.threshold=0.5)
snpset.id <- unlist(snpset)

sample.id <- read.gdsn(index.gdsn(genofile, "sample.id"))
pca <- snpgdsPCA(genofile, snp.id=snpset.id, num.thread=2)


tab <- data.frame(sample.id = pca$sample.id,
    pop = factor(pop_code)[match(pca$sample.id, sample.id)],
    EV1 = pca$eigenvect[,1],    # the first eigenvector
    EV3 = pca$eigenvect[,3],    # the third eigenvector
    stringsAsFactors = FALSE)
pdf('/home/vdp5/projects/vivax_cambodia/data/figures/population_figures/pca_eg1_eg3_#VCF1_ld0.5.thailand.pdf')
plot(tab$EV3, tab$EV1, col=as.integer(tab$pop), xlab="eigenvector 3", ylab="eigenvector 1")
legend("bottomright", legend=levels(tab$pop), pch="o", col=1:nlevels(tab$pop))
dev.off()



tab <- data.frame(sample.id = pca$sample.id,
    pop = factor(pop_code)[match(pca$sample.id, sample.id)],
    EV1 = pca$eigenvect[,1],    # the first eigenvector
    EV2 = pca$eigenvect[,2],    # the third eigenvector
    stringsAsFactors = FALSE)
pdf('/home/vdp5/projects/vivax_cambodia/data/figures/population_figures/pca_eg1_eg2_#VCF1_ld0.5.thailand.pdf')
plot(tab$EV2, tab$EV1, col=as.integer(tab$pop), xlab="eigenvector 2", ylab="eigenvector 1")
legend("bottomright", legend=levels(tab$pop), pch="o", col=1:nlevels(tab$pop))
dev.off()


pop_code <- unlist(read.table('/newhome/vdp5/projects/vivax_cambodia/data/txt_files/lists_gatk/thailand_only_#VCF1.experimentorigins.eth-wth.txt'))
tab <- data.frame(sample.id = pca$sample.id,
    pop = factor(pop_code)[match(pca$sample.id, sample.id)],
    EV1 = pca$eigenvect[,1],    # the first eigenvector
    EV2 = pca$eigenvect[,2],    # the third eigenvector
    stringsAsFactors = FALSE)
pdf('/home/vdp5/projects/vivax_cambodia/data/figures/population_figures/pca_eg1_eg2_#VCF1_ld0.5.thailand.eth-wth.pdf')
plot(tab$EV2, tab$EV1, col=as.integer(tab$pop), xlab="eigenvector 2", ylab="eigenvector 1")
legend("bottomright", legend=levels(tab$pop), pch="o", col=1:nlevels(tab$pop))
dev.off()