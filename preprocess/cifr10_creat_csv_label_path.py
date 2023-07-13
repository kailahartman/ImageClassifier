import csv
import os
import pickle
import re

local_path = r'C:\bootCamp\APPLIED'

def extract_label(string):
    pattern = r'label_(\d+).'
    match = re.search(pattern, string)
    if match:
        return int(match.group(1))
    else:
        return None

def save_cifar10_to_csv(image_dir, output_file):
    labels = []
    paths = []

    for file_name in os.listdir(image_dir):
        file_path = os.path.join(image_dir, file_name)
        if os.path.isfile(file_path):
            paths.append(file_path)
            label = extract_label(file_path)
            if label != None:
                labels.append(label)
            else:
                print("err", file_path)

    print("label: ", len(labels))
    print("path image: ", len(paths))

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(zip(labels, paths))  # Write the data rows


output_dir =os.getcwd()
for i in range(1, 6):
    image_dir = os.getcwd()+r'\\data\\output_images_'+str(i)
    output_file = os.path.join(output_dir, f'data\cifar10_data_batch_{i}.csv')

    save_cifar10_to_csv( image_dir, output_file)
