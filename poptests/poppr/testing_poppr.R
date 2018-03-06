library("vcfR")
library("poppr")

dat  <- read.vcfR("/newhome/vdp5/projects/vivax_cambodia/data/poptests/nsl/vcf_sitesofinterest/2-CV-tomaster-tmp/LT635621-472556_5000upandback.470056-475056.missense.vcf.gz")

mystrata <- read.csv("/newhome/vdp5/projects/vivax_cambodia/data/poptests/nsl/vcf_sitesofinterest/2-CV-tomaster-tmp/LT635621-472556_5000upandback.470056-475056.missense.vcf.gz.tab.sampletitles")
dat.gc         <- as.genclone(vcfR2genind(dat))
sampleorder    <- match(indNames(dat.gc), mystrata$sample)

strata(dat.gc) <- mystrata[sampleorder, ] # make sure the samples are ordered correctly
setPop(dat.gc) <- ~haplo             # set the population factor
