# --- MAIN FUNCTION ---
def main(file_path):
    """
    Main function to load data, preprocess, train and evaluate models, and plot predictions.
    """
    # LOAD the data
    df = load_data(file_path)

    df, time_stamp = remove_col(df)
    df = remove_line(df)

    # SPLIT the data
    X_train, X_test, y_train, y_test = split(df,0.2)

    # PRE-PROCESS the data
    X_train, X_test = scale(X_train,X_test)

    # TRAIN models
    results, predictions = evaluate_models(X_train, X_test, y_train, y_test)

    # EVALUATE models
    for model_name, metrics in results.items():
        print(f"\n{model_name} Results:")
        for metric, value in metrics.items():
            print(f"{metric}: {value:.4f}")

    # PLOT predictions vs actual data
    plot_predictions(y_test, predictions)