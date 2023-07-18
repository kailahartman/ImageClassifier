import numpy as np
import os
from preprocess.read_and_save_data.read_data import read_data
from preprocess.read_and_save_data.save_as_images_locally import save_image_local
from preprocess.read_and_save_data.save_to_numpy_file import save_as_numpy_file
def cfar10_read_save_locally_numpy_csv():
    path = os.getcwd()+r'\\data\\cifar-10-batches-py\\data_batch_'
    output_file = os.getcwd() + r'\\data\\cfar10'
    train_data, train_labels = [], []
    for i in range(1, 6):
        data_dict = read_data(path + str(i))
        data = data_dict[b'data']
        labels = data_dict[b'labels']
        train_data.append(data_dict[b'data'])
        train_labels.extend(data_dict[b'labels'])
        images = np.reshape(data, (len(data), 3, 32, 32))
        output_dir = os.getcwd() + r'\\data\\output_images_' + str(i)
        image_format = 'png'
        save_image_local(images, output_dir, image_format, labels)
    save_as_numpy_file(output_file, train_labels, train_data)