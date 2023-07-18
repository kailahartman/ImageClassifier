
import pickle
import numpy as np
import os

# def save_to_numpy_file(path,images):
#     np.savez(path,images)
#


def save_cifar10_as_numpy_dict(data_dir, output_file):
    train_data, train_labels = [], []
    for i in range(1, 6):
        file_path = os.path.join(data_dir, f'data_batch_{i}')
        with open(file_path, 'rb') as f:
            data = pickle.load(f, encoding='bytes')
            train_data.append(data[b'data'])
            train_labels.extend(data[b'labels'])


    #print("images", len(train_data))
    train_data = np.vstack(train_data)
    train_labels = np.array(train_labels)
    cifar_dict = {'images': train_data, 'labels': train_labels}

    np.savez(output_file, **cifar_dict)


path = os.getcwd()+r'\\data\\cifr10\\cifar-10-batches-py'  #your path
output_file = os.getcwd() + r'\\data\\cifr10\\'
save_cifar10_as_numpy_dict(path, output_file)