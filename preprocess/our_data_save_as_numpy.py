import os
import numpy as np
def create_labels(num_classes, num_samples):
    labels = []
    for i in range(num_classes):
        for j in range(num_samples):
            labels.append(i)
    return labels


def save_as_numpy(images):
    folder_load_path = os.getcwd()+"\\data\\our data\\our_data_umge from _google" # change to your path
    folder_save_path = os.getcwd()+"\\data\\our data"

    num_classes = 10
    num_samples = 5

    labels = create_labels(num_classes, num_samples)
    print("labels", len(labels))
    print("images", len(images))
    labels_data = np.array(labels)
    images_data = np.vstack(images)

    our_data_dict = {'images': images_data, 'labels': labels_data}
    np.savez(folder_save_path, **our_data_dict)