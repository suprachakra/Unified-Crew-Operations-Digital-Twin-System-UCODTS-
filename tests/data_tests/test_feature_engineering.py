import pandas as pd
import os
from preprocessing.feature_engineering import add_fatigue_features

def test_add_fatigue_features(tmp_path):
    # Create a dummy CSV for testing
    data = "crew_id,name,role,fatigue_score,last_scheduled\n1,Test,Pilot,0.45,2023-11-01\n"
    input_file = tmp_path / "crew.csv"
    output_file = tmp_path / "crew_featured.csv"
    input_file.write_text(data)
    
    add_fatigue_features(str(input_file), str(output_file))
    
    df = pd.read_csv(output_file)
    assert "normalized_fatigue" in df.columns
    # With one row, normalized value should equal 1.0
    assert df["normalized_fatigue"].iloc[0] == 1.0
