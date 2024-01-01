import numpy as np
import matplotlib.image
import os

def save_image_local(images, output_dir, image_format, labels):
    print("saving the images locally")
    for j in range(len(images)):
        image = images[j]
        image = np.transpose(image, (1, 2, 0))
        label = labels[j]
        image_name = r'image_{}_label_{}.{}'.format(j + 1, label, image_format)
        output_path = os.path.join(output_dir, image_name)
        matplotlib.image.imsave(output_path, image)