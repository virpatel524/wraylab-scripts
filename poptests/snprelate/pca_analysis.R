library('SNPRelate')

genofile <- snpgdsOpen('/newhome/vdp5/projects/vivax_cambodia/data/poptests/admixtrue/5iter_allvariants_filtered.rareremove.deploidcorrected.notrelevantremoved.nopirvirvariants.numcorrected.ann.vcf.gds')
pop_code <- unlist(read.table('/newhome/vdp5/projects/vivax_cambodia/data/other/poplablels-5iter_allvariants_filtered.rareremove.deploidcorrected.notrelevantremoved.chromcorrect.sorted.vcf-txt'))


# Eig1, Eig2 PCA Plot w/o Sampling

set.seed(1000)
snpset <- snpgdsLDpruning(genofile, ld.threshold=0.5)
snpset.id <- unlist(snpset)

sample.id <- read.gdsn(index.gdsn(genofile, "sample.id"))
pca <- snpgdsPCA(genofile, snp.id=snpset.id, num.thread=1)

tab <- data.frame(sample.id = pca$sample.id,
    pop = factor(pop_code)[match(pca$sample.id, sample.id)],
    EV1 = pca$eigenvect[,1],    # the first eigenvector
    EV2 = pca$eigenvect[,2],    # the second eigenvector
    stringsAsFactors = FALSE)
pdf('/home/vdp5/projects/vivax_cambodia/data/figures/population_figures/pca_eg1_eg2_#VCF1_ld0.5.pdf')
plot(tab$EV2, tab$EV1, col=as.integer(tab$pop), xlab="eigenvector 2", ylab="eigenvector 1")
legend("topright", legend=levels(tab$pop), pch="o", col=1:nlevels(tab$pop))
dev.off()

# Eig1, Eig2 PCA Plot w/o Sampling

set.seed(1000)
snpset <- snpgdsLDpruning(genofile, ld.threshold=0.5)
snpset.id <- unlist(snpset)

sample.id <- read.gdsn(index.gdsn(genofile, "sample.id"))
pca <- snpgdsPCA(genofile, snp.id=snpset.id, num.thread=1)

tab <- data.frame(sample.id = pca$sample.id,
    pop = factor(pop_code)[match(pca$sample.id, sample.id)],
    EV1 = pca$eigenvect[,1],    # the first eigenvector
    EV2 = pca$eigenvect[,2],    # the second eigenvector
    stringsAsFactors = FALSE)
pdf('/home/vdp5/projects/vivax_cambodia/data/figures/population_figures/pca_eg1_eg2_eg3#VCF1_ld0.5.pdf')
plot(tab$EV2, tab$EV1, col=as.integer(tab$pop), xlab="eigenvector 2", ylab="eigenvector 1")
legend("bottomright", legend=levels(tab$pop), pch="o", col=1:nlevels(tab$pop))
# dev.off()



#  Eig1, Eig2 PCA Plot w Sampling & Populations


pop_code <- unlist(read.table('/newhome/vdp5/projects/vivax_cambodia/data/other/poplablels-5iter_allvariants_filtered.rareremove.deploidcorrected.notrelevantremoved.chromcorrect.sorted.vcf-hupalopearsonjuliano.txt'))

set.seed(1000)
snpset <- snpgdsLDpruning(genofile, ld.threshold=0.5)
snpset.id <- unlist(snpset)

sample.id <- read.gdsn(index.gdsn(genofile, "sample.id"))
pca <- snpgdsPCA(genofile, snp.id=snpset.id, num.thread=1)

tab <- data.frame(sample.id = pca$sample.id,
    pop = factor(pop_code)[match(pca$sample.id, sample.id)],
    EV1 = pca$eigenvect[,1],    # the first eigenvector
    EV2 = pca$eigenvect[,2],    # the second eigenvector
    stringsAsFactors = FALSE)
