import numpy as np

def save_as_numpy_file(output_file, labels, data):
    print("saving the data to a numpy file")

    train_labels = np.array(labels)
    images = []
    for i in range(len(data)):
        image = data[i]
        image = np.transpose(image, (1, 2, 0))
        images.append(image)
    cifar_dict = {'images': data, 'labels': train_labels}
    np.savez(output_file, **cifar_dict)
