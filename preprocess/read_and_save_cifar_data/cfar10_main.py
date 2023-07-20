import numpy as np
import os
from read_and_save_cifar_data.read_data import read_data
from read_and_save_cifar_data.save_as_images_locally import save_image_local
from read_and_save_cifar_data.save_to_numpy_file import save_as_numpy_file
from read_and_save_cifar_data.write_to_csv import save_cifar_to_csv
def cfar10_read_save_locally_numpy_csv():
    path = os.getcwd()+r'\\data\\cifar-10-batches-py\\data_batch_'
    output_file = os.getcwd() + r'\\data\\cfar10'
    train_data, train_labels = [], []
    for i in range(1, 6):
        data_dict = read_data(path + str(i))
        for j in data_dict[b'data']:
            train_data.append(j)
        train_labels.extend(data_dict[b'labels'])

    images = np.reshape(train_data, (len(train_data), 3, 32, 32))

    save_as_numpy_file(output_file, train_labels, images)

    image_dir = os.path.join(os.getcwd(), "data", "output_images_from_cifar10")
    image_format = 'png'
    # train_data = np.vstack(train_data)
    save_image_local(images, image_dir, image_format, train_labels)

    output_file_cifar10 = os.path.join(os.getcwd(), "data", "cifar10.csv")
    save_cifar_to_csv(image_dir, output_file_cifar10, "cifar10")
