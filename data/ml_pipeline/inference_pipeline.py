import pandas as pd
import joblib

def run_inference(data_file: str, model_file: str):
    """Run inference on new data using the trained model."""
    df = pd.read_csv(data_file)
    df['scheduled_departure_ts'] = pd.to_datetime(df['scheduled_departure']).astype(int) / 10**9
    model = joblib.load(model_file)
    predictions = model.predict(df[['scheduled_departure_ts']])
    df['predicted_delay'] = predictions
    print("Inference complete. Sample predictions:")
    print(df[['flight_number', 'predicted_delay']].head())
    return df

if __name__ == "__main__":
    run_inference('../datasets/processed/flight_data_processed.csv', '../models/maintenance_model.pkl')
