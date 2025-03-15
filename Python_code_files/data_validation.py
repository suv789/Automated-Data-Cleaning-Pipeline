import pandas as pd

def validate_dateset(df,validation_rules=None):
    ''''Apply validation rules to a dataframe and return validation results.'''
    if validation_rules is None:
        validation_rules = {
            'numeric_columns': {'check_type': 'numeric','min_value': 0, 'max_value': 1000000},
            'date_columns': {'check_type': 'date','date_format': '%Y-%m-%d'},
        }

    validation_results = {}

    for column, rules in validation_rules.items():
        if column not in df.columns:
            continue
        issues = []

        # check for missing values
        missing_count = df[column].isnull().sum()
        if missing_count > 0:
            issues.append(f'{missing_count} missing values')

        # Numeric Validation
        if rules['check_type'] == 'numeric':
            if not pd.api.types.is_numeric_dtype(df[column]):
                issues.append('non-numeric values found')
            else:
                out_of_range = df[(df[column] < rules['min_value']) | (df[column] > rules['max_value'])]
                if len(out_of_range) > 0:
                    issues.append(f'{len(out_of_range)} out of range values')
        
        validation_results[column] = issues
    
    return validation_results