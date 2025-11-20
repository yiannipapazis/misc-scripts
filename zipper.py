import zipfile
import os

def zip_files(file_paths, zip_name):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file_path in file_paths:
            if os.path.isfile(file_path):
                # Add file to zip, using only the filename (not full path)
                zipf.write(file_path, os.path.basename(file_path))
            else:
                print(f"Warning: {file_path} does not exist and will be skipped.")
    print(f"Files zipped into {zip_name}")

def zip_files_with_structure(file_paths, zip_name, root_folder):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file_path in file_paths:
            if os.path.isfile(file_path):
                # Preserve folder structure relative to root_folder
                arcname = os.path.relpath(file_path, start=root_folder)
                zipf.write(file_path, arcname=arcname)
            else:
                print(f"Warning: {file_path} does not exist and will be skipped.")
    print(f"Files zipped into {zip_name} with folder structure preserved")
