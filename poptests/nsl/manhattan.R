library('ggman')


args = commandArgs(trailingOnly=TRUE)
data <- read.table(args[1], sep="\t", header = TRUE)


pdf(args[2])
ggman(data, snp = "snp", bp = "bp", chrom = "chrom", pvalue = "pvalue", logTransform = FALSE)
dev.off()