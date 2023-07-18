import pickle
import numpy as np
import os

def save_cifar10_as_numpy_dict(data_dir, output_file):
    train_data, train_labels = [], []
    with open(data_dir, 'rb') as f:
        data = pickle.load(f, encoding='bytes')
        train_data.append(data[b'data'])
        train_labels.extend(data[b'coarse_labels'])

    train_data = np.vstack(train_data)
    train_labels = np.array(train_labels)
    cifar_dict = {'images': train_data, 'labels': train_labels}

    np.savez(output_file, **cifar_dict)


path = os.getcwd()+r'\\data\\cifar_100\\cifar-100-python\\train'  #your path
output_file = os.getcwd() + r'\\data\\cifar_100\\cifar100_train'
# save_cifar10_as_numpy_dict(path, output_file)
path1 = os.getcwd()+r'\\data\\cifar_100\\cifar-100-python\\test'  #your path
output_file1 = os.getcwd() + r'\\data\\cifar_100\\cifar100_test'
save_cifar10_as_numpy_dict(path1,output_file1)