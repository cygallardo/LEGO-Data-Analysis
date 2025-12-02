"""Functions that perform analysis on cleaned DataFrames.
"""
import pandas as pd


class Analyzer:
def top_rated_products(self, df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
if 'rating' not in df.columns:
raise ValueError('rating column not found')
return df.sort_values(by='rating', ascending=False).head(top_n)


def avg_price_by_category(self, df: pd.DataFrame) -> pd.Series:
if 'main_category' not in df.columns:
raise ValueError('main_category column not found')
return df.groupby('main_category')['price'].mean().sort_values(ascending=False)


def count_missing_reviews(self, df: pd.DataFrame) -> int:
if 'customer_reviews' in df.columns:
return (df['customer_reviews'] == 'None').sum()
return df['customer_reviews'].isna().sum()
