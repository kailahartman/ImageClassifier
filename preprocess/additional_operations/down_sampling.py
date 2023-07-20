from PIL import Image
import numpy as np
import os

def down_sampling(load_path):
    image = Image.open(load_path).convert('RGB')  # Convert image to RGB mode
    resized_image = image.resize((32, 32), Image.LANCZOS)
    return resized_image

def create_images(folder_load_path):
    images = []
    for file_name in os.listdir(folder_load_path):
        load_path = os.path.join(folder_load_path, file_name)
        resized_image = down_sampling(load_path)
        images.append(resized_image)
    return images


