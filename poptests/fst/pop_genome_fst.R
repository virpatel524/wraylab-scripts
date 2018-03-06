library('PopGenome')
args = commandArgs(trailingOnly=TRUE)

GENOME.class <- readVCF(args[1], 10000,"10",1,5000000)
populations <- read.delim(args[2], col.names = c('sample', 'country', 'population'))

popMT <- as.list(subset(populations, population == '1-MT'))
popCV <- as.list(subset(populations, population == '2-CV'))
popMP <- as.list(subset(populations, population == '3-MP'))


GENOME.class <- set.populations(GENOME.class,list(popCV$sample,popMT$sample,popCV$sample), diploid=FALSE)

GENOME.class <- F_ST.stats(GENOME.class, mode="nucleotide")

pdf('~/tmp/test.pdf')

plot(GENOME.class@nucleotide.F_ST, ylim=c(0,1), xlab="genes", ylab="Hudson’s FST",pch=3)

dev.off()