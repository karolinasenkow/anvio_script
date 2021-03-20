## Anvi'o Pangenome Image

## Files:
* anvio_fasta is directory containing .fna files pulled from NCBI
* genome_names.txt contains names of all genome sequences

## Installation:
* install Anvi'o 7 -- https://merenlab.org/2016/06/26/installation-v2/
* create folder called anvio_fasta containing desired genomes (.fna format)
* update genome_names.txt with genome names (no repeats)
* if running on genus other than Klebsiella, update db name in anvio_script.py lines 31 & 32
 
## To Run:
    python3 anvio_script.py
    
## References
1. Eren AM, Esen ÖC, Quince C, Vineis JH, Morrison HG, Sogin ML, Delmont TO. 2015. Anvi’o: an advanced analysis and visualization platform for ‘omics data. PeerJ 3:e1319 https://doi.org/10.7717/peerj.1319

2. Delmont TO, Eren AM. 2018. Linking pangenomes and metagenomes: the Prochlorococcus metapangenome. PeerJ 6:e4320 https://doi.org/10.7717/peerj.4320
