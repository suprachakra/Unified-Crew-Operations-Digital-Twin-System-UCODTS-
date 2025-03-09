import pandas as pd
import os
from preprocessing.data_cleaning import clean_crew_data

def test_clean_crew_data(tmp_path):
    # Create a dummy CSV for testing
    data = "crew_id,name,role,schedule,fatigue_score,last_scheduled\n1,Test,Pilot,\"2023-11-01,2023-11-05\",0.45,2023-11-01\n"
    input_file = tmp_path / "raw_crew.csv"
    output_file = tmp_path / "cleaned_crew.csv"
    input_file.write_text(data)
    
    clean_crew_data(str(input_file), str(output_file))
    
    df = pd.read_csv(output_file)
    assert df.shape[0] == 1
    assert "fatigue_score" in df.columns
