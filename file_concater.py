import os

folders = [
    "D25-12455",
    "D25-12456",
    "D25-12457",
    "D25-12458",
    "D25-12459",
    "D25-12460",
    "D25-12461",
    "D25-12462",
    "D25-12463",
    "D25-12464",
    "D25-12465",
    "D25-12466",
    "D25-12467",
    "D25-12468",
    "D25-12469",
    "D25-12470",
    "D25-12471",
    "D25-12472",
    "D25-12473",
    "D25-12474",
    "D25-12475",
    "D25-12476",
    "D25-12477",
    "D25-12478"
]

def concatenate_fastq(file_1, file_2, output_file):
    # Ensure the output folder exists
    output_dir = os.path.dirname(output_file)
    os.makedirs(output_dir, exist_ok=True)

    # Run the shell command using 'cat' to concatenate the files
    command = f"cat {file_1} {file_2} > {output_file}"

    try:
        os.system(command)
        print(f"Successfully concatenated {file_1} and {file_2} into {output_file}")
    except Exception as e:
        print(f"Error: {str(e)}")

for folder in folders:
    # Generate the file paths
    file_1 = f'{folder}/250930Pat_{folder}-1_1_sequence.fastq'
    file_2 = f'{folder}/250930Pat_{folder}-2_1_sequence.fastq'
    output_file = f'{folder}/250930Pat_{folder}-1_sequence.fastq'

    concatenate_fastq(file_1, file_2, output_file)

    file_1 = f'{folder}/250930Pat_{folder}-1_2_sequence.fastq'
    file_2 = f'{folder}/250930Pat_{folder}-2_2_sequence.fastq'
    output_file = f'{folder}/250930Pat_{folder}-2_sequence.fastq'

    concatenate_fastq(file_1, file_2, output_file)
