# --- INSTALLING REQUIRED PACKAGES ---
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
    
# Model libraries
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
import xgboost as xgb

# --- TRAIN AND EVALUATE REGRESSION MODELS ---
def evaluate_models(X_train, X_test, y_train, y_test):
    """
    Train different regression models 
        - Linear regression
        - Decision Tree
        - Random Forest
        - Support Vector Machine
        - Gradient Boosting
        - XGBoost
        - Nearest Neighbor
    and evaluate their performance on the test data using metrics MAE, MSE, RMSE, R2.
    """
    # Define models
    models = {
        "Linear Regression": LinearRegression(),
        "Decision Tree": DecisionTreeRegressor(),
        "Random Forest": RandomForestRegressor(),
        "Support Vector Machine": SVR(),
        "Gradient Boosting": GradientBoostingRegressor(),
        "XGBoost": xgb.XGBRegressor(),
        "Nearest neighbor": KNeighborsRegressor()
    }

    # Evaluate each model
    results = {}
    predictions = {}

    for name, model in models.items():
        # Train the model
        model.fit(X_train, y_train)

        # Make predictions
        y_pred = model.predict(X_test)

        # Store predictions for plotting later
        predictions[name] = y_pred

        # Calculate evaluation metrics
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)

        # Store the results
        results[name] = {
            "MAE": mae,
            "MSE": mse,
            "RMSE": rmse,
            "R2": r2
        }

    return results, predictions

# --- PLOT RESULTS ---
def plot_predictions(y_test, predictions):
    """
    Generates two plots: (1) a time series plot of the actual and predicted values for each 
    model, evaluated on test data, and (2) a true vs predicted scatter plot to evaluate under or 
    overestimated ranges. 
    """    
    # TIME SERIES PLOT
    # Defining figure size and axis
    plt.figure(figsize=(12, 8))
    ax = np.linspace(0, len(y_test)-1, num=len(y_test))

    # Plot test data
    plt.plot(ax,y_test, label="Actual", color="black", linestyle="--", linewidth=2)

    # Plot predictions from each model
    for model_name, y_pred in predictions.items():
        plt.plot(ax,y_pred, label=f"{model_name} Prediction")

    # Plotting the plot with titles and lables
    plt.title("Model outputs and true values")
    plt.xlabel("Time Step")
    plt.legend()
    plt.grid(True)
    plt.show()

    # 2 TRUE VS. PREDICTED
    # Defining second figure and axises
    plt.figure(figsize=(12, 8))
    ax = np.linspace(min(y_test), max(y_test), num=len(y_test))

    # Plot the ideal predictor (y=x)
    plt.plot(ax,ax, label="Ideal predictor", color="black", linestyle="-", linewidth=2)

    # Plot the true predictions vs predictions from each model
    for model_name, y_pred in predictions.items():
        plt.scatter(y_test,y_pred, label=f"{model_name} prediction")

    # Plotting the plot with titles and lables
    plt.title("True vs. Predicted")
    plt.legend()
    plt.grid(True)
    plt.show()