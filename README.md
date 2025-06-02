# MA4034 Time Series Analysis Assignment

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive time series analysis toolkit for the MA4034 assignment, implementing ARIMA modeling with complete statistical analysis, model diagnostics, and forecasting capabilities.

## 🚀 Features

- **Complete ARIMA Pipeline**: From data exploration to forecasting
- **Automated Model Selection**: Grid search with AIC/BIC optimization
- **Comprehensive Diagnostics**: Ljung-Box, Jarque-Bera, and residual analysis
- **Professional Reporting**: Automated PDF and text report generation
- **Dual Dataset Analysis**: Comparative analysis across multiple datasets
- **Rich Visualizations**: Statistical plots and forecast visualizations
- **Robust Error Handling**: Comprehensive validation and error management

## 📋 Requirements

### System Requirements
- Python 3.8 or higher
- 4GB RAM minimum (8GB recommended)
- 500MB free disk space

### Dependencies
See `requirements.txt` for complete list. Key packages:
- pandas >= 1.3.0
- numpy >= 1.21.0
- matplotlib >= 3.4.0
- statsmodels >= 0.12.0
- scikit-learn >= 1.0.0

## 🛠 Installation

### Method 1: Clone and Install
```bash
git clone https://github.com/yourusername/ma4034-time-series-analysis.git
cd ma4034-time-series-analysis
pip install -r requirements.txt
```

### Method 2: Direct Installation (if packaged)
```bash
pip install ma4034-time-series-analysis
```

## 🏃‍♂️ Quick Start

### Basic Usage
```python
from src.time_series_analyzer import TimeSeriesAnalyzer
import pandas as pd

# Load your data
df = pd.read_excel('data/raw/MA4034_Assignment_S8_20.xlsx')

# Initialize analyzer
analyzer = TimeSeriesAnalyzer(df, column_name='200472B')

# Run complete analysis
analyzer.exploratory_analysis()
analyzer.stationarity_test()
analyzer.make_stationary()
analyzer.identify_order()
analyzer.model_selection()
analyzer.fit_model()
analyzer.model_diagnostics()
analyzer.forecast_and_evaluate()
```

### Command Line Usage
```bash
# Run complete analysis on both datasets
python scripts/run_analysis.py --data data/raw/MA4034_Assignment_S8_20.xlsx --mode complete

# Analyze specific column
python scripts/run_analysis.py --data data/raw/MA4034_Assignment_S8_20.xlsx --column 200472B --mode single
```

## 📊 Data Requirements

### Supported Formats
- Excel files (.xlsx, .xls)
- CSV files (.csv)
- Text files (.txt)

### Data Structure
- Time series data in columns
- Numerical values only
- Missing values handled automatically
- Minimum 30 observations recommended

### Example Data Format
```
Column_Name
12.34
15.67
18.90
...
```

## 📈 Analysis Workflow

1. **Data Loading & Validation**
   - Automatic format detection
   - Missing value handling
   - Data type validation

2. **Exploratory Data Analysis**
   - Descriptive statistics
   - Distribution analysis
   - Time series plotting

3. **Stationarity Testing**
   - Augmented Dickey-Fuller test
   - Automatic differencing if needed
   - Transformation validation

4. **Model Identification**
   - ACF/PACF analysis
   - Automated order selection
   - Grid search optimization

5. **Model Estimation**
   - Maximum likelihood estimation
   - Parameter significance testing
   - Model comparison (AIC/BIC)

6. **Diagnostic Testing**
   - Residual analysis
   - Ljung-Box test
   - Normality testing

7. **Forecasting & Evaluation**
   - Out-of-sample forecasting
   - Performance metrics (MSE, MAE, RMSE)
   - Confidence intervals

## 📁 Output Files

### Generated Reports
- `comprehensive_final_report.pdf` - Complete analysis with all plots
- `comprehensive_final_report.txt` - Text version of the report
- `model_comparison.txt` - Comparative analysis (dual datasets)
- `[dataset]_analysis_report.txt` - Individual dataset reports

### Visualization Files
- `[dataset]_exploratory_analysis.png` - Data exploration plots
- `[dataset]_stationarity_transformation.png` - Stationarity analysis
- `[dataset]_acf_pacf_plots.png` - Autocorrelation analysis
- `[dataset]_model_diagnostics.png` - Diagnostic plots
- `[dataset]_forecast_plot.png` - Forecasting visualization

## 🔧 Configuration

### Analysis Configuration (`config/analysis_config.yaml`)
```yaml
arima_orders:
  p_range: [0, 5]
  d_range: [0, 2] 
  q_range: [0, 5]

forecasting:
  periods: 12
  alpha: 0.05

diagnostics:
  ljung_box_lags: 10
  significance_level: 0.05
```

### Plotting Configuration (`config/plotting_config.yaml`)
```yaml
figure_size: [12, 8]
dpi: 300
style: 'default'
color_palette: 'husl'
```

## 🧪 Testing

Run the test suite:
```bash
pytest tests/ -v --cov=src/
```

Run specific tests:
```bash
pytest tests/test_analyzer.py -v
```

## 📚 Documentation

- [Methodology Guide](docs/methodology.md) - Detailed statistical methodology
- [API Reference](docs/api_reference.md) - Complete code documentation
- [User Guide](docs/user_guide.md) - Comprehensive usage examples

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup
```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install

# Run code formatting
black src/ tests/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- Email: your.email@university.edu
- Student ID: Your_ID
- Course: MA4034 - Time Series Analysis
- University: Your University Name

## 🙏 Acknowledgments

- Course Instructor: [Instructor Name]
- MA4034 Course Materials
- Statsmodels Documentation
- Python Time Series Analysis Community

## 📞 Support

If you encounter any issues or have questions:

1. Check the [documentation](docs/)
2. Search existing [issues](https://github.com/yourusername/ma4034-time-series-analysis/issues)
3. Create a new issue with detailed description
4. Contact the author via email

## 🔄 Version History

- **v1.0.0** - Initial release with complete ARIMA analysis pipeline
- **v1.1.0** - Added comparative analysis for dual datasets
- **v1.2.0** - Enhanced reporting and visualization features

---

*This project is developed as part of the MA4034 Time Series Analysis course assignment.*
