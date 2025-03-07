# --- INSTALLING REQUIRED OPEN PACKAGES ---
# Basics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Pre-processing and evaluation
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Model libraries
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
import xgboost as xgb

# --- IMPORTING OWN FUNCTIONS ---
from .load_csv import load_data
from .prep_csv import remove_col, remove_line
from .pre_process import split, scale
from .evaluation import evaluate_models, plot_predictions
from .main import main