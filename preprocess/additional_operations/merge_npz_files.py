import os
import numpy as np
def merge():
    x = np.load(os.getcwd()+r'\\data\\cfar10.npz')
    y = np.load(os.getcwd()+r'\\data\\cfar100.npz')
    z = np.load(os.getcwd()+r'\\data\\custom_data.npz')  #rename the name of your file

    merge=[*x, *y, *z]
    np.savez('data\merged_data.npz',merge)

