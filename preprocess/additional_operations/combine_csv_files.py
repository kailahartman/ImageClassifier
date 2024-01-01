import os
import glob
import pandas as pd
import codecs
def combine_csv_files():
    print("combining the csv files")
    file_list = glob.glob(os.path.join(os.getcwd(), 'data', '*.csv'))

    dfs = []
    for file_name in file_list:
        print(file_name)
        # Use 'codecs.open' to handle encoding with errors='ignore'
        with codecs.open(file_name, 'r', encoding='utf-8', errors='ignore') as file:
            df = pd.read_csv(file)
        dfs.append(df)

    combined_df = pd.concat(dfs)
    combined_df = combined_df.sample(frac=1).reset_index(drop=True)
    combined_df.to_csv(os.path.join(os.getcwd(), 'data', 'combined_data.csv'), index=False)
