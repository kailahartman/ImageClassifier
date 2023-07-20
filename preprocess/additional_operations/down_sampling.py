from PIL import Image
import os
import numpy as np
from PIL import Image
import numpy as np
import os

def down_sampling(load_path):
    image = Image.open(load_path).convert('RGB')  # Convert image to RGB mode
    resized_image = image.resize((32, 32), Image.LANCZOS)
    return resized_image

def create_images(folder_load_path):
    print("downsampling our data")

    images = []
    for file_name in os.listdir(folder_load_path):
        load_path = os.path.join(folder_load_path, file_name)
        resized_image = down_sampling(load_path)
        resized_image = np.transpose(resized_image, (2, 0, 1 ))

        images.append(np.array(resized_image))
    return images
