import zipfile
import os

def unzip_file(zip_file_path, extract_to_directory):
    os.makedirs(extract_to_directory, exist_ok=True)
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to_directory)
    print(f"Extracted all files to {extract_to_directory}")

# Example usage
unzip_file('/workspaces/codespaces-blank/Python_DSA/Resorces Code/8.+Trees+_+Generic.zip', '/workspaces/codespaces-blank/Python_DSA')
