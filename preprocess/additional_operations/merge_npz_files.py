import os
import numpy as np

def merge_npz_files():
    print("merging npz files")

    x = np.load(os.path.join(os.getcwd(), 'data', 'cfar10.npz'))
    y = np.load(os.path.join(os.getcwd(), 'data', 'cfar100.npz'))
    z = np.load(os.path.join(os.getcwd(), 'data', 'custom_data.npz'))  # Rename the name of your file

    x_images = x['images']
    x_labels = x['labels']

    y_images = y['images']
    y_labels = y['labels']

    z_images = z['images']
    z_labels = z['labels']

    print("x_images", x_images.shape)
    print("y_images", y_images.shape)
    print("z_images", z_images.shape)

    # Combine the images and labels from all datasets
    all_images = np.vstack([x_images, y_images, z_images])
    all_labels = np.concatenate([x_labels, y_labels, z_labels])

    # Shuffle the data randomly
    indices = np.random.permutation(all_images.shape[0])
    shuffled_images = all_images[indices]
    shuffled_labels = all_labels[indices]

    np.savez(os.path.join(os.getcwd(), 'data', 'merged_data.npz'), images=shuffled_images, labels=shuffled_labels)

