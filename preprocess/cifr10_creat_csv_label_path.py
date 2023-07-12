import csv
import os
import pickle

def save_cifar10_to_csv(label_dir, image_dir, output_file):
    with open(label_dir, 'rb') as fo:
        data_dict = pickle.load(fo, encoding='bytes')

    labels = data_dict[b'labels']
    paths = []

    for file_name in os.listdir(image_dir):
        file_path = os.path.join(image_dir, file_name)
        if os.path.isfile(file_path):
            paths.append(file_path)

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['label', 'path'])  # Write the header
        writer.writerows(zip(labels, paths))  # Write the data rows


output_dir = r'C:\Users\אתי\Documents\BOOTCAMP\Project'
for i in range(1, 6):
    label_dir = r'C:\Users\אתי\Documents\BOOTCAMP\cifar-10-batches-py\data_batch_'+str(i)
    image_dir = r'C:\Users\אתי\Documents\BOOTCAMP\Project\output_images_1'
    output_file = os.path.join(output_dir, f'cifar10_data_batch_{i}.csv')

    save_cifar10_to_csv(label_dir, image_dir, output_file)
