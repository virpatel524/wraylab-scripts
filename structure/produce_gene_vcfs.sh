transfer() { if [ $# -eq 0 ]; then echo "No arguments specified. Usage:\necho transfer /tmp/test.md\ncat /tmp/test.md | transfer test.md"; return 1; fi
tmpfile=$( mktemp -t transferXXX ); if tty -s; then basefile=$(basename "$1" | sed -e 's/[^a-zA-Z0-9._-]/-/g'); curl --progress-bar --upload-file "$1" "https://transfer.sh/$basefile" >> $tmpfile; else curl --progress-bar --upload-file "-" "https://transfer.sh/$1" >> $tmpfile ; fi; cat $tmpfile; rm -f $tmpfile; }


echo ${@}

geneofinterest=$1
echo $geneofinterest

rm -rf ../../data/structure_out/${1}
mkdir ../../data/structure_out/${1}

java -jar /home/vdp5/source_code/snpEff/SnpSift.jar filter "(ANN[*].GENE = '${1}')" ${2} > ../../data/extracted_vcf/${3}_extracted.vcf.ann


