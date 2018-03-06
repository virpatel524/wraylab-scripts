


bed.fn <- system.file("extdata", "plinkhapmap.bed.gz", package="SNPRelate")
fam.fn <- system.file("extdata", "plinkhapmap.fam.gz", package="SNPRelate")
bim.fn <- system.file("extdata", "plinkhapmap.bim.gz", package="SNPRelate")

snpgdsBED2GDS(bed.fn, fam.fn, bim.fn, "HapMap.gds")
genofile <- snpgdsOpen("HapMap.gds")
RV <- snpgdsPCA(genofile)
plot(RV$eigenvect[,2], RV$eigenvect[,1], xlab="PC 2", ylab="PC 1", col=rgb(0,0,150, 50, maxColorValue=255), pch=19)

snpgdsClose(genofile)