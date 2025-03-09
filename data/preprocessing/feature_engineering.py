import pandas as pd

def add_fatigue_features(input_file: str, output_file: str):
    """Add derived fatigue features (e.g., normalized fatigue score) to crew data."""
    df = pd.read_csv(input_file)
    df['normalized_fatigue'] = df['fatigue_score'] / df['fatigue_score'].max()
    df.to_csv(output_file, index=False)
    print(f"Derived fatigue features added and saved to {output_file}")

if __name__ == "__main__":
    add_fatigue_features('../datasets/processed/crew_data_processed.csv', '../datasets/processed/crew_data_processed.csv')
