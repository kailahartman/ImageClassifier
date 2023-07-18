import os
import csv
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


