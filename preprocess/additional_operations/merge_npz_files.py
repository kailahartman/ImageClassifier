import os
import numpy as np
x = np.load(os.getcwd()+r'\\data\\cfar10.npz')
y = np.load(os.getcwd()+r'\\data\\cfar100.npz')
z=[*x, *y]
np.savez('data\merged_data.npz',z)