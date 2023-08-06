# import numpy as np
# from tensorflow import  keras
# from preprocess.read_and_save_cifar_data.save_to_numpy_file import save_as_numpy_file
# def normilize_the_data(X_train,X_test,y_train,y_test):
#     x_train = X_train.astype('float32')
#     x_test = X_test.astype('float32')
#     x_train /= 255
#     x_test /= 255
#
#     # Convert class vectors to binary class matrices. This is called one hot encoding.
#     y_train = keras.utils.to_categorical(y_train, num_classes=13)
#     y_test = keras.utils.to_categorical(y_test, num_classes=13)
#
# def scale_images_numpy_array():
#     print("normalizing the merged npz file")
#     X_train = np.load("data/X_train.npz", allow_pickle=True)
#     y_train = np.load("data/y_train.npz", allow_pickle=True)
#     y_test = np.load("data/y_test.npz", allow_pickle=True)
#     X_test = np.load("data/X_test.npz", allow_pickle=True)
#
#     normilize_the_data(X_train,X_test,y_train,y_test)
