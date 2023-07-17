import numpy as np
import matplotlib.pyplot as plt
import csv
import os
import pickle


def read_cifar_100(file_path):
    with open(file_path, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict


def save_cifar100in_dict(cifr100_file_path,kind):
    kind=os.path.join(cifr100_file_path,kind)
    file_path = os.getcwd() +kind
    print(file_path)
    data = read_cifar_100(file_path)

    # flowers=2  fish=1 trees=17

    new_dict={2:[],1:[],17:[]}
    for i in range(len(data[b'coarse_labels'])):
        num=data[b'coarse_labels'][i]
        if(num==2 or num==1 or num==17):
            new_dict[num].append(data[b'data'][i])
    return new_dict

def save_the_pictures(cifar100Dict,output_dir_path,kind):
    for i in cifar100Dict.keys():
        data = cifar100Dict[i]
        images = np.reshape(data, (len(data), 3, 32, 32))
        output_dir = os.getcwd()+'\\' +output_dir_path
        image_format = 'png'
        if i==17:
            label = 12
        if(i==1):
            label = 10
        if(i==2):
            label = 11
        save_image_local(images, output_dir, image_format, label,kind)

def save_image_local(images, output_dir, image_format, label,kind):
    for j in range(len(images)):
        image = images[j]
        image = np.transpose(image, (1, 2, 0))
        image_name =  r'{}_{}_label_{}.{}'.format(j + 1,kind, label, image_format)
        print(output_dir)

        # plt.imshow(image)
        plt.axis('off')
        tmp = output_dir+r'\cifar_100_{}_images_{}\image{}'.format(kind,label,image_name)
        print(tmp)
        plt.savefig(tmp, bbox_inches='tight', pad_inches=0)
        plt.close()



def save_to_csv(cifar100Dict, output_dir_path, output_file_dir,kind):
    print("save_to_csv")
    for i in cifar100Dict.keys():
        d = {1: 10, 2: 11, 17: 12}
        label = d[i]
        image_dir = os.path.join(os.getcwd(), output_dir_path + str(label))
        output_file = os.path.join(output_file_dir, f'cifar100_class_{kind}_{label}.csv')
        save_cifar100_to_csv(label, image_dir, output_file)


def save_cifar100_to_csv(label, image_dir, output_file):
    labels = []
    paths = []

    for file_name in os.listdir(image_dir):
        file_path = os.path.join(image_dir, file_name)
        if os.path.isfile(file_path):
            paths.append(file_path)
            labels.append(label)

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['label', 'path'])  # Write the header
        writer.writerows(zip(labels, paths))  # Write the data rows





def cifar100_f():
    cifr100_file_path=r'\data\cifar_100\cifar-100-python'
    output_file_dir=r'\data\cifar_100'
    output_dir_path=r'\data\cifar_100'
    cifar100_dict_train=save_cifar100in_dict(cifr100_file_path,"train")
    save_the_pictures(cifar100_dict_train,output_dir_path,"train")
    save_to_csv(cifar100_dict_train,output_dir_path,output_file_dir,"train")

    cifar100_dict_test=save_cifar100in_dict(cifr100_file_path,"test")
    save_the_pictures(cifar100_dict_test,output_dir_path,"test")
    save_to_csv(cifar100_dict_test,output_dir_path,output_file_dir,"test")



    # file_path = r'C:\bootCamp\APPLIED\AppliedProject\preprocess\data\cifr100\cifar-100-python\train'
    # train_data = read_cifar_100(file_path)
    # file_path1=r'C:\bootCamp\APPLIED\AppliedProject\preprocess\data\cifr100\cifar-100-python\meta'
    # meta= read_cifar_100(file_path1)
    # for i in range(2500):
    #     print(train_data[b'coarse_labels'][i])
    #     print(meta[ b'coarse_label_names'][train_data[b'coarse_labels'][i]])
    #     print("=================================")
cifar100_f()


