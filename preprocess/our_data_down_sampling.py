from PIL import Image
import os

def down_sampling(load_path, save_path):
    image = Image.open(load_path)
    resized_image = image.resize((32, 32), Image.LANCZOS)
    resized_image.save(save_path)

folder_load_path = os.getcwd()+"data/our_data_umge from _google" # change to your path
folder_save_path = os.getcwd()+"data/our_data_downsampled"
for file_name in os.listdir(folder_load_path):
    load_path = os.path.join(folder_load_path, file_name)
    save_path = os.path.join(folder_save_path, file_name)
    down_sampling(load_path, save_path)

