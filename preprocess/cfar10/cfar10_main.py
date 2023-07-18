import numpy as np
import os
from preprocess.cfar10.cfar10_read_data import read_data
from preprocess.cfar10.cfar10_save_as_images_locally import save_image_local
from cfar10_save_numpy_file import save_to_numpy_file
def cfar10_read_save_locally_numpy_csv():
    path = os.getcwd()+r'\\data\\cifar-10-batches-py\\data_batch_'
    for i in range(1, 6):
        data_dict = read_data(path + str(i))
        data = data_dict[b'data']
        labels = data_dict[b'labels']
        images = np.reshape(data, (len(data), 3, 32, 32))
        save_to_numpy_file('data/cifar10',images)
        output_dir = os.getcwd() + r'\\data\\output_images_' + str(i)
        image_format = 'png'
        save_image_local(images, output_dir, image_format, labels)