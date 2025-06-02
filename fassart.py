import os

# Define the project structure with directories and files
project_structure = {
    "time_series_analysis": ["README.md", "requirements.txt", "config.py", "main.ipynb"],
    "src": [
        "__init__.py", "data_loader.py", "time_series_analyzer.py", "model_selector.py",
        "forecaster.py", "visualizer.py", "diagnostics.py", "report_generator.py"
    ],
    "utils": ["__init__.py", "file_utils.py", "statistical_tests.py", "validation.py"],
    "data/raw": [],
    "data/processed": [],
    "data/sample": [],
    "outputs/plots": [],
    "outputs/reports": [],
    "outputs/models": [],
    "outputs/forecasts": [],
    "notebooks": [
        "01_data_exploration.ipynb", "02_model_development.ipynb",
        "03_model_comparison.ipynb", "04_final_analysis.ipynb"
    ],
    "tests": ["__init__.py", "test_data_loader.py", "test_analyzer.py", "test_forecaster.py"]
}

def create_project_structure(base_path, structure):
    """
    Creates the directory structure and initializes empty files.
    """
    for folder, files in structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)  # Ensure directory exists
        for file in files:
            file_path = os.path.join(folder_path, file)
            open(file_path, 'w').close()  # Create empty files

# Set the base directory (current working directory)
base_directory = '/home/oshadi/SISR-Final_Year_Project/envs/Time_Series_Analysis'
create_project_structure(base_directory, project_structure)

print(f"Project structure created successfully in {base_directory}")
