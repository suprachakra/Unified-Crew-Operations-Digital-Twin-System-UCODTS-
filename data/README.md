## Data Science & ML Documentation

### Overview
This directory contains the Data Science and Machine Learning components for UCODTS. It is organized as follows:

- **datasets/**:  
  - `raw/`: Contains raw datasets (crew, flight, maintenance logs).
  - `processed/`: Contains processed and cleaned datasets for analysis.
- **notebooks/**:  
  - Jupyter notebooks for exploratory analysis, data cleaning, and model prototyping.
- **models/**:  
  - Trained ML models saved as binary files (e.g., crew fatigue model, maintenance model).
- **preprocessing/**:  
  - Python scripts for data cleaning, feature engineering, and data validation.
- **ml_pipeline/**:  
  - End-to-end ML pipeline scripts for training, inference, and utility functions.
- **requirements.txt**:  
  - Lists Python dependencies for the data and ML environment.

### Setup Instructions
1. Navigate to the `data/` directory.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
