# FUNCTION TO REMOVE COLUMNS FROM aCURVE .csv FILES
# Files are loaded through load_csv.py and converted to pandas format
# Remove all columns containing "tag" in line 1
def remove_col(data)
    # First column contains time stamps and should be saved separately
    time_stamp = data.iloc[:,0]
    time_stamp = time_stamp.drop(time_stamp.index[[0,2,3,4,5,6,7,8,9,10]], axis=0, inplace=True)

    # Remove all columns containing the word "Tag/tag" 
    data_red_col = data.loc[:,~df.columns.str.contains('^tag', case=False)] 
    
    return data_red_col, time_stamp
    
# FUNCTION TO REMOVE LINES FROM aCURVE .csv FILES
# Files are loaded through load_csv.py and converted to pandas format
# Name stored in line 2
def remove_lines(data)
    data_red_line = data.drop(data.index[[0,2,3,4,5,6,7,8,9,10]], axis=0, inplace=True)

    return data_red_line