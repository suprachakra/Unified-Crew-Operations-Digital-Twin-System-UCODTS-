import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

def train_model(data_file: str, model_file: str):
    """Train a simple regression model on flight data and save it as a binary file."""
    df = pd.read_csv(data_file)
    # Convert scheduled_departure to a numeric timestamp
    df['scheduled_departure_ts'] = pd.to_datetime(df['scheduled_departure']).astype(int) / 10**9
    X = df[['scheduled_departure_ts']]
    y = df['delay_minutes']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    print("Model training complete. R^2 score:", score)
    joblib.dump(model, model_file)
    print(f"Model saved to {model_file}")

if __name__ == "__main__":
    train_model('../datasets/processed/flight_data_processed.csv', '../models/maintenance_model.pkl')
