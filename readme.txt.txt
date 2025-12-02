# DATA3350 Project - Local Python Version


## Folder structure

Project/ │── app.py │── data_loader.py │── cleaning.py │── analysis.py │── visuals.py │── utils.py │── requirements.txt │── README.md └── datasets/ ├── geoMap.csv ├── toy-products-on-amazon-metadata.json └── amazon_co-ecommerce_sample[1].csv


## Setup
1. Create a virtual environment (recommended):
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt


2.Edit BASE_DATA_PATH in app.py if your datasets directory is placed differently.

3.Run the app:
python app.py


Use the interactive menu to load data, clean, analyze, plot, and export results.
