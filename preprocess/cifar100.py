import numpy as np
import matplotlib.pyplot as plt
import csv
import os
import pickle


def readCifar(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict


def save_cifar100_to_csv(label, image_dir, output_file):
    labels = []
    for i in range(2500):
        labels.append(label)
    paths = []

    for file_name in os.listdir(image_dir):
        file_path = os.path.join(image_dir, file_name)
        if os.path.isfile(file_path):
            paths.append(file_path)

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['label', 'path','source'])  # Write the header
        writer.writerows(zip(labels, paths,['cifar100']*len(labels)))  # Write the data rows



def save_image_local(images, output_dir, image_format):
    fig, axes = plt.subplots(2, 5, figsize=(12, 6))
    axes = axes.ravel()
    for j in range(len(images)):
        image = images[j]
        image = np.transpose(image, (1, 2, 0))

        image_name = r'image_{}_.{}'.format(j + 1, image_format)
        output_path = output_dir + '\\' + image_name

        plt.imshow(image)
        plt.axis('off')
        plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
        plt.close()


file = os.getcwd()+r'\\data\\cifar-100-python\train'
train_data = readCifar(file)



# flowers=2  fish=1 people=14

new_dict={2:[],1:[],17:[]}
for i in range(0,len(train_data[b'coarse_labels'])):
    num=train_data[b'coarse_labels'][i]
    if(num==2 or num==1 or num==17):
        new_dict[num].append(train_data[b'data'][i])
for i in new_dict.keys():
    data = new_dict[i]
    labels = i
    images = np.reshape(data, (len(data), 3, 32, 32))
    output_dir = os.getcwd()+r'\\data\\cifar100_class_' + str(i)
    image_format = 'png'
    save_image_local(images, output_dir, image_format)


output_dir = os.getcwd()+r'\\data'
for i in new_dict.keys():
    d={1:9,2:10,17:11}
    label= d[i]
    image_dir = os.getcwd()+r'\\data\\cifar100_class_'+str(i)
    output_file = os.path.join(output_dir, f'cifar100_class_{i}.csv')

    save_cifar100_to_csv(label, image_dir, output_file)