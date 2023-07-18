import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image

def save_image_local(images, output_dir, image_format):
    fig, axes = plt.subplots(2, 5, figsize=(12, 6))
    axes = axes.ravel()
    for j in range(len(images)):
        image = images[j]
        image = np.transpose(image, (1, 2, 0))

        image_name = r'image_{}_.{}'.format(j + 1, image_format)
        output_path = output_dir + '\\' + image_name
        matplotlib.image.imsave(output_path, image)
