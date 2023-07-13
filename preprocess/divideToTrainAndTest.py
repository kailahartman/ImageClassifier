import pandas as pd
from sklearn.model_selection import train_test_split
path_to_data="data.csv"
# Load the CSV file
df = pd.read_csv(path_to_data)

# Split the data into train and test sets
# x=df.loc[:,['Industry_code_ANZSIC06','Industry_aggregation_NZSIOC','Year']]
# y=df.loc[:,['Value']]
X_train, X_test, y_train, y_test = train_test_split(x,y, test_size=0.2)

# Save the train and test sets
X_train.to_csv("CFARTrainData.csv")
X_test.to_csv("CFARTestData.csv")
y_test.to_csv("CFARTestDataY.csv")
y_train.to_csv("CFARTrainDataY.csv")
