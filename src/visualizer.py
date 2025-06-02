"""Visualization utilities for time series analysis"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from scipy import stats
from pathlib import Path
from typing import Optional, Tuple, List
import config

class Visualizer:
    """Handles all visualization needs for time series analysis"""
    
    def __init__(self, figsize: Tuple[int, int] = config.FIGURE_SIZE, 
                 dpi: int = config.DPI, style: str = config.PLOT_STYLE):
        self.figsize = figsize
        self.dpi = dpi
        plt.style.use(style)
        self.output_dir = Path(config.PLOTS_DIR)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def plot_time_series(self, series: pd.Series, title: str = "Time Series Plot", 
                        save_path: Optional[str] = None) -> None:
        """Plot time series data"""
        fig, ax = plt.subplots(figsize=self.figsize, dpi=self.dpi)
        
        ax.plot(series.index, series.values, linewidth=1.5, color='steelblue')
        ax.set_title(title, fontsize=14, fontweight='bold')
        ax.set_xlabel('Time Period')
        ax.set_ylabel('Value')
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(self.output_dir / save_path, bbox_inches='tight')
        
        plt.show()
    
    def plot_exploratory_analysis(self, series: pd.Series, column_name: str, 
                                 save_path: str = "exploratory_analysis.png") -> None:
        """Create comprehensive exploratory analysis plots"""
        fig, axes = plt.subplots(2, 2, figsize=(15, 10), dpi=self.dpi)
        fig.suptitle(f'Exploratory Analysis - {column_name}', fontsize=16, fontweight='bold')
        
        # Time series plot
        axes[0,0].plot(series.index, series.values, color='steelblue', linewidth=1.5)
        axes[0,0].set_title('Time Series Plot')
        axes[0,0].grid(True, alpha=0.3)
        
        # Histogram
        axes[0,1].hist(series.dropna(), bins=30, alpha=0.7, color='lightcoral', edgecolor='black')
        axes[0,1].set_title('Distribution')
        axes[0,1].set_xlabel('Value')
        axes[0,1].set_ylabel('Frequency')
        
        # Box plot
        axes[1,0].boxplot(series.dropna(), vert=True)
        axes[1,0].set_title('Box Plot')
        axes[1,0].set_ylabel('Value')
        
        # Q-Q plot
        stats.probplot(series.dropna(), dist="norm", plot=axes[1,1])
        axes[1,1].set_title('Q-Q Plot (Normal Distribution)')
        
        plt.tight_layout()
        plt.savefig(self.output_dir / save_path, bbox_inches='tight')
        plt.show()
    
    def plot_acf_pacf(self, series: pd.Series, lags: int = 20, 
                     save_path: str = "acf_pacf_plots.png") -> None:
        """Plot ACF and PACF"""
        fig, axes = plt.subplots(1, 2, figsize=(15, 5), dpi=self.dpi)
        
        plot_acf(series.dropna(), lags=lags, ax=axes[0], title='Autocorrelation Function')
        plot_pacf(series.dropna(), lags=lags, ax=axes[1], title='Partial Autocorrelation Function')
        
        plt.tight_layout()
        plt.savefig(self.output_dir / save_path, bbox_inches='tight')
        plt.show()
    
    def plot_model_diagnostics(self, fitted_model, save_path: str = "model_diagnostics.png") -> None:
        """Plot comprehensive model diagnostics"""
        residuals = fitted_model.resid
        
        fig, axes = plt.subplots(2, 2, figsize=(15, 10), dpi=self.dpi)
        fig.suptitle('Model Diagnostics', fontsize=16, fontweight='bold')
        
        # Residuals vs Fitted
        fitted_values = fitted_model.fittedvalues
        axes[0,0].scatter(fitted_values, residuals, alpha=0.6, color='steelblue')
        axes[0,0].axhline(y=0, color='red', linestyle='--', alpha=0.7)
        axes[0,0].set_xlabel('Fitted Values')
        axes[0,0].set_ylabel('Residuals')
        axes[0,0].set_title('Residuals vs Fitted')
        axes[0,0].grid(True, alpha=0.3)
        
        # Residuals time series
        axes[0,1].plot(residuals.index, residuals.values, color='red', linewidth=1)
        axes[0,1].axhline(y=0, color='black', linestyle='--', alpha=0.7)
        axes[0,1].set_xlabel('Time')
        axes[0,1].set_ylabel('Residuals')
        axes[0,1].set_title('Residuals Over Time')
        axes[0,1].grid(True, alpha=0.3)
        
        # Q-Q plot of residuals
        stats.probplot(residuals.dropna(), dist="norm", plot=axes[1,0])
        axes[1,0].set_title('Q-Q Plot of Residuals')
        
        # Histogram of residuals
        axes[1,1].hist(residuals.dropna(), bins=30, alpha=0.7, color='lightgreen', edgecolor='black')
        axes[1,1].set_xlabel('Residuals')
        axes[1,1].set_ylabel('Frequency')
        axes[1,1].set_title('Distribution of Residuals')
        
        plt.tight_layout()
        plt.savefig(self.output_dir / save_path, bbox_inches='tight')
        plt.show()
    
    def plot_forecast(self, original_series: pd.Series, fitted_values: pd.Series, 
                     forecasts: pd.Series, forecast_ci: Optional[pd.DataFrame] = None,
                     save_path: str = "forecast_plot.png") -> None:
        """Plot forecasts with confidence intervals"""
        fig, ax = plt.subplots(figsize=self.figsize, dpi=self.dpi)
        
        # Plot original series
        ax.plot(original_series.index, original_series.values, 
                label='Actual', linewidth=2, color='blue')
        
        # Plot fitted values
        ax.plot(fitted_values.index, fitted_values.values, 
                label='Fitted', linewidth=1.5, alpha=0.7, color='red')
        
        # Plot forecasts
        forecast_index = range(len(original_series), len(original_series) + len(forecasts))
        ax.plot(forecast_index, forecasts.values, 
                label='Forecast', linewidth=2, color='green', linestyle='--')
        
        # Plot confidence intervals if available
        if forecast_ci is not None:
            ax.fill_between(forecast_index, 
                           forecast_ci.iloc[:, 0], forecast_ci.iloc[:, 1], 
                           alpha=0.3, color='green', label='Confidence Interval')
        
        ax.set_xlabel('Time Period')