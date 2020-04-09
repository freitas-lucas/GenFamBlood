import os

for item in os.listdir("/path/to/single_copy_genes/"):
	os.system("mafft --retree 1 --maxiterate 0 --anysymbol /path/to/single_copy_genes/" + str(item) + " > " + "/path/to/single_copy_genes/aligned/" + str(item[:-6]) + ".aln")
	os.system("Gblocks /path/to/single_copy_genes/aligned/" + str(item) + " -t=p -e=.out -b4=5 -b5=h -d=y")
