import numpy as np
import os
from preprocess.read_and_save_cifar_data.save_as_images_locally import save_image_local
from preprocess.read_and_save_cifar_data.save_to_numpy_file import save_as_numpy_file
from preprocess.read_and_save_cifar_data.write_to_csv import save_cifar_to_csv
from preprocess.additional_operations.down_sampling import create_images

def custom_images_read_save_locally_numpy_csv():
    print("custom------------------------------------------------------------:)")

    input_path = os.path.join(os.getcwd() ,"data", "our_data_umge from _google")
    output_path_downsamples_images=os.path.join(os.getcwd(),"data", "custom_images_downsampled")
    num_of_classes=10
    num_of_images_in_every_class=5

    labels=[i for i in range(1,num_of_classes+ 1) for _ in range(num_of_images_in_every_class)]
    images=create_images(input_path)
    images = np.reshape(images, (len(images), 3, 32, 32))

    print("save_as_numpy_file")
    print("tmp:::: ", images.shape)
    output_numpy_file = os.getcwd()+r'\\data\\custom_data'
    save_as_numpy_file(output_numpy_file,labels,images)

    print("save_image_local")
    save_image_local(images, output_path_downsamples_images, 'png', labels)

    print("save_cifar_to_csv")
    output_csv_path = os.path.join(os.getcwd(), "data", "custom_data.csv")
    save_cifar_to_csv(output_path_downsamples_images, output_csv_path, "custom data")
