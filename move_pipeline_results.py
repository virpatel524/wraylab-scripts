import os
import sys
import shutil

for di in os.listdir('../data/nyu_pipeline_results'):
    name = di.split('.')[0]
    for fle in os.listdir('../data/nyu_pipeline_results/{}'.format(di)):
        if fle == 'filtered_snps_final.vcf':
            shutil.copy(os.path.join('../data/nyu_pipeline_results/{}/{}'.format(di, fle)),
                        '/home/vdp5/projects/vivax_cambodia/data/nyu_pipeline_recacl_all/snps/{}_{}.vcf'.format(name, 'snps'))
        if fle == 'filtered_indels_recal.vcf':
            shutil.copy(os.path.join('../data/nyu_pipeline_results/{}/{}'.format(di, fle)),
                        '/home/vdp5/projects/vivax_cambodia/data/nyu_pipeline_recacl_all/indels/{}_{}.vcf'.format(name, 'indels'))
