# Time Series Analysis and Model Selection

A comprehensive, modular time series analysis toolkit designed for ARIMA modeling, forecasting, and statistical evaluation of time series data.

## 🎯 Project Overview

This project provides a complete framework for time series analysis including:
- **Data Loading & Preprocessing**: Excel/CSV data handling with validation
- **Exploratory Analysis**: Descriptive statistics and visualization
- **Stationarity Testing**: ADF tests with automatic differencing
- **Model Selection**: ARIMA order identification using AIC/BIC
- **Diagnostics**: Residual analysis and model validation
- **Forecasting**: Out-of-sample predictions with evaluation metrics
- **Reporting**: Automated report generation with visualizations

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/randikapra/Time-Series-Analysis-and-Model-Selection.git
cd time_series_analysis

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

```python
from src.data_loader import DataLoader
from src.time_series_analyzer import TimeSeriesAnalyzer
from src.report_generator import ReportGenerator

# Load your data
loader = DataLoader()
df = loader.load_excel_data('data/raw/your_data.xlsx')

# Run analysis
analyzer = TimeSeriesAnalyzer(df, 'your_column')
results = analyzer.run_complete_analysis()

# Generate reports
reporter = ReportGenerator()
reporter.generate_comprehensive_report(results)
```

## 📊 Features

### Core Analysis Features
- ✅ **Automated Stationarity Testing** - ADF test with auto-differencing
- ✅ **ARIMA Model Selection** - Grid search with AIC/BIC optimization
- ✅ **Comprehensive Diagnostics** - Ljung-Box, Jarque-Bera tests
- ✅ **Forecast Evaluation** - MSE, MAE, RMSE metrics
- ✅ **Visual Analytics** - 15+ plot types for complete analysis

### Advanced Features
- 🔄 **Multi-Dataset Comparison** - Compare models across datasets
- 📈 **Automated Forecasting** - 12-period ahead predictions
- 📊 **Interactive Visualizations** - High-quality matplotlib/seaborn plots
- 📋 **Professional Reporting** - PDF reports with embedded plots
- 🧪 **Statistical Validation** - Comprehensive model diagnostics

## 📁 Project Structure

```
time_series_analysis/
├── src/                    # Core analysis modules
├── utils/                  # Utility functions
├── data/                   # Data storage
├── outputs/                # Generated results
├── notebooks/              # Jupyter notebooks
└── tests/                  # Unit tests
```

## 🔧 Configuration

Edit `config.py` to customize:

```python
# Analysis parameters
FORECAST_PERIODS = 12
SIGNIFICANCE_LEVEL = 0.05
MAX_AR_ORDER = 5
MAX_MA_ORDER = 5

# Output settings
FIGURE_SIZE = (12, 8)
DPI = 300
PLOT_STYLE = 'seaborn-v0_8'
```

## 📖 Usage Examples

### 1. Single Dataset Analysis

```python
# Load and analyze single time series
analyzer = TimeSeriesAnalyzer(df, 'sales_data')
results = analyzer.run_complete_analysis()

print(f"Best Model: ARIMA{results['best_order']}")
print(f"AIC: {results['aic']:.4f}")
```

### 2. Multi-Dataset Comparison

```python
# Compare multiple datasets
from src.model_comparator import ModelComparator

comparator = ModelComparator()
comparison = comparator.compare_datasets([df1, df2], 'target_column')
comparator.generate_comparison_report(comparison)
```

### 3. Custom Analysis Pipeline

```python
# Build custom analysis pipeline
analyzer = TimeSeriesAnalyzer(df, 'column_name')

# Step-by-step analysis
analyzer.exploratory_analysis()
analyzer.stationarity_test()
analyzer.identify_order()
analyzer.fit_model()
analyzer.model_diagnostics()
forecasts = analyzer.forecast_and_evaluate()
```

## 📊 Generated Outputs

### Visualizations
- **Exploratory Plots**: Time series, distributions, seasonality
- **Stationarity Plots**: Before/after differencing comparisons
- **ACF/PACF Plots**: Correlation function analysis
- **Diagnostic Plots**: Residual analysis, Q-Q plots
- **Forecast Plots**: Predictions with confidence intervals

### Reports
- **Analysis Reports**: Detailed statistical summaries
- **Comparison Reports**: Multi-dataset model comparisons
- **PDF Reports**: Professional documents with embedded plots
- **Summary Statistics**: Key metrics and findings

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
python -m pytest tests/

# Run specific test
python -m pytest tests/test_analyzer.py

# Run with coverage
python -m pytest tests/ --cov=src
```

## 📚 Dependencies

### Core Libraries
- `pandas` >= 1.5.0 - Data manipulation
- `numpy` >= 1.21.0 - Numerical computing
- `statsmodels` >= 0.13.0 - Statistical modeling
- `scikit-learn` >= 1.1.0 - Machine learning metrics

### Visualization
- `matplotlib` >= 3.5.0 - Plotting
- `seaborn` >= 0.11.0 - Statistical visualization

### Additional
- `scipy` >= 1.9.0 - Scientific computing
- `jupyter` >= 1.0.0 - Notebook environment

## 🎯 Academic Use

This project is designed for academic assignments and research. Features include:

- **Reproducible Analysis**: Consistent methodology across datasets
- **Statistical Rigor**: Proper hypothesis testing and validation
- **Professional Reporting**: Academic-standard documentation
- **Modular Design**: Easy to extend and customize

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔍 Troubleshooting

### Common Issues

**Data Loading Problems**
```python
# Ensure correct file path and format
loader = DataLoader()
loader.validate_data_format('your_file.xlsx')
```

**Model Convergence Issues**
```python
# Try different starting parameters
analyzer.fit_model(method='css-mle', maxiter=1000)
```

**Memory Issues with Large Datasets**
```python
# Use chunked processing
analyzer.process_in_chunks(chunk_size=1000)
```

## 📞 Support

For questions and support:
- Create an issue on GitHub
- Check the documentation in `/docs`
- Review example notebooks in `/notebooks`

---

**Built for MA4034 Time Series Analysis Assignment**  
*Professional, modular, and academically rigorous time series analysis toolkit*
