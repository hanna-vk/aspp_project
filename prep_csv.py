# --- INSTALLING REQUIRED PACKAGES ---
import pandas as pd
import numpy as np

# --- LOAD DATA AND REMOVE UNWANTED ROWS AND COLUMNS ---
def prep_csv(file_path):    
    data = pd.read_csv(file_path, header=None)
    
    # Name stored in line 2, removing all other header lines
    data_red_row = data.drop(index=[0]+list(range(2,11))).reset_index(drop=True) 
    
    # First column contains time stamps and is saved separately and used for indexing in DataFrame
    time_stamp = data_red_row.iloc[1:, 0]
    
    # Remove every third column starting from the third
    data_red_col = data_red_row.iloc[:, 2::3]

    # Get variable names from line 2 (index 1)
    column_names = data_red_col.iloc[0].values
    data_red_col = data_red_col.drop(data_red_col.index[0], axis=0)
    
    # Setting new indices and column names
    data_red = data_red_col.set_index(time_stamp)
    data_red.columns = column_names

    # Remove rows with NaN values and corresponding time stamps
    valid_rows = ~data_red.isnull().any(axis=1)
    data_red = data_red[valid_rows]
    time_stamp = time_stamp[valid_rows.values]
    
    return data_red, time_stamp