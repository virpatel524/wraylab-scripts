# hard coded for 3 popualtions, change accordingly for otheres. 

#first arg is meanQ file, second is file with NO col names but according to format shown below, thrid is

barNaming <- function(vec) {
    retVec <- vec
    for(k in 2:length(vec)) {
        if(vec[k-1] == vec[k])
            retVec[k] <- ""
    }
    return(retVec)
}



args = commandArgs(trailingOnly=TRUE)

tbl=read.table(args[1])
indTable = read.table(args[2], col.names = c("Sample", "Country", "Population"))
par(mar=c(10,4,4,4))

pdf(paste0("/home/vdp5/projects/vivax_cambodia/data/figures/admixture/", args[3], ".pdf"))
mergedAdmixtureTable = cbind(tbl, indTable)
ordered = mergedAdmixtureTable[order(mergedAdmixtureTable$Population),]
print(ordered)
theta <- barplot(t(as.matrix(ordered[,1:4])), col=rainbow(3), border=NA, names.arg=barNaming(ordered$Population), las=1)
text(theta, -3.7, srt = 60, adj= 1, xpd = TRUE, labels = barNaming(ordered$Population) , cex=1.2)
dev.off()
