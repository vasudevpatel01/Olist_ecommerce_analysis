import os
import zipfile

# Path to zip folder
zip_path = r"C:\Users\SHWETA\Downloads\Olist_Ecommerce.zip"

# Path to the data folder in project
data_folder = "data"

# Creates 'data' folder if it doesn't exist
if not os.path.exists(data_folder):
    os.makedirs(data_folder)
    print(f"Created folder '{data_folder}'")

# Extract all files from the zip into the data folder
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(data_folder)

print(f"All files from '{zip_path}' have been extracted into '{data_folder}'")
