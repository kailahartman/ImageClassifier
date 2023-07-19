import numpy as np
import os
import matplotlib.pyplot as plt

def read_from_numpy_dict(file_path):
    cifar_data = np.load(file_path, allow_pickle=True)
    images = cifar_data['images']
    labels = cifar_data['labels']
    return images, labels


def show_images_with_labels(images, labels, figsize=(500, 500), fontsize=10):
    num_images = len(images)
    fig, axs = plt.subplots(1, num_images, figsize=figsize)

    for i in range(num_images):
        image = images[i].reshape(32, 32, 3)
        label = labels[i]

        axs[i].imshow(image)
        axs[i].axis('off')
        axs[i].set_title(f"Label: {label}", fontsize=fontsize, pad=8)

    plt.tight_layout()
    plt.show()

file_path = os.path.join(os.getcwd(), 'data', 'cifr10.npz')
images, labels = read_from_numpy_dict(file_path)
print("images:", len(images))
print("labels:", len(labels))

images = images[10:12]
labels = labels[10:12]

show_images_with_labels(images, labels)

