import numpy as np
from sklearn.preprocessing import StandardScaler
import numpy
def standardize_data(data):
  scaler = StandardScaler()
  scaled_data = scaler.fit_transform(data)
  return scaled_data

data = np.load("our_data.npy")
scaled_data = standardize_data(data)

print(scaled_data)

