import pandas as pd
import os
import glob

file_list = glob.glob(os.getcwd()+r'\\data\\*.csv')

dfs = []
for file_name in file_list:
    df = pd.read_csv(file_name)
    dfs.append(df)

combined_df = pd.concat(dfs)
combined_df = combined_df.sample(frac=1).reset_index(drop=True)
combined_df.to_csv(os.getcwd()+r'\data\combined_data.csv', index=False)


