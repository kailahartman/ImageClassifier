import numpy as np
import cv2

def downsample_image(image, new_size):
  """Downsamples an image to the specified size."""
  old_size = image.shape[:2]
  new_image = np.zeros((new_size[0], new_size[1], 3))
  for i in range(new_size[0]):
    for j in range(new_size[1]):
      old_i = int(i * old_size[0] / new_size[0])
      old_j = int(j * old_size[1] / new_size[1])
      new_image[i, j] = image[old_i, old_j]
  return new_image

def read_image(image_path):
  """Reads an image from the specified path."""
  image = cv2.imread(image_path)
  return image

def write_image(image, image_path):
  """Writes an image to the specified path."""
  cv2.imwrite(image_path, image)

image_path = "car.png"
image = read_image(image_path)
new_image = downsample_image(image, (32, 32))
write_image(new_image, "new_image.png")

