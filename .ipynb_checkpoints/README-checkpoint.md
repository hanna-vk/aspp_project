# aspp_project
Repository for course project

The idea with the project was to create a Python package, or set of functions at least, that can be used to, in a general way, load data from .csv files, remove unecessary rows and columns, pre-process data, split data into training and testing data sets, and evaluate some regression models.  

The repository consists of 
1. A notebook run_main.ipynb that calls some user defined functions
2. prep_csv.py that is used to prep data from aCurve (very specific software for data exports) in .csv format. The prep_csv function removes every third column (empty) and creates a pandas dataframe
with time stamps as indices and variable names as in row 2 in the .csv file. 
3. pre_process.py, which defines two functions: split and scale. The data is split into training and testing data using the split function. Data is scaled (normalized) using the function scale.
4. evaluation.py that is used to train and evaluate several machine learning models based on MAE, MSE, RMSE and R2, and plot the predictions and true data in two ways. 
