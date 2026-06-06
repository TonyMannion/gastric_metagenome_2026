import pandas as pd
import os

run_id = '250930Pat'

bbmap_path = '/home/dcm/BBMap_39.06/bbmap'
bbduk_output_folder = 'bbduk_output_folder'

os.makedirs(f'{bbduk_output_folder}', exist_ok=True)

file_df = pd.read_csv('files.txt', sep='\t')

#for folder, file in zip(file_df['folder'], file_df['file']):
#	os.system(f'{bbmap_path}/bbduk.sh \
#	in={folder}/{file}-1_sequence.fastq \
#	in2={folder}/{file}-2_sequence.fastq \
#	out={bbduk_output_folder}/bbduk_{file}-1_sequence.fastq \
#	out2={bbduk_output_folder}/bbduk_{file}-2_sequence.fastq \
#	outm={bbduk_output_folder}/ref_match_{file}-1_sequence.fastq \
#	outm2={bbduk_output_folder}/ref_match_{file}-2_sequence.fastq \
#	stats={bbduk_output_folder}/ref_match_{file}_sequence_stats.txt \
#	ref={bbmap_path}/resources/adapters.fa \
#	ktrim=r k=23 mink=11 hdist=1 tpe tbo')

metaspades_output_folder = 'metaspades_output_folder'

os.makedirs(f'{metaspades_output_folder}', exist_ok=True)

for folder, file in zip(file_df['folder'], file_df['file']):
       os.system(f'python /home/dcm/SPAdes-4.2.0-Linux/bin/spades.py -t 90 -m 325 --meta -1 {bbduk_output_folder}/bbduk_{file}-1_sequence.fastq -2 {bbduk_output_folder}/bbduk_{file}-2_sequence.fastq -o {metaspades_output_folder}/{file}')
