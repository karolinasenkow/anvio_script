## Anvi'o Pangenome Image

## Files:
* anvio_fasta is directory containing .fna files pulled from NCBI
* genome_names.txt contains names of all genome sequences

## Installation:
* install Anvi'o 7 -- https://merenlab.org/2016/06/26/installation-v2/
* update create folder called anvio_fasta containing desired genomes (.fna format)
* update genome_names.txt with genome names (no repeats)
* if running on genus other than Klebsiella, update db name in anvio_script.py lines 31 & 32
 
## To Run:
    python3 anvio_script.py
