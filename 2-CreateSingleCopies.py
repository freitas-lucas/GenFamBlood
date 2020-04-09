import os

# Species-ID dictionary
dic_species_id = {"7159": "Aedes", "7165": "Anopheles", "315563": "Belgica", "7176": "Culex", "7200": "Lutzomyia", "39758": "Mayetiola", "29031": "Phlebotomus", "7227": "Drosophila", "7394": "Glossina", "7213": "Ceratitis", "7375": "Lucilia", "36166": "Megaselia", "7370": "Musca", "7460": "Apis", "34740": "Heliconius", "7070": "Tribolium", "1218281": "Limnephilus", "1155016": "Mengenilla", "7029": "Acyrthosiphon", "79782": "Cimex", "121845": "Diaphorina", "56086": "Gerris", "286706": "Halyomorpha", "197043": "Homalodisca", "7536": "Oncopeltus", "38123": "Pachypsylla", "13249": "Rhodnius", "52612": "Calopteryx", "1049336": "Ephemera", "6973": "Blattella", "133901": "Frankliniella", "121225": "Pediculus", "136037": "Zootermopsis", "6669": "Daphnia"}

# count = 0

for item in os.listdir("/path/to/orthologous/groups/fastas/"):
#	Number of gene copies per species
	dic_table_zero = {"7159": 0,"7165": 0,"315563": 0,"7176": 0,"7200": 0,"39758": 0,"29031": 0,"7227": 0,"7394": 0,"7213": 0,"7375": 0,"36166": 0,"7370": 0,"7460": 0,"34740": 0,"7070": 0,"1218281": 0,"1155016": 0,"7029": 0,"79782": 0,"121845": 0,"56086": 0,"286706": 0,"197043": 0,"7536": 0,"38123": 0,"13249": 0,"52612": 0,"1049336": 0,"6973": 0,"133901": 0,"121225": 0,"136037": 0,"6669": 0}
	arquivo = open("/dados/lucas.freitas/OrthoDB/2-Genes/" + item, "r")
	seqs_dic = {}
	for line in arquivo:
		line = line.rstrip()
		if line.startswith(">"):
			fasta_header = line[1:]
			seqs_dic[fasta_header] = ""
			count_sp_id = fasta_header.split(":")
			count_sp_id = count_sp_id[0]
			dic_table_zero[count_sp_id] += 1
		else:
			seqs_dic[fasta_header] = seqs_dic[fasta_header] + line
	arquivo.close()

#	Count how many species have one copy and write a new file containing just species with one gene copy
	count_copies = 0
	for key, value in dic_table_zero.iteritems():
		if value == 1:
			count_copies += 1
		else:
			pass
	if count_copies >= 4:
#		count += 1 # Check the number of genes
		single_copies = open("/path/to/single_copy_genes/" + item, "w")
		for chave, valor in seqs_dic.iteritems():
			sp_id = chave.split(":")
			sp_id = sp_id[0]
			if dic_table_zero[sp_id] == 1:
				single_copies.write(">" + str(dic_species_id[sp_id]) + "\n" + str(valor) + "\n")
			else:
				pass
		single_copies.close()
	else:
		pass
