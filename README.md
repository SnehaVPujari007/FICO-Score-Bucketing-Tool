# FICO Score Bucketing Tool

Creates 10 quantile-based rating buckets from FICO scores with default rate analysis.

## Requirements
- pandas

## Usage

1. Install pandas: `pip install pandas`
2. Update CSV file path in script if needed
3. Run: `python task4.py`

## Input Data
CSV file with:
- `fico_score`: Credit scores
- `default`: Binary (1=default, 0=no default)

## Output Files
- `fico_rating_map.csv`: Individual records with ratings
- `bucket_summary.csv`: Bucket statistics and default rates

## Rating System
- **Rating 0**: Highest FICO scores (lowest risk)
- **Rating 9**: Lowest FICO scores (highest risk)

## Configuration
Change `n_buckets = 10` to modify number of buckets.
