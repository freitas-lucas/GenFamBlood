import os
import re

# Orthologous list for Arthropoda
lista_ortologos = []

odb_OGs = open("/path/to/odb9v1_OGs.tab", "r")

for line in odb_OGs:
    line = line.rstrip()
    line = line.split("\t")
    if line[1] == "6656": #
        lista_ortologos.append(line[0])
odb_OGs.close()

# Save a new OG2genes file containing information for XXXX
OG2genes = open("/path/to/odb9v1_OG2genes.tab", "r")
ArthropodaOG2genes = open("/path/to/Arthropoda_odb9v1_OG2genes.tab", "w")
for linha in OG2genes:
    linha = linha.rstrip()
    linha = linha.split("\t")
    if linha[0] in lista_ortologos:
        ArthropodaOG2genes.write(linha[0] + "\t" + linha[1] + "\n")
    else:
        pass

ArthropodaOG2genes.close()
OG2genes.close()
