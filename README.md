# GenFamBlood
## Description of data and scripts used.

### 1 Data
All data was obtained at [OrthoDB v9.1](https://www.orthodb.org/v9.1/index.html?page=filelist). We used both flat files [link](addlink) and [link](addlink).

### 2 Scripts
We used the 0-GetArthropodaOrthoIDs.py to retrieve all GROUPS sequences. Then we used 1-ParseOrthoDB_createMultipleCopies.py and 2-CreateSingleCopies.py to create one fasta sequence per gene family. The first script generate fasta sequences where multiple copies are allowed (to run CAFE) and the second script generate fasta sequences with single-copies (to run MCMCtree).
