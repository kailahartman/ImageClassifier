import numpy as np
import os
from read_and_save_cifar_data.read_data import read_data
from read_and_save_cifar_data.save_as_images_locally import save_image_local
from read_and_save_cifar_data.save_to_numpy_file import save_as_numpy_file
from read_and_save_cifar_data.write_to_csv import save_cifar_to_csv

def cfar100_read_save_locally_numpy_csv():
    print("cifar100----------------------------------------------------:-)")

    chosen_label_list = [1, 2, 17]
    convert_label_dict = {1: 10, 2: 11, 17: 12}

    file_pickle_train = os.getcwd()+r'\\data\\cifar-100-python\train'
    file_pickle_test = os.getcwd()+r'\\data\\cifar-100-python\test'
    output_file_npz = os.getcwd() + r'\\data\\cfar100'
    train_data = read_data(file_pickle_train)
    test_data = read_data(file_pickle_test)
    list_data = []
    list_label = []
    for img, lbl in zip(train_data[b'data'], train_data[b'coarse_labels']):
        if lbl in chosen_label_list:
            list_data.append(img)
            list_label.append(lbl)

    for img, lbl in zip(test_data[b'data'], test_data[b'coarse_labels']):
        if lbl in chosen_label_list:
            list_data.append(img)
            list_label.append(lbl)

    for i, lbl in enumerate(list_label):
        list_label[i] = convert_label_dict[lbl]

    images = np.reshape(list_data, (len(list_data), 3, 32, 32))

    save_as_numpy_file(output_file_npz,list_label,images)

    images = np.reshape(list_data, (len(list_data), 3, 32, 32))
    images_output_folder = os.getcwd()+r'\\data\\output_images_from_cifar100'
    image_format = 'png'
    save_image_local(images, images_output_folder, image_format,list_label)

    image_dir_cifar100 = os.path.join(os.getcwd(), "data", "output_images_from_cifar100")
    output_file_cifar100 = os.path.join(os.getcwd(), "data", "cifar100.csv")

    save_cifar_to_csv(image_dir_cifar100, output_file_cifar100, "cifar100")
