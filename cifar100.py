
import pickle
import numpy as np
import matplotlib.pyplot as plt

def unpickle(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict
file = r'C:\Users\אתי\Documents\BOOTCAMP\cifar-100-python\train'
train_data = unpickle(file)
print(train_data.keys())


meta_file = r'C:\Users\אתי\Documents\BOOTCAMP\cifar-100-python\meta'
meta_data = unpickle(meta_file )

# take the images data from training data
images = train_data[b'data']
# reshape and transpose the images
images = images.reshape(len(images),3,32,32).transpose(0,2,3,1)
# take coarse and fine labels of the images
c_labels = train_data[b'coarse_labels']
# print(c_labels)
f_labels = train_data[b'fine_labels']
# take coarse and fine label names of the images
coarse_names = meta_data[b'coarse_label_names']
fine_names = meta_data[b'fine_label_names']


# dispaly random nine images
# define row and column of figure
rows, columns = 3, 3
# take random image idex id
imageId = np.random.randint(0, len(images), rows * columns)
# take images for above random image ids
images = images[imageId]
# take coarse and fine labels for these images only
c_labels = [c_labels[i] for i in imageId]
f_labels = [f_labels[j] for j in imageId]
# define figure
fig=plt.figure(figsize=(8, 10))
# visualize these random images
for i in range(1, columns*rows +1):
    fig.add_subplot(rows, columns, i)
    plt.imshow(images[i-1])
    plt.xticks([])
    plt.yticks([])
    plt.title("{} \n {}"
          .format(coarse_names[c_labels[i-1]], fine_names[f_labels[i-1]]))
plt.show()