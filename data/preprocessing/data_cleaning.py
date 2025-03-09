import pandas as pd

def clean_crew_data(input_file: str, output_file: str):
    """Clean crew data by converting fatigue scores to numeric and dropping rows with missing values."""
    df = pd.read_csv(input_file)
    df['fatigue_score'] = pd.to_numeric(df['fatigue_score'], errors='coerce')
    df.dropna(inplace=True)
    df.to_csv(output_file, index=False)
    print(f"Crew data cleaned and saved to {output_file}")

if __name__ == "__main__":
    clean_crew_data('../datasets/raw/crew_data.csv', '../datasets/processed/crew_data_processed.csv')
