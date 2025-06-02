"""Data loading and preprocessing utilities"""

import pandas as pd
import numpy as np
from pathlib import Path
from typing import Tuple, Optional, List
import config

class DataLoader:
    """Handles data loading and basic preprocessing"""
    
    def __init__(self, data_dir: str = config.DATA_DIR):
        self.data_dir = Path(data_dir)
    
    def load_excel_data(self, filepath: str, sheet1: str = 'Dataset 1', 
                       sheet2: str = 'Dataset 2') -> Tuple[pd.DataFrame, pd.DataFrame]:
        """Load data from Excel file with multiple sheets"""
        try:
            df1 = pd.read_excel(filepath, sheet_name=sheet1)
            df2 = pd.read_excel(filepath, sheet_name=sheet2)
            
            print(f"Dataset 1 shape: {df1.shape}")
            print(f"Dataset 2 shape: {df2.shape}")
            
            return df1, df2
        except Exception as e:
            raise FileNotFoundError(f"Error loading data: {str(e)}")
    
    def load_csv_data(self, filepath: str) -> pd.DataFrame:
        """Load data from CSV file"""
        return pd.read_csv(filepath)
    
    def validate_column(self, df: pd.DataFrame, column: str) -> bool:
        """Validate if column exists and has numeric data"""
        if column not in df.columns:
            raise ValueError(f"Column '{column}' not found in dataset")
        
        if not pd.api.types.is_numeric_dtype(df[column]):
            raise TypeError(f"Column '{column}' must contain numeric data")
        
        return True
    
    def extract_time_series(self, df: pd.DataFrame, column: str) -> pd.Series:
        """Extract and clean time series data"""
        self.validate_column(df, column)
        
        series = df[column].dropna()
        if len(series) == 0:
            raise ValueError(f"No valid data found in column '{column}'")
        
        return series