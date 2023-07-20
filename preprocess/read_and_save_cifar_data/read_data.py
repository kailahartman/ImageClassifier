import pickle

def read_data(file):
    print("unpickling the data")

    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict


