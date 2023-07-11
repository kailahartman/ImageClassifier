import pickle
import numpy as np
import matplotlib.pyplot as plt

def reed_data(file):
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
        image_name = 'image_{}_label_{}.{}'.format(j + 1, label, image_format)
        output_path = output_dir + '\\' + image_name

        plt.imshow(image)
        plt.axis('off')
        plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
        plt.close()

path = r'C:\bootCamp\APPLIED\cifar-10-batches-py\\data_batch_'
for i in range(1, 6):
    data_dict = reed_data(path + str(i))
    data = data_dict[b'data']
    labels = data_dict[b'labels']
    images = np.reshape(data, (len(data), 3, 32, 32))
    output_dir = r'C:\bootCamp\APPLIED\output_images_' + str(i)
    image_format = 'png'
    save_image_local(images, output_dir, image_format)






