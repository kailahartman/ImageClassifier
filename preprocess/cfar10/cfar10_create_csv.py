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

def save_cifar10_to_csv(image_dir, output_file):
    labels = []
    paths = []

    for file_name in os.listdir(image_dir):
        file_path = os.path.join(image_dir, file_name)
        if os.path.isfile(file_path):
            paths.append(file_path)
            label = extract_label(file_path)
            if label is not None:
                labels.append(label)
            else:
                print("err", file_path)

    print("label: ", len(labels))
    print("path image: ", len(paths))

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(['label', 'path', 'source'])

        # Write the data rows
        writer.writerows(zip(labels, paths, ['cifar10'] * len(labels)))


