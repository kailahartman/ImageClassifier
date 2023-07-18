import numpy as np
import os
from preprocess.cfar10.cfar10_read_data import read_data
from preprocess.cfar10.cfar10_save_as_images_locally import save_image_local
def save_to_numpy_file(path,images):
    np.savez(path,images)

