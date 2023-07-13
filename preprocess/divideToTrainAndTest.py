import pandas as pd
import os
from sklearn.model_selection import train_test_split
path_to_data = os.getcwd()+r'\\data\\combined_data.csv'

df = pd.read_csv(path_to_data)

X = df.loc[:, ['labels']]
y = df.loc[:, ['path']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Save the train and test sets
X_train.to_csv("CFARTrainDataX.csv")
X_test.to_csv("CFARTestDataX.csv")
y_train.to_csv("CFARTrainDataY.csv")
y_test.to_csv("CFARTestDataY.csv")
