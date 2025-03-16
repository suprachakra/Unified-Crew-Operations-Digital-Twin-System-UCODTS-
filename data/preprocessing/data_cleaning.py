import pandas as pd

def clean_data(file_path: str) -> pd.DataFrame:
    """
    Load and clean the dataset.
    
    Steps:
    - Load CSV data.
    - Drop duplicate rows.
    - Convert numeric columns and fill missing values with the median.
    - Convert date columns to datetime.
    
    Returns:
        Cleaned DataFrame.
    """
    df = pd.read_csv(file_path)
    
    # Drop duplicate rows
    df.drop_duplicates(inplace=True)
    
    # Fill missing values for numeric columns with the median value
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    for col in numeric_cols:
        df[col].fillna(df[col].median(), inplace=True)
    
    # Convert date columns to datetime, if they exist
    if 'last_scheduled' in df.columns:
        df['last_scheduled'] = pd.to_datetime(df['last_scheduled'])
    
    return df

if __name__ == "__main__":
    input_file = "datasets/raw/crew_data.csv"
    output_file = "datasets/processed/crew_data_processed.csv"
    cleaned_df = clean_data(input_file)
    cleaned_df.to_csv(output_file, index=False)
    print(f"Data cleaned and saved to {output_file}")
