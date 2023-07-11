
import pickle
import csv
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pandas as pd


def unpickle(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict




file = r'C:\Users\אתי\Documents\BOOTCAMP\cifar-100-python\train'
train_data = unpickle(file)




# flowers=2  fish=1 people=14

new_dict={2:[],1:[],14:[]}
for i in range(0,len(train_data[b'coarse_labels'])):
    num=train_data[b'coarse_labels'][i]
    if(num==2 or num==1 or num==14):
        new_dict[num].append(train_data[b'data'][i])
#
