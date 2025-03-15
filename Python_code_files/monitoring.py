import pandas as pd # type: ignore

def generate_quality_metrics(df,baseline_metrics = None):

    metrics = {
        'row_count': len(df),
        'missing_values': df.isna().sum().to_dict(),
        'unique_values': df.nunique().to_dict(),
        'data_types': df.dtypes.astype(str).to_dict()

    }

    # Descriptive stats for numeric column
    numeric_columns = df.select_dtypes(include=['numbers']).columns
    metrics['numeric_stats'] = df[numeric_columns].describe().to_dict()

    #compare with baseline metric if provided
    if baseline_metrics:

        metrics['changes'] = {
            'row_count_change': metrics['row_count'] - baseline_metrics['row_count'],
            'missing_value_change': {
                col: metrics['missing_values'][col] - baseline_metrics['missing_values'][col]
                for col in metrics['missing_values']
            }
        }
    return metrics