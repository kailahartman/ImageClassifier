import pickle
import numpy as np
import matplotlib.pyplot as plt

def unpickle(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

path = r'C:\bootCamp\APPLIED\cifar-10-batches-py\\data_batch_'
for i in range(1, 6):
    data_dict = unpickle(path+str(i))
    data = data_dict[b'data']
    labels = data_dict[b'labels']


    images = np.reshape(data, (len(data), 3, 32, 32))
    print("images", images)

    fig, axes = plt.subplots(2, 5, figsize=(12, 6))
    axes = axes.ravel()
    # Saving the images
    output_dir = r'C:\bootCamp\APPLIED\output_images'
    image_format = 'png'

    for j in range(len(images)):
        image = images[j]
        image = np.transpose(image, (1, 2, 0))

        label = labels[j]
        image_name = 'image_{}_label_{}.{}'.format(j + 1, label, image_format)
        output_path = output_dir + '\\' + image_name

        plt.imshow(image)
        plt.axis('off')
        plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
        plt.close()

    print('Images saved successfully!')

    plt.tight_layout()
    plt.show()

