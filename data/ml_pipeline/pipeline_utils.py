import pandas as pd

def split_data(df: pd.DataFrame, test_size: float = 0.2, random_state: int = 42):
    """
    Split the data into training and testing sets.
    
    Returns:
        X_train, X_test, y_train, y_test
    """
    from sklearn.model_selection import train_test_split
    return train_test_split(df, test_size=test_size, random_state=random_state)

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the model using Mean Squared Error (MSE).
    
    Returns:
        mse: Mean Squared Error of the model on test data.
    """
    from sklearn.metrics import mean_squared_error
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    return mse

if __name__ == "__main__":
    # Example usage
    df = pd.DataFrame({"feature": [1, 2, 3, 4], "target": [2, 4, 6, 8]})
    X_train, X_test, y_train, y_test = split_data(df[["feature"]], df["target"])
    print("Data split successfully.")
