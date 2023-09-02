import numpy as np
import pandas as pd
import random
import cv2
import logging
from datetime import datetime


def rotate_image(image_array: np.array, angle: float) -> np.array:
    """
    Rotate an image in form of numpy array
    :param image_array: Image to rotate of type numpy array
    :param angle: The angle of rotation
    :return: The rotated image of type numpy array.
    """
    image_array = np.reshape(image_array,(3,32,32))
    image = image_array.copy()
    height, width = image.shape[:2]
    diagonal = np.sqrt(height ** 2 + width ** 2)
    padding = int((diagonal - min(height, width)) / 2)

    # Add padding to the image using BORDER_REFLECT or BORDER_REPLICATE mode
    padded_image = cv2.copyMakeBorder(image, padding, padding, padding, padding, cv2.BORDER_REFLECT)

    # Calculate the center of the padded image
    center_x = width // 2 + padding
    center_y = height // 2 + padding

    # Calculate the rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D((center_x, center_y), angle, 1.0)

    # Apply the rotation to the padded image
    rotated = cv2.warpAffine(padded_image, rotation_matrix, (padded_image.shape[1], padded_image.shape[0]),
                             flags=cv2.INTER_LINEAR)

    # Crop the rotated image to remove the padding
    rotated_cropped = rotated[padding:-padding, padding:-padding]

    return rotated_cropped


# def rotate_half_of_CIFAR_10(labels:list, df_cifar10: pd.DataFrame) -> pd.DataFrame:
#
#     rotated_cifar10 = pd.DataFrame()
#
#     labels_unique = labels.unique()
#     print(type(df_cifar10))
#     pixels = [col for col in df_cifar10.columns]
#     print(labels_unique)
#     for label in labels_unique:
#         logging.info(f'LABEL: {label}')
#
#         # create a DataFrame of the current label class
#         df_class = df_cifar10[labels['label'] == label]
#         # take only half class
#         half_class_to_rotate = df_class.iloc[:df_class.shape[0] // 2]
#         half_class_to_save = df_class.iloc[df_class.shape[0] // 2:]
#         rotated_cifar10 = pd.concat([rotated_cifar10, half_class_to_save])
#
#         for i in range(half_class_to_rotate.shape[0]):
#
#             # Image pixels of current index
#             image_pixels = half_class_to_rotate[pixels].iloc[i]
#
#             # Convert into unsigned kind.
#             image_array = image_pixels.values.reshape(32, 32, 3).astype('uint8')
#
#             # Create a random angle until 90 degrees
#             angle = random.random() * 90
#
#             now = datetime.now()
#             logging.info(f"i = {i} -> rotate_image(image_array, {angle}), time: {now}")
#             print(now)
#
#             rotated_image = rotate_image(image_array, angle)
#
#             now = datetime.now()
#             print(now)
#
#             rotated_image_df = pd.DataFrame(rotated_image.reshape(1, -1), columns=pixels)
#             rotated_image_df['label'] = label
#             rotated_image_df['source'] = 'cifar-10 rotated'
#             rotated_cifar10 = pd.concat([rotated_cifar10, rotated_image_df])
#
#     return rotated_cifar10


# def rotate_CIFAR_100(df_cifar100: pd.DataFrame):
#     print("columns: ", df_cifar100.columns)
#     pixels = [col for col in df_cifar100.columns if col.startswith('pixel')]
#     print("pixels: ", pixels)
#     # Create an empty DataFrame with the same columns
#     rotated_cifar100 = pd.DataFrame(columns=df_cifar100.columns)
#
#     for img_index in range(0, df_cifar100.shape[0]):
#
#         # Access the row data by index using pd.iloc function
#         row = df_cifar100.iloc[img_index]
#
#         # Extract image pixels from the row
#         img = row[pixels].values.reshape(32, 32, 3).astype('uint8')
#
#         label_number = row["label"]
#
#         # Create a random angle until 90 degrees
#         angle = random.random() * 90
#
#         rotate_img = rotate_image(img, angle)
#
#         now = datetime.now()
#         logging.info(f"i = {img_index} -> rotate_image(image_array, {angle}), time: {now}")
#
#         # Create a new row for the rotated image with the same format
#
#         rotated_img_df = pd.DataFrame(rotate_img.reshape(1, -1), columns=pixels)
#         rotated_img_df['label'] = label_number
#         rotated_img_df['source'] = 'cifar-100_rotated'
#
#         rotated_cifar100 = pd.concat([rotated_cifar100, rotated_img_df])
#
#     rotated_cifar100 = pd.concat([rotated_cifar100, df_cifar100])
#     return rotated_cifar100


