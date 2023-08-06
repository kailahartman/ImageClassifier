
from read_and_save_cifar_data.cfar10_main import cfar10_read_save_locally_numpy_csv
from read_and_save_cifar_data.cfar100_main import cfar100_read_save_locally_numpy_csv
from read_and_save_cifar_data.custom_images_main import custom_images_read_save_locally_numpy_csv
from additional_operations.merge_npz_files import merge_npz_files
from additional_operations.combine_csv_files import combine_csv_files
# from additional_operations.normalization import scale_images_numpy_array
from additional_operations.our_data_train_test import split_train_test
from visualize.show_data import show_data_main
import os
if __name__ == '__main__':

    cfar10_read_save_locally_numpy_csv()
    cfar100_read_save_locally_numpy_csv()
    custom_images_read_save_locally_numpy_csv()
    combine_csv_files()
    #
    merge_npz_files()
    split_train_test()
    # scale_images_numpy_array()
    # split_train_test()

    show_data_main()
