import glob
import os
import shutil

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

for folder_name in folders:
    # Correct pattern to match all relevant folders
    source_folders = glob.glob(f'{folder_name}*')  # No space after folder name

    # Destination folder
    destination_folder = folder_name

    # Create destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    # Loop through all matching folders
    for folder in source_folders:
        if os.path.isdir(folder):
            # Get all files in each folder
            for file_name in os.listdir(folder):
                source_path = os.path.join(folder, file_name)
                if os.path.isfile(source_path):
                    dest_path = os.path.join(destination_folder, file_name)

                    # Handle name conflicts by renaming
                    base, ext = os.path.splitext(file_name)
                    count = 1
                    while os.path.exists(dest_path):
                        dest_path = os.path.join(destination_folder, f"{base}_{count}{ext}")
                        count += 1

                    shutil.move(source_path, dest_path)
                    print(f"Moved: {source_path} → {dest_path}")
