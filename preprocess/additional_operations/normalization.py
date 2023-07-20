import numpy as np
from sklearn.preprocessing import StandardScaler
def standardize_data(data):
    # Reshape the data array from 4 dimensions to 2 dimensions
    flattened_data = data.reshape(data.shape[0], -1)
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(flattened_data)
    return scaled_data


def scale_images_numpy_array():
    print("normalizing the merged npz file")
    data = np.load("data/merged_data.npz", allow_pickle=True)
    scaled_data = standardize_data(data['images'])
