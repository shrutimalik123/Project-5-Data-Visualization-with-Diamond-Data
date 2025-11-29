import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the built-in diamonds dataset from Seaborn
df_diamonds = sns.load_dataset('diamonds')

print("--- Diamond Data Overview ---")
print(df_diamonds.head())
print(f"\nDataFrame shape: {df_diamonds.shape}")

# 1. Histogram of Price
plt.figure(figsize=(10, 5))
sns.histplot(df_diamonds['price'], bins=50, kde=True)
plt.title('Distribution of Diamond Prices (USD)')
plt.xlabel('Price ($)')
plt.savefig('histogram_price.png')
plt.close()

# 2. Log-transformed Histogram (Better View of Skewed Data)
plt.figure(figsize=(10, 5))
sns.histplot(df_diamonds['price'], bins=50, kde=True, log_scale=True)
plt.title('Log-Transformed Distribution of Diamond Prices')
plt.xlabel('Price (Log Scale)')
plt.savefig('histogram_price_log.png')
plt.close()

# 3. Bar chart for the 'cut' quality
plt.figure(figsize=(8, 5))
sns.countplot(y='cut', data=df_diamonds, order=df_diamonds['cut'].value_counts().index)
plt.title('Count of Diamonds by Cut Quality')
plt.xlabel('Count')
plt.ylabel('Cut Quality')
plt.savefig('bar_cut_quality.png')
plt.close()

# 4. Scatter plot of Carat vs. Price
plt.figure(figsize=(10, 6))
# Using 'hue' to introduce a third variable (cut) for multivariate context
sns.scatterplot(x='carat', y='price', hue='cut', data=df_diamonds, alpha=0.5, palette='viridis')
plt.title('Relationship Between Carat, Price, and Cut')
plt.xlabel('Carat (Weight)')
plt.ylabel('Price ($)')
plt.legend(title='Cut', loc='upper left')
plt.savefig('scatter_carat_price.png')
plt.close()

# 5. Box plot showing the distribution of Price for each Cut category
plt.figure(figsize=(10, 6))
# Using a log scale on the Y-axis to handle the highly skewed price data
sns.boxplot(x='cut', y='price', data=df_diamonds, order=df_diamonds['cut'].unique())
plt.yscale('log') # Important to better visualize the median and quartiles
plt.title('Price Distribution by Cut Quality (Log Scale)')
plt.xlabel('Cut Quality')
plt.ylabel('Price (Log Scale)')
plt.savefig('boxplot_price_cut.png')
plt.close()
