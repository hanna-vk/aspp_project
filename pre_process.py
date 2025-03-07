# --- SPLIT AND PRE-PROCESS DATA ---
def split(data,testsize):
    """
    Preprocess the data by splitting into features (X) and target (y),
    and splitting into training and test sets, assuming y is the last column of "data", 
    and assigning a test size "testsize". 
    Optional feature scaling by assigning scaling = 1 (ON) or = 0 (OFF). 
    """
    
    # Assume the last column is the target variable
    X = data.iloc[:, :-1].values  # Features (all but last column)
    y = data.iloc[:, -1].values   # Response variable (last column)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=testsize, shuffle=False, random_state=42)

    return X_train, X_test, y_train, y_test

def scale(X_train, X_test)   
    # Feature scaling
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test
