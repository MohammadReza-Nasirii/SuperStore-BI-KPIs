import kagglehub
import shutil
import os

path = kagglehub.dataset_download("vivek468/superstore-dataset-final")

print("Path to dataset files:", path)

source_file = os.path.join(path, "Sample - Superstore.csv")

dest_folder = "DataSet"
os.makedirs(dest_folder, exist_ok=True)

shutil.copy(source_file, dest_folder)

print("✅ Dataset copied to:", dest_folder)
