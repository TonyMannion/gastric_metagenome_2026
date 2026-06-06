import pandas as pd
import os

#path variables
bbmap_path = '/home/dcm/BBMap_39.06/bbmap'
bbduk_output_folder = 'bbduk_output_folder'
bbnorm_output_folder = 'bbnorm_output_folder_100x'
metaspades_output_folder = 'metaspades_output_folder_bbnorm_100x'
bbmap_coverage_out = 'bbmap_coverage_out_bbnorm_100x'
scaffolds_folder_1000bp = 'scaffolds_folder_1000bp'
nt_prok_blastn_out = 'nt_prok_blastn_out'
annotation_output = 'annotation_output'


#input file
file_df = pd.read_csv('files.txt', sep='\t')

###########
###bbduk###
###########

# os.makedirs(f'{bbduk_output_folder}', exist_ok=True)

# for folder, file in zip(file_df['folder'], file_df['file']):
	# os.system(f'{bbmap_path}/bbduk.sh \
	# in={folder}/{file}-1_sequence.fastq \
	# in2={folder}/{file}-2_sequence.fastq \
	# out={bbduk_output_folder}/bbduk_{file}-1_sequence.fastq \
	# out2={bbduk_output_folder}/bbduk_{file}-2_sequence.fastq \
	# outm={bbduk_output_folder}/ref_match_{file}-1_sequence.fastq \
	# outm2={bbduk_output_folder}/ref_match_{file}-2_sequence.fastq \
	# stats={bbduk_output_folder}/ref_match_{file}_sequence_stats.txt \
	# ref={bbmap_path}/resources/adapters.fa \
	# ktrim=r k=23 mink=11 hdist=1 tpe tbo')

############
###bbnorm###
############

# os.makedirs(f'{bbnorm_output_folder}', exist_ok=True)

# for folder, file in zip(file_df['folder'], file_df['file']):
	# os.system(f'{bbmap_path}/bbnorm.sh \
	# in={bbduk_output_folder}/bbduk_{file}-1_sequence.fastq \
	# in2={bbduk_output_folder}/bbduk_{file}-2_sequence.fastq\
	# out={bbnorm_output_folder}/bbnorm_bbduk_{file}-1_sequence.fastq \
	# out2={bbnorm_output_folder}/bbnorm_bbduk_{file}-2_sequence.fastq \
	# target=100 \
	# hist={bbnorm_output_folder}/bbnorm_bbduk_{file}_hist.txt')

################
###metaspades###
################

# os.makedirs(f'{metaspades_output_folder}', exist_ok=True)

# for folder, file in zip(file_df['folder'], file_df['file']):
	# os.system(f'python /home/dcm/SPAdes-4.2.0-Linux/bin/spades.py \
	# -t 90 --meta \
	# -1 {bbnorm_output_folder}/bbnorm_bbduk_{file}-1_sequence.fastq \
	# -2 {bbnorm_output_folder}/bbnorm_bbduk_{file}-2_sequence.fastq \
	# -o {metaspades_output_folder}/{file}')

####################
###bbmap coverage###
####################

# os.makedirs(f'{bbmap_coverage_out}', exist_ok=True)

# for folder, file in zip(file_df['folder'], file_df['file']):
	# os.system(f'{bbmap_path}/bbmap.sh \
	# in={bbduk_output_folder}/bbduk_{file}-1_sequence.fastq \
	# in2={bbduk_output_folder}/bbduk_{file}-2_sequence.fastq \
	# ref={metaspades_output_folder}/{file}/scaffolds.fasta \
	# covstats={bbmap_coverage_out}/{file}_constats.txt \
	# covhist={bbmap_coverage_out}/{file}_covhist.txt \
	# basecov={bbmap_coverage_out}/{file}_basecov.txt \
	# bincov={bbmap_coverage_out}/{file}_bincov.txt \
	# scafstats={bbmap_coverage_out}/{file}_scafstats.txt \
	# rpkm={bbmap_coverage_out}/{file}_rpkm.txt \
	# outu={bbmap_coverage_out}/{file}_umapped.fastq')


# ##############################
# ##bbtool contig size filter###
# ##############################

# os.makedirs(f'{metaspades_output_folder}/{scaffolds_folder_1000bp}', exist_ok=True)

# for folder, file in zip(file_df['folder'], file_df['file']):
	# os.system(f'{bbmap_path}/reformat.sh \
	# in={metaspades_output_folder}/{file}/scaffolds.fasta \
	# out={metaspades_output_folder}/{scaffolds_folder_1000bp}/{file}_scaffolds_1000bp.fasta \
	# minlength=1000')


# ############################
# ## send contigs to bv-brc###
# ############################

# for folder, file in zip(file_df['folder'], file_df['file']):
	# os.system(f'p3-cp \
	# {metaspades_output_folder}/{scaffolds_folder_1000bp}/{file}_scaffolds_1000bp.fasta \
	# ws:/anthonymannion@patricbrc.org/home/250513Pat_250728Pat_250930Pat/metaspades_output_folder_bbnorm_100x/{file}_scaffolds_1000bp.fasta \
	# -f --map-suffix fasta=contigs')


