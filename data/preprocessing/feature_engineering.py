import pandas as pd

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add new features to the dataset.
    
    Features:
    - normalized_fatigue: Normalizes fatigue_score by dividing by the max fatigue score.
    - day_of_week: Extracts the day of the week from the 'last_scheduled' date.
    
    Returns:
        DataFrame with new features.
    """
    # Normalize fatigue_score if it exists
    if 'fatigue_score' in df.columns:
        df['normalized_fatigue'] = df['fatigue_score'] / df['fatigue_score'].max()
    
    # Extract day of week from last_scheduled if it exists
    if 'last_scheduled' in df.columns:
        df['day_of_week'] = pd.to_datetime(df['last_scheduled']).dt.day_name()
    
    return df

if __name__ == "__main__":
    input_file = "datasets/raw/crew_data.csv"
    output_file = "datasets/processed/crew_data_processed.csv"
    df = pd.read_csv(input_file)
    df = add_features(df)
    df.to_csv(output_file, index=False)
    print(f"Features added and saved to {output_file}")
