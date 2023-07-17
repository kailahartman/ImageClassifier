import pickle
import numpy as np
import os
import matplotlib.image
def reed_data(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

def save_image_local(images, output_dir, image_format, labels):
    for j in range(len(images)):
        label = labels[j]
        image_name = r'image_{}_label_{}.{}'.format(j + 1, label, image_format)
        output_path = output_dir + '\\' + image_name
        matplotlib.image.imsave(output_path, image)



def cifr10_reed_save_f(output_dir_path, cifr_path):
    path = os.getcwd()+cifr_path  #your path
    for i in range(1, 6):
        data_dict = reed_data(path + str(i))
        data = data_dict[b'data']
        labels = data_dict[b'labels']
        images = np.reshape(data, (len(data), 3, 32, 32))
        output_dir = os.getcwd()+output_dir_path + str(i) #your path
        image_format = 'png'
        save_image_local(images, output_dir, image_format, labels)





