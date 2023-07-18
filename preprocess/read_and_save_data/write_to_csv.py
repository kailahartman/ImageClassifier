import csv
import os
import re

def extract_label(string):
    pattern = r'label_(\d+).'
    match = re.search(pattern, string)
    if match:
        return int(match.group(1))
    else:
        return None

def save_cifar_to_csv(labels, image_dir, output_file, dataset_name):
    paths = []

    for file_name in os.listdir(image_dir):
        file_path = os.path.join(image_dir, file_name)
        if os.path.isfile(file_path):
            paths.append(file_path)

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['label', 'path', 'source'])  # Write the header
        writer.writerows(zip(labels, paths, [dataset_name] * len(labels)))  # Write the data rows