# ####################################
# ## send annotation jobs to bv-brc###
# ####################################

# for folder, file in zip(file_df['folder'], file_df['file']):
	# # define variables
	# file_name = f'{file}_scaffolds_1000bp'
	# contig_path = f'/anthonymannion@patricbrc.org/home/250513Pat_250728Pat_250930Pat/metaspades_output_folder_bbnorm_100x/{file_name}.fasta'
	# output_path = f'/anthonymannion@patricbrc.org/home/250513Pat_250728Pat_250930Pat/annotations'
	
	# # Read the template once
	# with open('Annotations_submission_template.json', 'r') as f:
		# content = f.read()
	# # Dictionary of replacements
	# replacements = {
		# '$$file_name$$': file_name,
		# '$$contig_path$$': contig_path,
		# '$$output_path$$': output_path,
	# }
	
	# # Perform all replacements
	# for old, new in replacements.items():
		# content = content.replace(old, str(new))
	
	# # Write the modified content to output
	# with open('Annotations_submission.json', 'w') as f:
		# f.write(content)

	# os.system(f'appserv-start-app GenomeAnnotation Annotations_submission.json \"parrello@patricbrc.org/home/\"')


# ######################################
# ### get NCBI nt prok blast database###
# ######################################

#update_blastdb.pl --showall
#update_blastdb.pl --decompress ref_prok_rep_genomes

# ##############################################
# ### blastn contigs against nt prok database###
# ##############################################

# os.makedirs(f'{nt_prok_blastn_out}', exist_ok=True)

# for folder, file in zip(file_df['folder'], file_df['file']):
	# os.system(f'blastn \
	# -query {metaspades_output_folder}/{scaffolds_folder_1000bp}/{file}_scaffolds_1000bp.fasta \
	# -db /home/dcm/bioinformatic_scripts/blast_databases/nt_prok_6_28_25/nt_prok \
	# -outfmt "6 qseqid sseqid salltitles staxids pident length qlen slen mismatch gapopen qstart qend sstart send evalue bitscore" \
	# -max_target_seqs 1 \
	# -num_threads 90 \
	# -out {nt_prok_blastn_out}/{file}_scaffolds_1000bp_nt_prok_blastn_out.txt')


# ########################################
# ### download annotation output files ###
# ########################################

# os.makedirs(f'{annotation_output}/features_table', exist_ok=True)
# os.makedirs(f'{annotation_output}/protein_annotations', exist_ok=True)
# os.makedirs(f'{annotation_output}/DNA_annotations', exist_ok=True)

# for folder, file in zip(file_df['folder'], file_df['file']):

	# path = 'anthonymannion@patricbrc.org/home/250513Pat_250728Pat_250930Pat/annotations'
	# file_name = f'annotations_{file}_scaffolds_1000bp'

	# # features
	# os.system(f'p3-cp \
	# ws:/{path}/.{file_name}/{file_name}.txt \
	# {annotation_output}/features_table/{file_name}.txt')

	# # protein annotations
	# os.system(f'p3-cp \
	# ws:/{path}/.{file_name}/{file_name}.feature_protein.fasta \
	# {annotation_output}/protein_annotations/{file_name}.feature_protein.fasta')

	# # DNA annotations
	# os.system(f'p3-cp \
	# ws:/{path}/.{file_name}/{file_name}.feature_dna.fasta \
	# {annotation_output}/DNA_annotations/{file_name}.feature_dna.fasta')


####################################################################################
### InterProScan on Protein annotatins 
###
### AntiFam-7.0,CDD-3.20,Coils-2.2.1,FunFam-4.3.0,Gene3D-4.3.0,
### Hamap-2023_05,MobiDBLite-4.0,NCBIfam-15.0,PANTHER-19.0,Pfam-37.1,
### Phobius-1.01,PIRSF-3.10,PIRSR-2023_05,PRINTS-42.0,ProSitePatterns-2023_05,
### ProSiteProfiles-2023_05,SFLD-4,SignalP_EUK-4.1,SignalP_GRAM_NEGATIVE-4.1,
### SignalP_GRAM_POSITIVE-4.1,SMART-9.0,SUPERFAMILY-1.75
####################################################################################

os.makedirs(f'{annotation_output}/IPS', exist_ok=True)

for folder, file in zip(file_df['folder'], file_df['file']):

	file_name = f'annotations_{file}_scaffolds_1000bp'

	os.system(f'/home/dcm/interproscan/interproscan-5.72-103.0/interproscan.sh \
	-i {annotation_output}/protein_annotations/{file_name}.feature_protein.fasta \
	-dp -b {annotation_output}/IPS/{file}_ips \
	-f tsv -cpu 90 -pa -goterms -iprlookup')
