import numpy as np
import os

#

def read_cifar10_from_numpy_dict(file_path):
    cifar_data = np.load(file_path, allow_pickle=True)
    images = cifar_data['images']
    labels = cifar_data['labels']
    return images, labels

file_path = os.path.join(os.getcwd(), 'data\our data', 'our_data.npz')
images, labels = read_cifar10_from_numpy_dict(file_path)
print("images:", images)
print("labels:", labels)

