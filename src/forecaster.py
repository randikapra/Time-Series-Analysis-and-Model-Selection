"""Forecasting and evaluation utilities"""

import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error
from typing import Tuple, Dict, Optional
import config

class Forecaster:
    """Handles forecasting and performance evaluation"""
    
    def __init__(self, forecast_periods: int = config.FORECAST_PERIODS):
        self.forecast_periods = forecast_periods
    
    def generate_forecasts(self, fitted_model, steps: Optional[int] = None) -> pd.Series:
        """Generate out-of-sample forecasts"""
        if steps is None:
            steps = self.forecast_periods
        
        forecast = fitted_model.get_forecast(steps=steps)
        return forecast.predicted_mean
    
    def get_forecast_intervals(self, fitted_model, steps: Optional[int] = None, 
                             alpha: float = 0.05) -> Tuple[pd.Series, pd.DataFrame]:
        """Get forecasts with confidence intervals"""
        if steps is None:
            steps = self.forecast_periods
        
        forecast = fitted_model.get_forecast(steps=steps)
        forecast_mean = forecast.predicted_mean
        forecast_ci = forecast.conf_int(alpha=alpha)
        
        return forecast_mean, forecast_ci
    
    def evaluate_forecasts(self, actual: pd.Series, predicted: pd.Series) -> Dict:
        """Calculate forecast evaluation metrics"""
        # Ensure same length for comparison
        min_len = min(len(actual), len(predicted))
        actual_subset = actual.iloc[-min_len:]
        predicted_subset = predicted.iloc[:min_len]
        
        mse = mean_squared_error(actual_subset, predicted_subset)
        mae = mean_absolute_error(actual_subset, predicted_subset)
        rmse = np.sqrt(mse)
        
        # Additional metrics
        mape = np.mean(np.abs((actual_subset - predicted_subset) / actual_subset)) * 100
        
        return {
            'mse': mse,
            'mae': mae,
            'rmse': rmse,
            'mape': mape
        }
    
    def cross_validate_forecast(self, series: pd.Series, model_order: Tuple[int, int, int], 
                              test_size: int = 12) -> Dict:
        """Perform time series cross-validation"""
        from statsmodels.tsa.arima.model import ARIMA
        
        train_series = series.iloc[:-test_size]
        test_series = series.iloc[-test_size:]
        
        # Fit model on training data
        model = ARIMA(train_series, order=model_order)
        fitted_model = model.fit()
        
        # Generate forecasts
        forecasts = self.generate_forecasts(fitted_model, steps=test_size)
        
        # Evaluate performance
        metrics = self.evaluate_forecasts(test_series, forecasts)
        
        return {
            'metrics': metrics,
            'forecasts': forecasts,
            'actual': test_series,
            'fitted_model': fitted_model
        }
