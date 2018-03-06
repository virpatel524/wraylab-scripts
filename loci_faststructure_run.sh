transfer() { if [ $# -eq 0 ]; then echo "No arguments specified. Usage:\necho transfer /tmp/test.md\ncat /tmp/test.md | transfer test.md"; return 1; fi
tmpfile=$( mktemp -t transferXXX ); if tty -s; then basefile=$(basename "$1" | sed -e 's/[^a-zA-Z0-9._-]/-/g'); curl --progress-bar --upload-file "$1" "https://transfer.sh/$basefile" >> $tmpfile; else curl --progress-bar --upload-file "-" "https://transfer.sh/$1" >> $tmpfile ; fi; cat $tmpfile; rm -f $tmpfile; }



geneofinterest=$1
rm -rf ../data/structure_out/${1}
mkdir ../data/structure_out/${1}

java -jar  /newhome/vdp5/source_code/GenomeAnalysisTK.jar  -T SelectVariants --excludeNonVariants -R /newhome/vdp5/data/reference_genomes/PVP01.fasta -V ${2} -L ${1}  -o ../data/extracted_vcf/${1}_extracted.vcf.ann
plink --vcf ../data/extracted_vcf/${1}_extracted.vcf.ann --out ../data/plink_output/${1}_plink --double-id --allow-extra-chr 

python /home/vdp5/source_code/fastStructure/structure.py --output=/home/vdp5/projects/vivax_cambodia/data/structure_out/${1}/${1} --input=/home/vdp5/projects/vivax_cambodia/data/plink_output/${1}_plink -K 2 --full &
python /home/vdp5/source_code/fastStructure/structure.py --output=/home/vdp5/projects/vivax_cambodia/data/structure_out/${1}/${1} --input=/home/vdp5/projects/vivax_cambodia/data/plink_output/${1}_plink -K 3 --full &
python /home/vdp5/source_code/fastStructure/structure.py --output=/home/vdp5/projects/vivax_cambodia/data/structure_out/${1}/${1} --input=/home/vdp5/projects/vivax_cambodia/data/plink_output/${1}_plink -K 4 --full &
python /home/vdp5/source_code/fastStructure/structure.py --output=/home/vdp5/projects/vivax_cambodia/data/structure_out/${1}/${1} --input=/home/vdp5/projects/vivax_cambodia/data/plink_output/${1}_plink -K 5 --full &
python /home/vdp5/source_code/fastStructure/structure.py --output=/home/vdp5/projects/vivax_cambodia/data/structure_out/${1}/${1} --input=/home/vdp5/projects/vivax_cambodia/data/plink_output/${1}_plink -K 6 --full &
python /home/vdp5/source_code/fastStructure/structure.py --output=/home/vdp5/projects/vivax_cambodia/data/structure_out/${1}/${1} --input=/home/vdp5/projects/vivax_cambodia/data/plink_output/${1}_plink -K 7 --full &
python /home/vdp5/source_code/fastStructure/structure.py --output=/home/vdp5/projects/vivax_cambodia/data/structure_out/${1}/${1} --input=/home/vdp5/projects/vivax_cambodia/data/plink_output/${1}_plink -K 8 --full &
python /home/vdp5/source_code/fastStructure/structure.py --output=/home/vdp5/projects/vivax_cambodia/data/structure_out/${1}/${1} --input=/home/vdp5/projects/vivax_cambodia/data/plink_output/${1}_plink -K 9 --full &
python /home/vdp5/source_code/fastStructure/structure.py --output=/home/vdp5/projects/vivax_cambodia/data/structure_out/${1}/${1} --input=/home/vdp5/projects/vivax_cambodia/data/plink_output/${1}_plink -K 10 --full &
python /home/vdp5/source_code/fastStructure/structure.py --output=/home/vdp5/projects/vivax_cambodia/data/structure_out/${1}/${1} --input=/home/vdp5/projects/vivax_cambodia/data/plink_output/${1}_plink -K 11 --full &
python /home/vdp5/source_code/fastStructure/structure.py --output=/home/vdp5/projects/vivax_cambodia/data/structure_out/${1}/${1} --input=/home/vdp5/projects/vivax_cambodia/data/plink_output/${1}_plink -K 12 --full &
wait 

cd /home/vdp5/source_code/fastStructure

mkdir -p /home/vdp5/projects/vivax_cambodia/data/distrust/$1

distruct.py -K 2 --input /home/vdp5/projects/vivax_cambodia/data/structure_out/$1/$1 --output /home/vdp5/projects/vivax_cambodia/data/distrust/$1/Kof_2.png --popfile /newhome/vdp5/projects/vivax_cambodia/data/other/labels-samples.txt
distruct.py -K 3 --input /home/vdp5/projects/vivax_cambodia/data/structure_out/$1/$1 --output /home/vdp5/projects/vivax_cambodia/data/distrust/$1/Kof_3.png --popfile /newhome/vdp5/projects/vivax_cambodia/data/other/labels-samples.txt
distruct.py -K 4 --input /home/vdp5/projects/vivax_cambodia/data/structure_out/$1/$1 --output /home/vdp5/projects/vivax_cambodia/data/distrust/$1/Kof_4.png --popfile /newhome/vdp5/projects/vivax_cambodia/data/other/labels-samples.txt
distruct.py -K 5 --input /home/vdp5/projects/vivax_cambodia/data/structure_out/$1/$1 --output /home/vdp5/projects/vivax_cambodia/data/distrust/$1/Kof_5.png --popfile /newhome/vdp5/projects/vivax_cambodia/data/other/labels-samples.txt
distruct.py -K 6 --input /home/vdp5/projects/vivax_cambodia/data/structure_out/$1/$1 --output /home/vdp5/projects/vivax_cambodia/data/distrust/$1/Kof_6.png --popfile /newhome/vdp5/projects/vivax_cambodia/data/other/labels-samples.txt
distruct.py -K 7 --input /home/vdp5/projects/vivax_cambodia/data/structure_out/$1/$1 --output /home/vdp5/projects/vivax_cambodia/data/distrust/$1/Kof_7.png --popfile /newhome/vdp5/projects/vivax_cambodia/data/other/labels-samples.txt
distruct.py -K 8 --input /home/vdp5/projects/vivax_cambodia/data/structure_out/$1/$1 --output /home/vdp5/projects/vivax_cambodia/data/distrust/$1/Kof_8.png --popfile /newhome/vdp5/projects/vivax_cambodia/data/other/labels-samples.txt
distruct.py -K 9 --input /home/vdp5/projects/vivax_cambodia/data/structure_out/$1/$1 --output /home/vdp5/projects/vivax_cambodia/data/distrust/$1/Kof_9.png --popfile /newhome/vdp5/projects/vivax_cambodia/data/other/labels-samples.txt
distruct.py -K 10 --input /home/vdp5/projects/vivax_cambodia/data/structure_out/$1/$1 --output /home/vdp5/projects/vivax_cambodia/data/distrust/$1/Kof_10.png --popfile /newhome/vdp5/projects/vivax_cambodia/data/other/labels-samples.txt
distruct.py -K 11 --input /home/vdp5/projects/vivax_cambodia/data/structure_out/$1/$1 --output /home/vdp5/projects/vivax_cambodia/data/distrust/$1/Kof_11.png --popfile /newhome/vdp5/projects/vivax_cambodia/data/other/labels-samples.txt
distruct.py -K 12 --input /home/vdp5/projects/vivax_cambodia/data/structure_out/$1/$1 --output /home/vdp5/projects/vivax_cambodia/data/distrust/$1/Kof_12.png --popfile /newhome/vdp5/projects/vivax_cambodia/data/other/labels-samples.txt

cd /home/vdp5/projects/vivax_cambodia/data/distrust/
zip ${1}.zip $1/*
transfer ${1}.zip
