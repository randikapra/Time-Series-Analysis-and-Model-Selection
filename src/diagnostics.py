"""Model diagnostics and statistical tests"""

import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.tsa.stattools import adfuller
from typing import Tuple, Dict
import config

class ModelDiagnostics:
    """Performs comprehensive model diagnostics"""
    
    def __init__(self, significance_level: float = config.SIGNIFICANCE_LEVEL):
        self.alpha = significance_level
    
    def ljung_box_test(self, residuals: pd.Series, lags: int = 10) -> Dict:
        """Perform Ljung-Box test for residual autocorrelation"""
        lb_test = acorr_ljungbox(residuals, lags=lags, return_df=True)
        
        # Get overall test result
        p_value = lb_test['lb_pvalue'].iloc[-1]
        is_significant = p_value < self.alpha
        
        return {
            'test_statistic': lb_test['lb_stat'].iloc[-1],
            'p_value': p_value,
            'is_significant': is_significant,
            'interpretation': 'Residuals show autocorrelation' if is_significant else 'No significant autocorrelation'
        }
    
    def jarque_bera_test(self, residuals: pd.Series) -> Dict:
        """Perform Jarque-Bera test for residual normality"""
        jb_stat, p_value = stats.jarque_bera(residuals.dropna())
        is_significant = p_value < self.alpha
        
        return {
            'test_statistic': jb_stat,
            'p_value': p_value,
            'is_significant': is_significant,
            'interpretation': 'Residuals are not normally distributed' if is_significant else 'Residuals are approximately normal'
        }
    
    def adf_test(self, series: pd.Series) -> Dict:
        """Perform Augmented Dickey-Fuller test for stationarity"""
        adf_stat, p_value, used_lag, n_obs, critical_values, ic_best = adfuller(series.dropna())
        
        is_stationary = p_value < self.alpha
        
        return {
            'test_statistic': adf_stat,
            'p_value': p_value,
            'critical_values': critical_values,
            'used_lag': used_lag,
            'is_stationary': is_stationary,
            'interpretation': 'Series is stationary' if is_stationary else 'Series is non-stationary'
        }
    
    def comprehensive_diagnostics(self, fitted_model, original_series: pd.Series) -> Dict:
        """Run comprehensive model diagnostics"""
        residuals = fitted_model.resid
        
        diagnostics = {
            'ljung_box': self.ljung_box_test(residuals),
            'jarque_bera': self.jarque_bera_test(residuals),
            'residual_stats': {
                'mean': residuals.mean(),
                'std': residuals.std(),
                'skewness': stats.skew(residuals.dropna()),
                'kurtosis': stats.kurtosis(residuals.dropna())
            }
        }
        
        return diagnostics
