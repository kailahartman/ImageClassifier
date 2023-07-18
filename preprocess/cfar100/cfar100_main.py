import numpy as np
import os
from cfar100_read_data import readCifar
from cfar100_save_images_locally import save_image_local
from cfar100_create_csv import save_cifar100_to_csv


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
    d={1:10,2:11,17:12}
    label= d[i]
    image_dir = os.getcwd()+r'\\data\\cifar100_class_'+str(i)
    output_file = os.path.join(output_dir, f'cifar100_class_{i}.csv')

    save_cifar100_to_csv(label, image_dir, output_file)