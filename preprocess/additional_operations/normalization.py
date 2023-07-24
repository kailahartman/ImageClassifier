import numpy as np
from preprocess.read_and_save_cifar_data.save_to_numpy_file import save_as_numpy_file

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

# Convert class vectors to binary class matrices. This is called one hot encoding.
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

def scale_images_numpy_array():
    print("normalizing the merged npz file")
    data = np.load("data/merged_data.npz", allow_pickle=True)
    scaled_data = standardize_data(data['images'])
    save_as_numpy_file(r"data/normalization", data['labels'], scaled_data)