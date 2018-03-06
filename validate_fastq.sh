for alpha in ../data/sequences_gz/*; do
	fastQValidator --file $alpha
done