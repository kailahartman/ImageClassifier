import pandas as pd
import os
df1 = pd.read_csv(os.getcwd()+r'\\data\\file1.csv')
df2 = pd.read_csv(os.getcwd()+r'\\data\\file1.csv')
df3 = pd.read_csv(os.getcwd()+r'\\data\\our_data.csv')

combined_df = pd.concat([df1, df2, df3])

combined_df.to_csv(os.getcwd()+r'\\data\\combined_data.csv', index=False)
