import numpy as np
import os
from preprocess.read_and_save_data.read_data import read_data
from preprocess.read_and_save_data.save_as_images_locally import save_image_local
from preprocess.read_and_save_data.save_to_numpy_file import save_as_numpy_file
from preprocess.read_and_save_data.write_to_csv import save_cifar_to_csv

def cfar100_read_save_locally_numpy_csv():
    file = os.getcwd()+r'\\data\\cifar-100-python\train'
    output_file = os.getcwd() + r'\\data\\cfar100'
    train_data = read_data(file)
    list_data = []
    list_lable = []
    for i in range(len(train_data[b'coarse_labels'])):
        if train_data[b'coarse_labels'][i] == 2 or train_data[b'coarse_labels'][i] == 1 or train_data[b'coarse_labels'][i] == 17:
            list_data.append(train_data[b'data'][i])
            list_lable.append(train_data[b'coarse_labels'][i])
    for i in range(len(list_lable)):
        d = {1: 10, 2: 11, 17: 12}
        list_lable[i] = d[list_lable[i]]

    save_as_numpy_file(output_file,list_lable,list_data)

    images = np.reshape(list_data, (len(list_data), 3, 32, 32))
    output_dir = os.getcwd()+r'\\data\\output_images_from_cifar100'
    image_format = 'png'

    # save_image_local(images, output_dir, image_format,list_lable)

    csv_output_dir = os.getcwd()+r'\\data'
    image_dir = os.getcwd()+r'\\data\\output_images_from_cifar100'
    output_file = os.path.join(csv_output_dir, f'cifar100.csv')

    # save_cifar100_to_csv(list_lable, image_dir, output_file)

    image_dir_cifar100 = os.path.join(os.getcwd(), "data", "output_images_from_cifar100")
    output_file_cifar100 = os.path.join(os.getcwd(), "data", "cifar100.csv")
    labels_cifar100 = [101, 102, 103, 104, 105]  # Replace with your CIFAR-100 labels

    save_cifar_to_csv(list_lable, image_dir_cifar100, output_file_cifar100, "cifar100")
