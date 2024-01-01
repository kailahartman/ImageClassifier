from PIL import Image
import numpy as np
import os

def down_sampling(load_path):
    image = Image.open(load_path).convert('RGB')
    resized_image = image.resize((32, 32), Image.LANCZOS)
    resized_image=np.transpose(resized_image, (2, 0, 1))
    return resized_image

# def extract_number(filename):
#     return int(''.join(filter(str.isdigit, filename)))

def create_images(folder_load_path):
    images = []
    sorted_file_list = sorted(os.listdir(folder_load_path), key=extract_number)
    for file_name in sorted_file_list:
        load_path = os.path.join(folder_load_path, file_name)
        resized_image = down_sampling(load_path)
        images.append(resized_image)
    return images


