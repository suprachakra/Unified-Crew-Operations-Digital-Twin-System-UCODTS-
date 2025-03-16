import pandas as pd
import joblib

def load_model(model_path: str):
    """Load a trained model from a binary file."""
    return joblib.load(model_path)

def predict_fatigue(model, input_data: pd.DataFrame):
    """Generate predictions using the provided model."""
    predictions = model.predict(input_data)
    return predictions

if __name__ == "__main__":
    # Load processed data for inference
    input_data = pd.read_csv("datasets/processed/crew_data_processed.csv")[['fatigue_score']]
    model = load_model("../models/crew_fatigue_model.pkl")
    predictions = predict_fatigue(model, input_data)
    print("Predictions:", predictions)
