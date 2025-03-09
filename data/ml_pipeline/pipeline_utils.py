import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """Load a CSV file into a DataFrame."""
    return pd.read_csv(file_path)

def save_model(model, filename: str):
    """Save the model using joblib."""
    import joblib
    joblib.dump(model, filename)
    print(f"Model saved to {filename}")
