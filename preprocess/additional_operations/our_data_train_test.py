import pandas as pd
import os
from sklearn.model_selection import train_test_split
import numpy as np
from preprocess.view.show_data import read_from_numpy_dict

def division(images,labels):
    print("dividing to train and test")

    X = images
    y = labels
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test


def save_as_numpy_file(output_file, data,name):
    # train_labels = np.array(labels)
    cifar_dict = {name: data}
    np.savez(output_file, **cifar_dict)


def save_numpy_file(parent_dir,images,labels):
    print("saving the train and test to a numpy file")
    X_train, X_test, y_train, y_test = division(images, labels)
    l = [X_train, X_test, y_train, y_test]
    names = ['X_train', 'X_test', 'y_train', 'y_test']
    for i in range(len(l)):
        file_path1 = os.path.join(os.getcwd(), 'data', names[i])
        save_as_numpy_file(file_path1, l[i], names[i])

def split_train_test():

    parent_dir = os.path.dirname(os.getcwd())
    file_path = os.path.join(os.getcwd(), 'data', 'merged_data.npz')
    images, labels = read_from_numpy_dict(file_path)
    save_numpy_file(parent_dir,images,labels)



