import pickle
import numpy as np
import matplotlib.pyplot as plt
from dotenv import dotenv_values
env_vars = dotenv_values('.env')
# file_path = env_vars['FILE_PATH']
def read_data(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

def save_image_local(images, output_dir, image_format):
    fig, axes = plt.subplots(2, 5, figsize=(12, 6))
    axes = axes.ravel()
    for j in range(len(images)):
        image = images[j]
        image = np.transpose(image, (1, 2, 0))

        label = labels[j]
        image_name = r'image_{}_label_{}.{}'.format(j + 1, label, image_format)
        output_path = output_dir + '\\' + image_name

        plt.imshow(image)
        plt.axis('off')
        plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
        plt.close()

path = r'F:\cifar-10-batches-py\\data_batch_'
# path = file_path+r'\cifar-10-batches-py\\data_batch_'
for i in range(1, 6):
    data_dict = read_data(path + str(i))
    data = data_dict[b'data']
    labels = data_dict[b'labels']
    images = np.reshape(data, (len(data), 3, 32, 32))
    output_dir = r'F:\output_images_' + str(i)
    # output_dir = file_path+r'\output_images_' + str(i)
    image_format = 'png'
    save_image_local(images, output_dir, image_format)






