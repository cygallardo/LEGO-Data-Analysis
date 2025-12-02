"""Load CSV and JSON files from the datasets folder.


Functions return pandas DataFrames (for CSV) or raw JSON (dict) for JSON files.
"""
from pathlib import Path
import pandas as pd
import json


class DataLoader:
def __init__(self, base_path: Path):
self.base_path = Path(base_path)


def _path(self, filename: str) -> Path:
return self.base_path / filename


def load_csv(self, filename: str) -> pd.DataFrame:
p = self._path(filename)
if not p.exists():
raise FileNotFoundError(f"CSV not found: {p}")
return pd.read_csv(p)


def load_json(self, filename: str) -> dict:
p = self._path(filename)
if not p.exists():
raise FileNotFoundError(f"JSON not found: {p}")
with open(p, 'r', encoding='utf-8') as f:
return json.load(f)
