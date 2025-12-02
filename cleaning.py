"""Cleaning helpers for the amazon dataset and toy JSON.


def parse_price(x):
# handle None/NaN early
if pd.isna(x):
return None
s = str(x).replace('£', '').replace('$', '').replace(',', '').strip()
# if contains range like "269.00 - 699.99"
if '-' in s:
parts = [p.strip() for p in s.split('-') if p.strip()]
try:
low = float(parts[0])
high = float(parts[1]) if len(parts) > 1 else low
return (low + high) / 2
except:
return None
try:
return float(s)
except:
return None


class Cleaner:
def normalize_toy_json(self, toy_json: dict) -> pd.DataFrame:
# expects the structure from your toy-products json
# recordSet -> [ { 'field': [...] } ]
record_set = toy_json.get('recordSet')
if not record_set:
raise ValueError('toy json missing recordSet')
# 'field' likely contains the actual list of product dicts
record = record_set[0]
fields = record.get('field', [])
return pd.json_normalize(fields)


def clean_amazon_df(self, df: pd.DataFrame) -> pd.DataFrame:
df = df.copy()
# rating
if 'average_review_rating' in df.columns:
df['rating'] = df['average_review_rating'].astype(str).str.extract(r'([\d\.]+)')[0]
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')


# price
if 'price' in df.columns:
df['price'] = df['price'].apply(parse_price)


# split categories
if 'amazon_category_and_sub_category' in df.columns:
parts = df['amazon_category_and_sub_category'].str.split('>', n=1, expand=True)
if parts.shape[1] == 2:
df['main_category'] = parts[0].str.strip()
df['sub_category'] = parts[1].str.strip()
else:
df['main_category'] = parts[0].str.strip()
df['sub_category'] = None


# fill textual missing values with placeholder
text_cols = [
'customers_who_bought_this_item_also_bought',
'items_customers_buy_after_viewing_this_item',
'customer_reviews'
]
for c in text_cols:
if c in df.columns:
df[c] = df[c].fillna('None')


return df
