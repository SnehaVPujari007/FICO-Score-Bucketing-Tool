
import pandas as pd

# Load your dataset
df = pd.read_csv("Task 3 and 4_Loan_Data.csv")  # Update path as needed

# Define number of buckets
n_buckets = 10

# Quantile-based bucketing
df['quantile_rating'], quantile_bins = pd.qcut(df['fico_score'], q=n_buckets, labels=False, retbins=True, duplicates='drop')

# Reverse rating: lower score = better rating
df['quantile_rating'] = n_buckets - 1 - df['quantile_rating']

# Save the rating map to a CSV file
rating_map = df[['fico_score', 'quantile_rating', 'default']]
rating_map.to_csv("fico_rating_map.csv", index=False)

# Summarize the buckets
bucket_summary = df.groupby('quantile_rating').agg(
    min_fico=('fico_score', 'min'),
    max_fico=('fico_score', 'max'),
    avg_fico=('fico_score', 'mean'),
    default_rate=('default', 'mean'),
    count=('default', 'count')
).reset_index()

bucket_summary.to_csv("bucket_summary.csv", index=False)

print("Bucket summary:")
print(bucket_summary)
