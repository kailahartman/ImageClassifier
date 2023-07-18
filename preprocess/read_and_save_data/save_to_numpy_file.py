
import numpy as np

def save_as_numpy_file(output_file, labels, data):
    train_labels = np.array(labels)
    cifar_dict = {'images': data, 'labels': train_labels}
    np.savez(output_file, **cifar_dict)
