for alpha in ../../data/variant_files/*; do
	cut -f 1-10 $alpha | sponge $alpha
done