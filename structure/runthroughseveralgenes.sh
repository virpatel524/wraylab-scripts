while IFS= read -r line
do 
  echo "$line"
  ./annotated_faststructure_run.sh "$line" ${2} ${3} &
done < ${1}


cd /home/vdp5/projects/vivax_cambodia/data/distrust/