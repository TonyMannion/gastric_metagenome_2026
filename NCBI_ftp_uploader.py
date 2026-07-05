import os
from ftplib import FTP
import pandas as pd

# --- Configuration ---
FTP_HOST = "ftp-private.ncbi.nlm.nih.gov"
FTP_USER = "subftp"
FTP_PASS = "xxxxxxx"  # Replace with your actual password

# Remote directories
REMOTE_DIR_1 = "xxxx" #replace with upload/username based on NCBI 
REMOTE_DIR_2 = "xxxx" # replace with subfolder created within above directory 

# Path to your tab-delimited text file
TSV_FILE_PATH = "ftp_file_list.txt"


def load_file_list(file_path):
    """Loads the tab-delimited file into a Pandas DataFrame."""
    print(f"Loading file list from: {file_path}")

    # Note: If your file already has a header row (e.g., 'path' and 'filename'),
    # remove `header=None` and `names=[...]` and use your actual column names.
    df = pd.read_csv(
        file_path,
        sep="\t"
    )

    # Clean up any leading/trailing whitespaces from paths and filenames
    df["folder_path"] = df["folder_path"].str.strip()
    df["file_name"] = df["file_name"].str.strip()

    # Drop rows that have missing values in either column
    df = df.dropna(subset=["folder_path", "file_name"])

    return df


def upload_files_from_group(ftp, local_dir, file_list):
    """Changes to the local directory and uploads the specific list of files."""
    print(f"\nProcessing local directory: {local_dir}")
    try:
        os.chdir(local_dir)
    except FileNotFoundError:
        print(f"Error: Local directory '{local_dir}' not found. Skipping {len(file_list)} files.")
        return

    print(f"Found {len(file_list)} scheduled file(s) for this directory.")

    for file_name in file_list:
        if not os.path.exists(file_name):
            print(f"Warning: File '{file_name}' does not exist in {local_dir}. Skipping.")
            continue

        print(f"Uploading {file_name}...")
        try:
            with open(file_name, "rb") as file_obj:
                ftp.storbinary(f"STOR {file_name}", file_obj)
            print(f"Successfully uploaded {file_name}")
        except Exception as e:
            print(f"Failed to upload {file_name}. Error: {e}")


def main():
    # 1. Load the data using Pandas
    try:
        df = load_file_list(TSV_FILE_PATH)
    except Exception as e:
        print(f"Failed to read the tab-delimited file: {e}")
        return

    # 2. Connect and Login to FTP
    print(f"Connecting to {FTP_HOST}...")
    try:
        ftp = FTP(FTP_HOST)
        ftp.login(user=FTP_USER, passwd=FTP_PASS)
        print("Login successful.")

        # Enable passive mode for firewall compatibility
        ftp.set_pasv(True)

        # 3. Navigate to the Target Remote Directory
        print(f"Navigating to remote path...")
        ftp.cwd(REMOTE_DIR_1)
        ftp.cwd(REMOTE_DIR_2)
        print(f"Current remote directory set to: {ftp.pwd()}")

        # 4. Group by local folder and upload its explicit files
        grouped = df.groupby("folder_path")
        for folder, group in grouped:
            # Convert the 'file_name' column for this specific folder into a list
            files_to_upload = group["file_name"].tolist()
            upload_files_from_group(ftp, folder, files_to_upload)

        # 5. Clean up and close connection
        ftp.quit()
        print("\nAll transfers complete. Connection closed successfully.")

    except Exception as e:
        print(f"An FTP error occurred: {e}")


if __name__ == "__main__":
    main()