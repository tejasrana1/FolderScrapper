# %%
import json
from pathlib import Path
import shutil
import argparse

# %%
config_path = "config.json"
def load_config(config_path):
    with open(config_path, 'r') as f:
        return json.load(f)

# %%
def get_folder_for_extension(ext,config):
    for folder,extension in config.items():
        if ext in extension:
            return folder
    return "Others"

# %%
def organise_files(folder_path, config_path):
    folder = Path(folder_path)
    if not folder.exists():
        print("Folder does not exist!")
        return
    config = load_config(config_path)
    for file in folder.iterdir():
        if file.is_file():
            ext = file.suffix.lower().strip(".") or "no_extension"
            target_folder_name = get_folder_for_extension(ext,config)
            target_folder = folder / target_folder_name
            target_folder.mkdir(exist_ok=True)
            shutil.move(str(file), target_folder / file.name)
            print(f"Moved: {file.name} -> {target_folder_name}/")
    print("Organization complete.")

# %%
def get_arguments():
    parser = argparse.ArgumentParser(description="Organize files into folders based on file extension")
    parser.add_argument("-f", "--folder", type=str, default="T:\Downloads", help="Path to the folder to organize")
    parser.add_argument("-c", "--config", type=str, default="config.json", help="Path to the config JSON file")
    return parser.parse_args()

# %%
if __name__ == "__main__":
    args = get_arguments()
    organise_files(args.folder,args.config)

# %%



