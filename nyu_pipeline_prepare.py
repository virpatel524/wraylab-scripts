import os
import sys
import csv
counter = 1

launcscript = open('nyu_pipeline_launch.sh', 'w')

for alpha in os.listdir('/home/vdp5/projects/vivax_cambodia/data/sequences_bam/'):
    if '.bai' in alpha:
        continue
    if counter != 11:
        launcscript.write('bash NYU_pipeline.sh {} &\n'.format(
            os.path.join('/home/vdp5/projects/vivax_cambodia/data/sequences_bam/', alpha)))
    else:
        launcscript.write('wait\n')
        counter = 1
        launcscript.write('bash NYU_pipeline.sh {} &\n'.format(
            os.path.join('/home/vdp5/projects/vivax_cambodia/data/sequences_bam/', alpha)))
    counter += 1
