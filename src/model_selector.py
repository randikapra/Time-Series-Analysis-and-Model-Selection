"""ARIMA model selection and comparison"""

import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from itertools import product
from typing import Tuple, Dict, List, Optional
import config

class ModelSelector:
    """Handles ARIMA model selection and comparison"""
    
    def __init__(self, max_p: int = config.MAX_AR_ORDER, 
                 max_d: int = config.MAX_DIFF_ORDER, 
                 max_q: int = config.MAX_MA_ORDER):
        self.max_p = max_p
        self.max_d = max_d
        self.max_q = max_q
    
    def grid_search_arima(self, series: pd.Series, 
                         seasonal: bool = False) -> Tuple[Tuple[int, int, int], pd.DataFrame]:
        """Perform grid search to find optimal ARIMA parameters"""
        
        results = []
        
        # Generate parameter combinations
        p_values = range(0, self.max_p + 1)
        d_values = range(0, self.max_d + 1)
        q_values = range(0, self.max_q + 1)
        
        for p, d, q in product(p_values, d_values, q_values):
            try:
                model = ARIMA(series, order=(p, d, q))
                fitted_model = model.fit()
                
                results.append({
                    'order': (p, d, q),
                    'aic': fitted_model.aic,
                    'bic': fitted_model.bic,
                    'llf': fitted_model.llf,
                    'params': len(fitted_model.params)
                })
                
            except Exception as e:
                continue
        
        if not results:
            raise ValueError("No valid ARIMA models could be fitted")
        
        # Convert to DataFrame and sort by AIC
        results_df = pd.DataFrame(results)
        results_df = results_df.sort_values('aic').reset_index(drop=True)
        
        best_order = results_df.iloc[0]['order']
        
        return best_order, results_df
    
    def compare_models(self, results_df: pd.DataFrame, top_n: int = 5) -> pd.DataFrame:
        """Compare top N models by AIC"""
        return results_df.head(top_n)
    
    def fit_best_model(self, series: pd.Series, order: Tuple[int, int, int]):
        """Fit the best ARIMA model"""
        model = ARIMA(series, order=order)
        return model.fit()
