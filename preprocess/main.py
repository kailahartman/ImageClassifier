from preprocess.cfar10.cfar10_save_numpy_file import save_to_numpy_file
from normalization import standardize_data
import numpy as np
#reads the data
save_to_numpy_file()
data = np.load("data/cifar10.npy")
scaled_data = standardize_data(data)
