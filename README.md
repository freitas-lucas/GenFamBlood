# GenFamBlood
## Description of data and scripts used by [Freitas & Nery (2020)](https://bmcevolbiol.biomedcentral.com/articles/10.1186/s12862-020-01650-3).

### Data and scripts
All data was obtained at [OrthoDB v9.1](https://www.orthodb.org/v9.1/index.html?page=filelist). 

- The [0-GetArthropodaOrthoIDs.py](https://github.com/freitas-lucas/GenFamBlood/blob/master/0-GetArthropodaOrthoIDs.py) script was used to get all orthologous IDs related wih Insecta from the [table of cluster ids file](https://www.orthodb.org/v9.1/download/odb9v1_OGs.tab.gz). Next the script parsed the [map cluster ids to gene ids file](https://www.orthodb.org/v9.1/download/odb9v1_OG2genes.tab.gz) to create a new "all cluster ids to gene ids" file for Arthropoda;

- The [1-ParseOrthoDB_createMultipleCopies.py](https://github.com/freitas-lucas/GenFamBlood/blob/master/1-ParseOrthoDB_createMultipleCopies.py) script was used to create one fasta file for each orthologous group using [the fasta files for Metazoa](https://www.orthodb.org/v9.1/download/odb9v1_metazoa_fasta.tar.gz) and the "all cluster ids to gene ids" file for Arthropoda.

- The [2-CreateSingleCopies.py](https://github.com/freitas-lucas/GenFamBlood/blob/master/2-CreateSingleCopies.py) script was used to create single-copy fasta files for each orthologous group. 

- The [3-MafftGblocksLoop.py](https://github.com/freitas-lucas/GenFamBlood/blob/master/3-MafftGblocksLoop.py) script was to run  mafft and Gblocks to align and remove gap-rich regions.

- The [4-CheckGblocks.py](https://github.com/freitas-lucas/GenFamBlood/blob/master/4-CheckGBlocks.py) script was used to select orthologous groups that were used to estimate the divergence time.

- The [5-CreateCAFEtable.py](https://github.com/freitas-lucas/GenFamBlood/blob/master/5-CreateCAFEtable.py) script was used to create CAFE's input table.
