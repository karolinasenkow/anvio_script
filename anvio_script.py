import csv
import os
path = os.getcwd()
file = open('genome_names.txt').read().splitlines()

# reformat fasta files from .fna to .fa
for i in file:
    os.system('anvi-script-reformat-fasta --seq-type NT ' + path + '/anvio_fasta/' + i + '.fna -o ' + path + '/new_fasta/' + i + '.fa -l 1000 --simplify-names')

# generate a new anvi'o contigs database
for i in file:
    os.system('anvi-gen-contigs-database -f ' + path + '/new_fasta/' + i + '.fa -o ' + path + '/contigs_db/' + i + '.db -n "species_db"')

# populate tables that store HMM hits in an anvi'o contigs database
for i in file:
    os.system('anvi-run-hmms -c ' + path + '/contigs_db/' + i + '.db')

# run NCBI's COGs to associate genes in an anvi'o contigs database with functions
for i in file:
    os.system('anvi-run-ncbi-cogs -c ' + path + '/contigs_db/' + i + '.db')

# create external genomes file
col0 = ['name']
col1 = ['contigs_db_path']
for i in range(len(file)):
    col0.append('genome' + str(i))
for i in file:
    col1.append('contigs_db/' + i + '.db')

with open(path + '/external-genomes.txt', 'w') as f:
	writer = csv.writer(f, delimiter='\t')
	writer.writerows(zip(col0, col1))

# generate an anvi’o genomes storage
os.system('anvi-gen-genomes-storage -e external-genomes.txt -o species-GENOMES.db')

# generate an anvi’o pan database
os.system('anvi-pan-genome -g species-GENOMES.db -n KLEBSIELLA --use-ncbi-blast --mcl-inflation 10 -T 5')


# visualize pangenome image
os.system('anvi-display-pan -p KLEBSIELLA/KLEBSIELLA-PAN.db -g species-GENOMES.db')
