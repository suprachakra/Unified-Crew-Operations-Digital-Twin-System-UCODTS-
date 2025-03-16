import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

def load_data(file_path: str) -> pd.DataFrame:
    """Load the dataset from a CSV file."""
    return pd.read_csv(file_path)

def train_model(df: pd.DataFrame):
    """
    Train a baseline model to predict fatigue_score.
    This is a placeholder using a simple linear regression model.
    """
    # Define features and target (placeholder: using fatigue_score as both)
    X = df[['fatigue_score']]
    y = df['fatigue_score']
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Evaluate model performance
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f"Model trained with Mean Squared Error: {mse}")
    
    # Save the trained model to a binary file
    joblib.dump(model, "../models/crew_fatigue_model.pkl")
    print("Model saved to ../models/crew_fatigue_model.pkl")
    
if __name__ == "__main__":
    df = load_data("datasets/processed/crew_data_processed.csv")
    train_model(df)
