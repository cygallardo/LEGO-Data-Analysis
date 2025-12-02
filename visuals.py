"""Matplotlib visualizations for the project.


Rules: single plot per function; no custom colors (user asked for default palette)
"""
import matplotlib.pyplot as plt
import numpy as np


class Visualizer:
def plot_price_distribution(self, df):
if 'price' not in df.columns:
print('price column not present')
return
prices = df['price'].dropna()
if prices.empty:
print('no price data to plot')
return
plt.figure(figsize=(8,5))
plt.hist(prices, bins=30)
plt.title('Price Distribution')
plt.xlabel('Price')
plt.ylabel('Count')
plt.grid(True)
plt.show()


def plot_avg_price_by_category(self, df, top_n=10):
if 'main_category' not in df.columns or 'price' not in df.columns:
print('required columns not present')
return
grouped = df.groupby('main_category')['price'].mean().dropna().sort_values(ascending=False)
top = grouped.head(top_n)
if top.empty:
print('no data to plot')
return
plt.figure(figsize=(10,6))
plt.bar(
