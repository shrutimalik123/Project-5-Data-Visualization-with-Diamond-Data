# Project-5-Data-Visualization-with-Diamond-Data
Project 5: Data Visualization with Diamond Data

Objective

The goal is to load the well-known "Diamonds" dataset, and use Matplotlib and Seaborn to perform univariate and bivariate explorations of key features like price, carat, and cut.

## Installation

To run this project, you need to have Python installed along with the following libraries:

```bash
pip install pandas seaborn matplotlib
```

## Usage

Run the analysis script to load the data and generate visualizations:

```bash
python analyze_diamonds.py
```

## Results

The script generates the following visualizations:

### Price Distribution
![Price Distribution](histogram_price.png)

### Log-Transformed Price Distribution
![Log-Transformed Price Distribution](histogram_price_log.png)

### Cut Quality Distribution
![Cut Quality Distribution](bar_cut_quality.png)

### Carat vs Price Scatter Plot
![Carat vs Price Scatter Plot](scatter_carat_price.png)

### Price Distribution by Cut Quality
![Price Distribution by Cut Quality](boxplot_price_cut.png)
