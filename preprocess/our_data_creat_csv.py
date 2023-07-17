import csv
import os


def save_our_data_to_csv  (image_dir, output_file):
    labels = []
    paths = []
    for i in range(0,10):
        for j in range(5):
            labels.append(i)

    for file_name in os.listdir(image_dir):
        paths.append(os.path.join(image_dir, file_name))

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(zip(labels, paths))  # Write the data rows


output_file_path = os.getcwd()+r'\\data\\our_data.csv'
image_dir = os.getcwd()+r'\\data\\our_data'
save_our_data_to_csv(image_dir, output_file_path)