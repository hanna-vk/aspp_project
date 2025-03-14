# --- LOAD DATA ---
def load_data(file_path):
    """
    Load the CSV file and return the data as a pandas DataFrame.
    """
    return pd.read_csv(file_path)
