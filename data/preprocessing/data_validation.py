import pandas as pd

def validate_data(df: pd.DataFrame) -> bool:
    """
    Validate the DataFrame by checking for missing values and negative fatigue scores.
    
    Returns:
        True if data passes validation, False otherwise.
    """
    # Check for missing values in the entire dataframe
    if df.isnull().sum().sum() > 0:
        print("Validation Error: Missing values found.")
        return False
    
    # Check for negative values in 'fatigue_score' if it exists
    if 'fatigue_score' in df.columns and (df['fatigue_score'] < 0).any():
        print("Validation Error: Negative fatigue scores found.")
        return False
    
    print("Data validation passed.")
    return True

if __name__ == "__main__":
    input_file = "datasets/raw/crew_data.csv"
    df = pd.read_csv(input_file)
    if validate_data(df):
        print("Data is valid.")
    else:
        print("Data validation failed.")
