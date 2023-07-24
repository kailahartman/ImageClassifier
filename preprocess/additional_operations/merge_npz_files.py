# import os
# import numpy as np
#
# def merge_npz_files ():
#
#     x = np.load(os.getcwd() + r'\\data\\cfar10.npz')
#     y = np.load(os.getcwd() + r'\\data\\cfar100.npz')
#     z = np.load(os.getcwd() + r'\\data\\custom_data.npz')  # rename the name of your file
#
#     merge = [*x, *y, *z]
#     print(merge)
#     np.savez('data\merged_data.npz', merge)
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

    merged_images = np.vstack([x_images, y_images, z_images])
    merged_labels = np.concatenate([x_labels, y_labels, z_labels])
    np.savez(os.path.join(os.getcwd(), 'data', 'merged_data.npz'), images=merged_images, labels=merged_labels)


