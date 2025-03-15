import pandas as pd
from datetime import datetime
import calendar

def remove_duplicates(df):
    """Remove duplicate rows from the dataframe."""
    return df.drop_duplicates()

def fix_invalid_dates(year, month, day):
    """Fix invalid months and days in a date."""
    # Ensure the month is in the valid range (1-12)
    month = max(1, min(12, month))

    # Ensure the day is within the valid range of that month
    max_day = calendar.monthrange(year, month)[1]  # Get last valid day of the month
    day = max(1, min(max_day, day))

    return f"{year:04d}/{month:02d}/{day:02d}"  # Return formatted date

def standardize_date(date_str):
    """
    Standardizes a single date string to YYYY/MM/DD format.
    If the date is invalid, it tries to fix it. If it cannot be fixed, it returns NaN.
    """
    # List of possible date formats to try
    date_formats = [
        '%Y-%m-%d', '%m-%d-%Y', '%d-%m-%Y',  # Common date formats
        '%Y/%m/%d', '%m/%d/%Y', '%d/%m/%Y',  # Slash-separated formats
        '%Y%m%d'  # Format for YYYYMMDD (e.g., 20210615)
    ]

    for fmt in date_formats:
        try:
            # Try to parse the date with the current format
            date_obj = datetime.strptime(str(date_str), fmt)
            # If successful, return the date in the standard format YYYY/MM/DD
            return date_obj.strftime('%Y/%m/%d')
        except ValueError:
            continue

    # If parsing fails, try to fix the date manually
    try:
        # Extract numeric parts (assuming YYYYMMDD format if possible)
        clean_str = ''.join(filter(str.isdigit, str(date_str)))  # Remove any non-numeric characters
        if len(clean_str) == 8:  # Expecting YYYYMMDD format
            year, month, day = int(clean_str[:4]), int(clean_str[4:6]), int(clean_str[6:])
            return fix_invalid_dates(year, month, day)

    except Exception:
        pass  # If it can't be fixed, return NaN

    return pd.NaT  # If completely invalid, return NaN

def standardize_dates(df):
    """Apply date standardization to the 'joining_date' column."""
    if 'joining_date' in df.columns:
        df['joining_date'] = df['joining_date'].apply(lambda x: standardize_date(x) if pd.notna(x) else pd.NaT)

    return df


# def remove_duplicates(df):
#     """Remove duplicate rows from the dataframe."""
#     return df.drop_duplicates()

# def standardize_dates(df):
#     """
#     Convert date columns to a standard format (YYYY-MM-DD).
#     If the date is invalid, it remains unchanged.
#     """
#     def standardize_date(date_str):
#         """
#         Standardizes a single date string to YYYY-MM-DD format.
#         If the date is invalid, returns the original string.
#         """
#         # List of possible date formats to try
#         date_formats = [
#             '%Y-%m-%d', '%m-%d-%Y', '%d-%m-%Y',  # Common date formats
#             '%Y/%m/%d', '%m/%d/%Y', '%d/%m/%Y',  # Slash-separated formats
#             '%Y%m%d'  # Format for YYYYMMDD (e.g., 20210615)
#         ]

#         for fmt in date_formats:
#             try:
#                 # Try to parse the date with the current format
#                 date_obj = datetime.strptime(str(date_str), fmt)
#                 # If successful, return the date in the standard format
#                 return date_obj.strftime('%Y-%m-%d')
#             except ValueError:
#                 continue

#         # If none of the formats work, return the original string
#         return date_str

#     # Identify columns that are likely to contain dates
#     # Include both object and numeric columns (e.g., joining_date as int)
#     date_columns = [col for col in df.columns if df[col].dtype in ['object', 'int', 'float']]

#     for col in date_columns:
#         # Apply the standardize_date function to each value in the column
#         df[col] = df[col].apply(lambda x: standardize_date(x) if pd.notna(x) else x)

#     return df