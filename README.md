# Automated-Data-Cleaning-Pipeline

## Overview >
This project is an automated data-cleaning pipeline built using Python and Pandas. It streamlines the process of cleaning and preprocessing raw data, making it analysis-ready by removing inconsistencies, handling missing values, and standardizing text and date formats.


## Features
✔️ Supports Multiple File Formats – Loads CSV, Excel, JSON, Pickle, and Parquet files.
✔️ Duplicate Removal – Automatically detects and removes duplicate records.
✔️ Date Standardization – Converts various date formats to a consistent format (YYYY/MM/DD).
✔️ Text Cleaning – Removes special characters, extra spaces, and ensures uniform lowercase formatting.
✔️ Validation & Monitoring – Checks for missing values, incorrect data types, and outliers.
✔️ Scalable & Modular – Uses a pipeline approach, making it easy to extend and customize.

## Project Structure >

📂 Automated-Data-Cleaning
│── 📄 data_loader.py         # Loads data from different file formats
│── 📄 data_validation.py     # Performs data validation and checks
│── 📄 data_cleaning.py       # Cleans duplicate records and standardizes dates
│── 📄 text_cleaning.py       # Cleans text columns and removes unnecessary characters
│── 📄 monitoring.py          # Generates quality metrics for data monitoring
│── 📄 pipeline.py            # Defines and runs the data-cleaning pipeline
│── 📄 main.py                # Main script to execute the pipeline
│── 📄 requirements.txt       # Dependencies list
│── 📄 README.md              # Project documentation

## Usage Example
1. Place your dataset (e.g., movies.csv) in the project directory.
2. The pipeline will:
  Load the dataset.
  Remove duplicates.
  Standardize dates.
  Clean text columns.
  Save the cleaned data as cleaned_data.csv.
3. The script outputs a report of the cleaning steps executed.
