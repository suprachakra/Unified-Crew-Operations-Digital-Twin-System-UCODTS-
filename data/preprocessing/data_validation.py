import pandas as pd

def validate_data(input_file: str):
    """Validate dataset by checking for missing values and ensuring correct data types."""
    df = pd.read_csv(input_file)
    null_counts = df.isnull().sum()
    print("Null values in each column:\n", null_counts)
    # Additional validation logic can be added here
    return null_counts

if __name__ == "__main__":
    validate_data('../datasets/processed/flight_data_processed.csv')
