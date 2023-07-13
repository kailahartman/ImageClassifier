import csv
import os
import pickle
local_path = r'C:\bootCamp\APPLIED'
def save_cifar10_to_csv(label_dir, image_dir, output_file):
    with open(label_dir, 'rb') as fo:
        data_dict = pickle.load(fo, encoding='bytes')

    labels = data_dict[b'labels']
    paths = []

    for file_name in os.listdir(image_dir):
        file_path = os.path.join(image_dir, file_name)
        print("file_path", file_path)
        if os.path.isfile(file_path):
            paths.append(file_path)

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(zip(labels, paths))  # Write the data rows


output_dir =os.getcwd()
for i in range(1, 6):
    label_dir = os.getcwd()+r'\\data\\cifar-10-batches-py\data_batch_'+str(i)
    image_dir = os.getcwd()+r'\\data\\output_images_'+str(i)
    output_file = os.path.join(output_dir, f'data\cifar10_data_batch_{i}.csv')

    save_cifar10_to_csv(label_dir, image_dir, output_file)
