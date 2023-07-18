
import numpy as np


def save_as_numpy_file(output_file, labels, data):
    print("images", len(data))
    train_data = np.vstack(data)
    train_labels = np.array(labels)

    print("images after", len(train_data))


    cifar_dict = {'images': train_data, 'labels': train_labels}
    np.savez(output_file, **cifar_dict)
