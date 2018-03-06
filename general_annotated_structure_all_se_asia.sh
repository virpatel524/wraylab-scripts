plink --vcf $1 --out ../data/plink_output/all_se_asia_plink --double-id --allow-extra-chr   

python /home/vdp5/source_code/fastStructure/structure.py --output=/home/vdp5/projects/vivax_cambodia/data/structure_out/all_se_asia --input=/newhome/vdp5/projects/vivax_cambodia/data/plink_output/all_se_asia_plink -K 2 --full & 
# python /home/vdp5/source_code/fastStructure/structure.py --output=/home/vdp5/projects/vivax_cambodia/data/structure_out/all_se_asia --input=/newhome/vdp5/projects/vivax_cambodia/data/plink_output/all_se_asia_plink -K 3 --full &
# python /home/vdp5/source_code/fastStructure/structure.py --output=/home/vdp5/projects/vivax_cambodia/data/structure_out/all_se_asia --input=/newhome/vdp5/projects/vivax_cambodia/data/plink_output/all_se_asia_plink -K 4 --full &
# python /home/vdp5/source_code/fastStructure/structure.py --output=/home/vdp5/projects/vivax_cambodia/data/structure_out/all_se_asia --input=/newhome/vdp5/projects/vivax_cambodia/data/plink_output/all_se_asia_plink -K 5 --full &
# python /home/vdp5/source_code/fastStructure/structure.py --output=/home/vdp5/projects/vivax_cambodia/data/structure_out/all_se_asia --input=/newhome/vdp5/projects/vivax_cambodia/data/plink_output/all_se_asia_plink -K 6 --full &
# python /home/vdp5/source_code/fastStructure/structure.py --output=/home/vdp5/projects/vivax_cambodia/data/structure_out/all_se_asia --input=/newhome/vdp5/projects/vivax_cambodia/data/plink_output/all_se_asia_plink -K 7 --full &


wait

cd /home/vdp5/source_code/fastStructure

distruct.py -K 2 --input /home/vdp5/projects/vivax_cambodia/data/structure_out/all_se_asia --output /home/vdp5/projects/vivax_cambodia/data/distrust/all_se_asia_Kof_2 --popfile /newhome/vdp5/projects/vivax_cambodia/data/txt_files/lists_gatk/all_sample_#VCF1.txt
# distruct.py -K 3 --input /home/vdp5/projects/vivax_cambodia/data/structure_out/all_se_asia --output /home/vdp5/projects/vivax_cambodia/data/distrust/all_se_asia_Kof_3 --popfile /newhome/vdp5/projects/vivax_cambodia/data/txt_files/lists_gatk/all_sample_#VCF1.txt
# distruct.py -K 4 --input /home/vdp5/projects/vivax_cambodia/data/structure_out/all_se_asia --output /home/vdp5/projects/vivax_cambodia/data/distrust/all_se_asia_Kof_4 --popfile /newhome/vdp5/projects/vivax_cambodia/data/txt_files/lists_gatk/all_sample_#VCF1.txt
# distruct.py -K 5 --input /home/vdp5/projects/vivax_cambodia/data/structure_out/all_se_asia --output /home/vdp5/projects/vivax_cambodia/data/distrust/all_se_asia_Kof_5 --popfile /newhome/vdp5/projects/vivax_cambodia/data/txt_files/lists_gatk/all_sample_#VCF1.txt
# distruct.py -K 6 --input /home/vdp5/projects/vivax_cambodia/data/structure_out/all_se_asia --output /home/vdp5/projects/vivax_cambodia/data/distrust/all_se_asia_Kof_6 --popfile /newhome/vdp5/projects/vivax_cambodia/data/txt_files/lists_gatk/all_sample_#VCF1.txt
# distruct.py -K 7 --input /home/vdp5/projects/vivax_cambodia/data/structure_out/all_se_asia --output /home/vdp5/projects/vivax_cambodia/data/distrust/all_se_asia_Kof_7 --popfile /newhome/vdp5/projects/vivax_cambodia/data/txt_files/lists_gatk/all_sample_#VCF1.txt

