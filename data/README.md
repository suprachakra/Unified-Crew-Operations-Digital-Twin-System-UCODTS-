## Data Science & Machine Learning

This directory contains all components related to data science and machine learning for the Unified Crew & Operations Digital Twin System (UCODTS). It includes raw and processed datasets, Jupyter notebooks for exploratory analysis and prototyping, preprocessing scripts, ML pipelines for training and inference, and trained model files.

### Directory Structure
- **datasets/**  
  - **raw/**: Contains raw CSV files for crew, flight, and maintenance logs (50 rows each).  
  - **processed/**: Contains cleaned and enriched CSV files derived from raw data.
- **notebooks/**  
  Jupyter notebooks for exploratory data analysis (EDA), data cleaning prototypes, and model prototyping.
- **models/**  
  Binary files for trained ML models (placeholders); generated during the training process.
- **preprocessing/**  
  Python scripts for data cleaning, feature engineering, and data validation.
- **ml_pipeline/**  
  End-to-end ML pipeline scripts for training models, performing inference, and utility functions.
- **requirements.txt**  
  Lists all Python dependencies for the Data/ML environment.
- **README.md**  
  This documentation file.

### Getting Started
1. **Install Dependencies:**  
   Run `pip install -r requirements.txt` from the `data/` directory.
2. **Data Preparation:**  
   Execute preprocessing scripts in the `preprocessing/` folder to clean and enhance raw datasets.
3. **Exploratory Analysis:**  
   Open the notebooks in the `notebooks/` folder using Jupyter Notebook or JupyterLab for initial exploration.
4. **Model Training:**  
   Run the training script in `ml_pipeline/train_pipeline.py` to build predictive models.
5. **Inference:**  
   Use `ml_pipeline/inference_pipeline.py` to perform model inference on new data.
6. **Continuous Improvement:**  
   Leverage the utility functions in `ml_pipeline/pipeline_utils.py` for data splitting and model evaluation.

### Contributing
Contributions are welcome. Please follow the guidelines in the root `CONTRIBUTING.md` document.
