import numpy as np
import os
from preprocess.read_and_save_cifar_data.read_data import read_data
from preprocess.read_and_save_cifar_data.save_as_images_locally import save_image_local
from preprocess.read_and_save_cifar_data.save_to_numpy_file import save_as_numpy_file
from preprocess.read_and_save_cifar_data.write_to_csv import save_cifar_to_csv
from preprocess.additional_operations.image_rotation import rotate_image

def cfar100_read_save_locally_numpy_csv():
    print("cifar100----------------------------------------------------:-)")

    file = os.getcwd()+r'\\data\\cifar-100-python\train'
    output_file = os.getcwd() + r'\\data\\cfar100'
    train_data = read_data(file)
    list_data = []
    list_lable = []
    for i in range(len(train_data[b'coarse_labels'])):
        if train_data[b'coarse_labels'][i] == 2 or train_data[b'coarse_labels'][i] == 1 or train_data[b'coarse_labels'][i] == 17:
            list_data.append(train_data[b'data'][i])
            j= train_data[b'data'][i]
            print(j)
            rotated_image = rotate_image(j, 90)
            list_data.append(rotated_image)
            list_lable.append(train_data[b'coarse_labels'][i])
            list_lable.append(train_data[b'coarse_labels'][i])
    for i in range(len(list_lable)):
        d = {1: 10, 2: 11, 17: 12}
        list_lable[i] = d[list_lable[i]]


    images = np.reshape(list_data, (len(list_data), 3, 32, 32))

    save_as_numpy_file(output_file,list_lable,images)

    # images = np.reshape(list_data, (len(list_data), 3, 32, 32))
    image_dir = os.getcwd()+r'\\data\\output_images_from_cifar100'
    image_format = 'png'

    save_image_local(images, image_dir, image_format,list_lable)

    image_dir_cifar100 = os.path.join(os.getcwd(), "data", "output_images_from_cifar100")
    output_file_cifar100 = os.path.join(os.getcwd(), "data", "cifar100.csv")

    save_cifar_to_csv(image_dir_cifar100, output_file_cifar100, "cifar100")
