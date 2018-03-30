library('ggman')

args = commandArgs(trailingOnly=TRUE)
dat <- read.table(args[1],  sep='\t', header=TRUE)
highlights <- scan(args[2],character(), quote = "")



p1 <- ggman(dat, snp = "snp", bp = "bp", chrom = "chrom", pvalue = "FST", logTransform=FALSE, ylabel='FST Value', ymax = 1)
ggmanHighlight(p1, highlight = highlights, colour="dodgerblue1")