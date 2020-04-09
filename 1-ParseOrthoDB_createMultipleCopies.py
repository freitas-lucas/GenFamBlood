import os

# Species-ID dictionary
dic_species_id = {"7159": "Aedes", "7165": "Anopheles", "315563": "Belgica", "7176": "Culex", "7200": "Lutzomyia", "39758": "Mayetiola", "29031": "Phlebotomus", "7227": "Drosophila", "7394": "Glossina", "7213": "Ceratitis", "7375": "Lucilia", "36166": "Megaselia", "7370": "Musca", "7460": "Apis", "34740": "Heliconius", "7070": "Tribolium", "1218281": "Limnephilus", "1155016": "Mengenilla", "7029": "Acyrthosiphon", "79782": "Cimex", "121845": "Diaphorina", "56086": "Gerris", "286706": "Halyomorpha", "197043": "Homalodisca", "7536": "Oncopeltus", "38123": "Pachypsylla", "13249": "Rhodnius", "52612": "Calopteryx", "1049336": "Ephemera", "6973": "Blattella", "133901": "Frankliniella", "121225": "Pediculus", "136037": "Zootermopsis"}

# A dictionary with all fasta sequences 
all_fasta_dic = {}
for item in os.listdir("/path/to/folder/with/metazoa/fastas/"):
	if item[:-3] in dic_species_id:
		arquivo = open("/path/to/folder/with/metazoa/fastas/" + item, "r")
		for line in arquivo:
			line = line.rstrip()
			if line.startswith(">"):
				fasta_header = line[1:]
				all_fasta_dic[fasta_header] = ""
			else:
				all_fasta_dic[fasta_header] = all_fasta_dic[fasta_header] + line
		arquivo.close()
	else:
		pass


# To parse map cluster ids to gene ids file for Arthropoda and create a fasta file for orthologous ID
arthropoda_genes_table = open("/path/to/Arthropoda_odb9v1_OG2genes.tab", "r")

for line in arthropoda_genes_table:
	line = line.rstrip()
	line = line.split("\t")
	sp_id = line[1].split(":")
	sp_id = sp_id[0]
	if sp_id in dic_species_id:
		new_file = open("/path/to/orthologous/groups/fastas/" + line[0] + ".fasta", "a")
		new_file.write(">" + str(line[1]) + "\n" + str(all_fasta_dic[line[1]]) + "\n")
		new_file.close()
	else:
		pass