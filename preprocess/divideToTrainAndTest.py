import pandas as pd
from sklearn.model_selection import train_test_split

# Load the CSV file
df = pd.read_csv("data.csv")

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(df, df["target"], test_size=0.2)

# Save the train and test sets
X_train.to_csv("CFARTrainData.csv")
X_test.to_csv("CFARTestData.csv")