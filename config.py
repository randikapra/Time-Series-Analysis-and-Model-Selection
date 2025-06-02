"""Configuration settings for time series analysis"""

# Analysis Parameters
FORECAST_PERIODS = 12
SIGNIFICANCE_LEVEL = 0.05
MAX_AR_ORDER = 5
MAX_MA_ORDER = 5
MAX_DIFF_ORDER = 2

# Visualization Settings
FIGURE_SIZE = (12, 8)
DPI = 300
PLOT_STYLE = 'default'

# File Paths
DATA_DIR = 'data'
OUTPUT_DIR = 'outputs'
PLOTS_DIR = 'outputs/plots'
REPORTS_DIR = 'outputs/reports'