pdf('/home/vdp5/projects/vivax_cambodia/data/figures/population_figures/pca_eg1_eg2_experimentpoplabelscombined#VCF1_ld0.5.pdf')
plot(tab$EV2, tab$EV1, col=as.integer(tab$pop), xlab="eigenvector 2", ylab="eigenvector 1")
legend("bottomleft", legend=levels(tab$pop), pch="o", col=1:nlevels(tab$pop))
dev.off()

# Eig1, Eig2 PCA Plot, LD=0.0


set.seed(1000)
snpset <- snpgdsLDpruning(genofile, ld.threshold=0.0)
snpset.id <- unlist(snpset)

sample.id <- read.gdsn(index.gdsn(genofile, "sample.id"))
pca <- snpgdsPCA(genofile, snp.id=snpset.id, num.thread=1)

tab <- data.frame(sample.id = pca$sample.id,
    pop = factor(pop_code)[match(pca$sample.id, sample.id)],
    EV1 = pca$eigenvect[,1],    # the first eigenvector
    EV2 = pca$eigenvect[,2],    # the second eigenvector
    stringsAsFactors = FALSE)
pdf('/home/vdp5/projects/vivax_cambodia/data/figures/population_figures/pca_eg1_eg2_#VCF1_ld0.0.pdf')
plot(tab$EV2, tab$EV1, col=as.integer(tab$pop), xlab="eigenvector 2", ylab="eigenvector 1")
legend("bottomright", legend=levels(tab$pop), pch="o", col=1:nlevels(tab$pop))
dev.off()


# Eig1, Eig2 PCA Plot, LD=1.0


set.seed(1000)
snpset <- snpgdsLDpruning(genofile, ld.threshold=1.0)
snpset.id <- unlist(snpset)

sample.id <- read.gdsn(index.gdsn(genofile, "sample.id"))
pca <- snpgdsPCA(genofile, snp.id=snpset.id, num.thread=1)

tab <- data.frame(sample.id = pca$sample.id,
    pop = factor(pop_code)[match(pca$sample.id, sample.id)],
    EV1 = pca$eigenvect[,1],    # the first eigenvector
    EV2 = pca$eigenvect[,2],    # the second eigenvector
    stringsAsFactors = FALSE)
pdf('/home/vdp5/projects/vivax_cambodia/data/figures/population_figures/pca_eg1_eg2_#VCF1_ld1.0.pdf')
plot(tab$EV2, tab$EV1, col=as.integer(tab$pop), xlab="eigenvector 2", ylab="eigenvector 1")
legend("bottomright", legend=levels(tab$pop), pch="o", col=1:nlevels(tab$pop))
dev.off()


# experiment

pop_code <- unlist(read.table('/newhome/vdp5/projects/vivax_cambodia/data/txt_files/lists_gatk/all_sample_#VCF1_experimentlabel.txt'))


set.seed(1000)
snpset <- snpgdsLDpruning(genofile, ld.threshold=0.5)
snpset.id <- unlist(snpset)

sample.id <- read.gdsn(index.gdsn(genofile, "sample.id"))
pca <- snpgdsPCA(genofile, snp.id=snpset.id, num.thread=1)

tab <- data.frame(sample.id = pca$sample.id,
    pop = factor(pop_code)[match(pca$sample.id, sample.id)],
    EV1 = pca$eigenvect[,1],    # the first eigenvector
    EV2 = pca$eigenvect[,2],    # the second eigenvector
    stringsAsFactors = FALSE)
pdf('/home/vdp5/projects/vivax_cambodia/data/figures/population_figures/pca_eg1_eg2_#VCF1_ld0.5.experiment.nopop.pdf')
plot(tab$EV2, tab$EV1, col=as.integer(tab$pop), xlab="eigenvector 2", ylab="eigenvector 1")
legend("bottomright", legend=levels(tab$pop), pch="o", col=1:nlevels(tab$pop))
dev.off()
