import numpy as np
import os
from preprocess.read_and_save_data.read_data import read_data
from preprocess.read_and_save_data.save_as_images_locally import save_image_local
from preprocess.read_and_save_data.save_to_numpy_file import save_as_numpy_file
# from cfar100_create_csv import save_cifar100_to_csv

def cfar100_read_save_locally_numpy_csv():
    file = os.getcwd()+r'\\data\\cifar-100-python\train'
    output_file = os.getcwd() + r'\\data\\cfar100'

    train_data = read_data(file)
    list_data = []
    list_lable = []
    for i in range(len(train_data[b'coarse_labels'])):
        if train_data[b'coarse_labels'][i] == 2 or train_data[b'coarse_labels'][i] == 1 or train_data[b'coarse_labels'][i] == 17:
            list_data.append(train_data[b'data'][i])
            list_lable.append(train_data[b'coarse_labels'][i])
    save_as_numpy_file(output_file,list_lable,list_data)
    # flowers=2  fish=1 people=14
    #new_dict={2:[],1:[],17:[]}
    # for i in range(0,len(train_data[b'coarse_labels'])):
    #     num=train_data[b'coarse_labels'][i]
    #     if(num==2 or num==1 or num==17):
    #         new_dict[num].append(train_data[b'data'][i])
    # for i in new_dict.keys():
    #     data = new_dict[i]
    #     labels = [i]*len(new_dict[i])
    images = np.reshape(list_data, (len(list_data), 3, 32, 32))
    output_dir = os.getcwd()+r'\\data\\output_images_from_cifar100'
    image_format = 'png'
    save_image_local(list_data, output_dir, image_format,list_lable)
    #
    #
    # output_dir = os.getcwd()+r'\\data'
    # for i in new_dict.keys():
    #     d={1:10,2:11,17:12}
    #     label= d[i]
    #     image_dir = os.getcwd()+r'\\data\\cifar100_class_'+str(i)
    #     output_file = os.path.join(output_dir, f'cifar100_class_{i}.csv')
    #
    #     #save_cifar100_to_csv(label, image_dir, output_file)