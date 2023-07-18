import pickle
import numpy as np
import os

def save_cifar100_as_numpy_dict(data_dir, output_file):
    train_data, train_labels = [], []
    with open(data_dir, 'rb') as f:
        data = pickle.load(f, encoding='bytes')
    list_data=[]
    list_lable=[]
    for i in range(len(data[b'coarse_labels'])):
        if data[b'coarse_labels'][i]==2 or data[b'coarse_labels'][i]==1 or data[b'coarse_labels'][i]==17:
            list_data.append(data[b'data'][i])
            list_lable.append(data[b'coarse_labels'][i])
    train_data.append(list_data)
    train_labels.extend(list_lable)

    train_data = np.vstack(train_data)
    train_labels = np.array(train_labels)
    cifar_dict = {'images': train_data, 'labels': train_labels}

    np.savez(output_file, **cifar_dict)


path = os.getcwd()+r'\\data\\cifar_100\\cifar-100-python\\train'  #your path
output_file = os.getcwd() + r'\\data\\cifar_100\\cifar100_train'
save_cifar100_as_numpy_dict(path, output_file)
path1 = os.getcwd()+r'\\data\\cifar_100\\cifar-100-python\\test'  #your path
output_file1 = os.getcwd() + r'\\data\\cifar_100\\cifar100_test'
save_cifar100_as_numpy_dict(path1,output_file1)