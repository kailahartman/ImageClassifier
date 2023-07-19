
from preprocess.our_data.our_data_creat_csv import create
from preprocess.our_data.our_data_down_sampling import downsampling
from preprocess.our_data.our_data_save_as_numpy import save_as_numpy
def main():
    create()
    images = downsampling()
    save_as_numpy(images)