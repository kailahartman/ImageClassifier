# # import csv
# # import matplotlib.pyplot as plt
# # import matplotlib.image as mpimg
# #
# # def display_images_from_csv(csv_file):
# #     with open(csv_file, 'r') as csvfile:
# #         reader = csv.reader(csvfile)
# #         header = next(reader)  # Skip the header row
# #         label_index = header.index('label')
# #         path_index = header.index('path')
# #
# #         for row in reader:
# #             label = row[label_index]
# #             path = row[path_index]
# #             print("pppppp", path);
# #             image = mpimg.imread(path)
# #             plt.imshow(image)
# #             plt.title(f'Label: {label}')
# #             plt.axis('off')
# #             plt.show()
# #
# # csv_file = r'C:\bootCamp\APPLIED\cifar10_data.csv'  # Path to the CSV file
# #
# # display_images_from_csv(csv_file)
#
# import csv
# import os
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
#
# def display_images_from_csv(csv_file):
#     with open(csv_file, 'r') as csvfile:
#         reader = csv.reader(csvfile)
#         header = next(reader)  # Skip the header row
#         label_index = header.index('label')
#         path_index = header.index('path')
#
#         for row in reader:
#             label = row[label_index]
#             path = row[path_index]
#
#             # Handle the absolute file path correctly
#             abs_path = os.path.abspath(path)
#
#             image = mpimg.imread(abs_path)
#             plt.imshow(image)
#             plt.title(f'Label: {label}')
#             plt.axis('off')
#             plt.show()
#
# csv_file =  r'C:\bootCamp\APPLIED\cifar10_data.csv'  # Path to the CSV file
#
# display_images_from_csv(csv_file)
#
import csv
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def display_images_from_csv(csv_file):
    with open(csv_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Skip the header row
        label_index = header.index('label')
        path_index = header.index('path')

        for row in reader:
            label = row[label_index]
            path = row[path_index]

            image = mpimg.imread(path)
            plt.imshow(image)
            plt.title(f'Label: {label}')
            plt.axis('off')
            plt.show()

csv_file = r'C:\bootCamp\APPLIED\AppliedProject\cifar10_data.csv'  # Path to the CSV file

display_images_from_csv(csv_file)
