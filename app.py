import pickle
import numpy as np
import matplotlib.pyplot as plt

def unpickle(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

path = r'C:\Users\אתי\Documents\BOOTCAMP\cifar-10-batches-py\\data_batch_1'
data_dict = unpickle(path)


data = data_dict[b'data']
labels = data_dict[b'labels']


images = np.reshape(data, (len(data), 3, 32, 32))
print("images", images)

fig, axes = plt.subplots(2, 5, figsize=(12, 6))
axes = axes.ravel()

for i in range(10):
    image = images[i]
    image = np.transpose(image, (1, 2, 0))

    axes[i].imshow(image)
    axes[i].set_title('Label: {}'.format(labels[i]))
    axes[i].axis('off')

plt.tight_layout()
plt.show()