import csv

import os
def save_our_data_to_csv(image_dir, output_file):
    labels = []
    paths = []
    for i in range(0, 10):
        for j in range(5):
            labels.append(i)
    for file_name in os.listdir(image_dir):
        paths.append(os.path.join(image_dir, file_name))
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['label', 'path', 'source'])
        writer.writerows(zip(labels, paths, ['our data'] * len(labels)))  # Write the data rows

def create():
    output_file_path = os.path.join(os.getcwd(), 'data', 'our_data.csv')
    image_dir = os.path.join(os.getcwd(), 'data', 'our_data_image from _google')
    save_our_data_to_csv(image_dir, output_file_path)









