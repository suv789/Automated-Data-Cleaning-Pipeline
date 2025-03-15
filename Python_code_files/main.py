from data_loader import load_dataset
from data_cleaning import remove_duplicates,standardize_dates
from text_cleaning import clean_text_columns
from pipeline import DataCleaningPipeline


# load dataset
df = load_dataset('movies.csv')

#create pipeline
pipeline = DataCleaningPipeline()
pipeline.add_step('remove_duplicates', remove_duplicates)
pipeline.add_step('standardize_dates', standardize_dates)
pipeline.add_step('clean_text_columns', clean_text_columns)

# Execute pipeline
cleaned_df, results = pipeline.execute(df)

for result in results:
    print(result)

# Save the cleaned dataset
cleaned_df.to_csv("cleaned_data.csv", index=False)  
print("Cleaned data saved as cleaned_data.csv")