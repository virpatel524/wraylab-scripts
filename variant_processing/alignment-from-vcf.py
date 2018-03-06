from Bio import SeqIO
from pysam import VariantFile
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
import sys

helpstr = '''The script requires the following 7 arguements (in the given order):
    path to the reference genome in fasta format
    path to the vcf
    name of the contig that contains the region of interest
    start of the region
    end of the region
    ploidy (This script obviously only makes sense if variants are phased. One sequence per genome copy will be generated)
    path to the output file. This will be in fasta format.
An 8th arguement can optionally be supplied and should specify the path to a file containing a list of individuals to be included.
If not supplied, all individuals will be used.'''

print 'Alignment-from-vcf, written by Stephan Kamrad (stephan.kamrad@crick.ac.uk)'

if len(sys.argv) not in [8,9]:
    print helpstr
    sys.exit('Invalid arguements supplied')

ref_path = sys.argv[1]
print 'Reading the reference genome: '+ref_path
ref = SeqIO.index(ref_path, "fasta")

vcf_path = sys.argv[2]
print 'Reading the vcf: '+vcf_path
vcffile = VariantFile(vcf_path)

contig = sys.argv[3]
start = int(sys.argv[4])
end = int(sys.argv[5])
print 'Getting variants in region %s:%i-%u'%(contig, start, end)
variants = list(vcffile.fetch(contig, start, end-1))
ref_seq = ref[contig].seq[start:end]

if len(variants) == 0:
    raise Exception('No variants in specified region. Terminating.')

ploidy = int(sys.argv[6])
print 'Ploidy is %i.'%ploidy

if len(sys.argv) == 9:
    samples_path = sys.argv[8]
    with open(samples_path, 'r') as sfile:
        samples = [l.strip() for l in sfile if l.strip()!='']
    print 'Generating alignment for the following individuals: '+str(samples)
else:
    samples = list(variants[0].samples.keys())
    print 'Generating alignment for the all individuals: '+str(samples)

def get_sequence(ref_seq, variants, s, p):
    seq = list(str(ref_seq))
    for v in variants:
        #In order to create a correct alignement, we need to determine the length of the longest allele if the variant is an indel
        max_indel_length = max(map(len,v.alleles))
        
        #Now we determine the allele of the individual at the specified phase
        allele = v.samples[s].alleles[p]
        allele = allele if allele is not None else 'N'

        #Adding the appropriate number of - so alignment stays intact
        if len(allele) != max_indel_length:
            allele += '-'*(max_indel_length-len(allele))
        seq[v.pos-start] =  allele 
    return ''.join(seq)

#Getting sequences for all individuals and haplotypes
records = [SeqRecord(Seq(get_sequence(ref_seq, variants, s, p)), id='%s-%i-%s:%i-%i'%(s, p, contig, start, end)) for p in range(ploidy) for s in samples]

out_path = sys.argv[7]
print 'Writing alignement to: '+out_path
SeqIO.write(records, out_path, "fasta")

print 'Done.'
