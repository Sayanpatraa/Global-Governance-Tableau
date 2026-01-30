"""
DATS 6401 Project 1 - Data Cleaning Script
This script provides templates for common data cleaning tasks.
Adapt as needed for your specific datasets.
"""

import pandas as pd
import numpy as np
from datetime import datetime

# ============================================================================
# CONFIGURATION
# ============================================================================

# File paths
RAW_DATA_A = '../data/raw/dataset_a_primary.csv'
RAW_DATA_B = '../data/raw/dataset_b_secondary.csv'
PROCESSED_DATA_A = '../data/processed/dataset_a_cleaned.csv'
PROCESSED_DATA_B = '../data/processed/dataset_b_cleaned.csv'
MERGED_DATA = '../data/processed/merged_data.csv'

# ============================================================================
# DATASET A CLEANING
# ============================================================================

def clean_dataset_a():
    """
    Clean and prepare Dataset A (Primary/Fact dataset)
    """
    print("Loading Dataset A...")
    df_a = pd.read_csv(RAW_DATA_A)
    
    print(f"Original shape: {df_a.shape}")
    print(f"Columns: {df_a.columns.tolist()}")
    
    # -------------------------------------------------------------------------
    # 1. Handle Missing Data
    # -------------------------------------------------------------------------
    print("\nChecking for missing data...")
    missing_summary = df_a.isnull().sum()
    print(missing_summary[missing_summary > 0])
    
    # Example: Drop rows with missing values in critical columns
    # df_a = df_a.dropna(subset=['critical_column1', 'critical_column2'])
    
    # Example: Fill missing values with mean/median/mode
    # df_a['numeric_column'].fillna(df_a['numeric_column'].median(), inplace=True)
    # df_a['categorical_column'].fillna('Unknown', inplace=True)
    
    # -------------------------------------------------------------------------
    # 2. Handle Duplicates
    # -------------------------------------------------------------------------
    print("\nChecking for duplicates...")
    duplicates = df_a.duplicated().sum()
    print(f"Number of duplicate rows: {duplicates}")
    
    # Example: Remove duplicates
    # df_a = df_a.drop_duplicates()
    
    # -------------------------------------------------------------------------
    # 3. Clean and Standardize Column Names
    # -------------------------------------------------------------------------
    print("\nStandardizing column names...")
    df_a.columns = df_a.columns.str.lower().str.replace(' ', '_').str.replace('[^a-z0-9_]', '', regex=True)
    print(f"Cleaned columns: {df_a.columns.tolist()}")
    
    # -------------------------------------------------------------------------
    # 4. Parse and Standardize Dates
    # -------------------------------------------------------------------------
    print("\nProcessing date columns...")
    # Example: Convert string to datetime
    # df_a['date_column'] = pd.to_datetime(df_a['date_column'], format='%Y-%m-%d', errors='coerce')
    
    # Example: Extract year, month, quarter
    # df_a['year'] = df_a['date_column'].dt.year
    # df_a['month'] = df_a['date_column'].dt.month
    # df_a['quarter'] = df_a['date_column'].dt.quarter
    
    # -------------------------------------------------------------------------
    # 5. Clean and Standardize Geographic Fields
    # -------------------------------------------------------------------------
    print("\nCleaning geographic fields...")
    # Example: Standardize state names/codes
    # df_a['state'] = df_a['state'].str.upper().str.strip()
    
    # Example: Handle different state formats
    # state_mapping = {
    #     'virginia': 'VA',
    #     'new york': 'NY',
    #     # ... add more mappings
    # }
    # df_a['state_code'] = df_a['state_name'].str.lower().map(state_mapping)
    
    # -------------------------------------------------------------------------
    # 6. Clean Numeric Columns
    # -------------------------------------------------------------------------
    print("\nCleaning numeric columns...")
    # Example: Remove $ and , from currency columns
    # df_a['price'] = df_a['price'].str.replace('$', '').str.replace(',', '').astype(float)
    
    # Example: Handle outliers
    # Q1 = df_a['numeric_column'].quantile(0.25)
    # Q3 = df_a['numeric_column'].quantile(0.75)
    # IQR = Q3 - Q1
    # df_a = df_a[(df_a['numeric_column'] >= Q1 - 1.5*IQR) & (df_a['numeric_column'] <= Q3 + 1.5*IQR)]
    
    # -------------------------------------------------------------------------
    # 7. Clean Categorical Columns
    # -------------------------------------------------------------------------
    print("\nCleaning categorical columns...")
    # Example: Standardize category names
    # df_a['category'] = df_a['category'].str.strip().str.title()
    
    # Example: Combine rare categories
    # category_counts = df_a['category'].value_counts()
    # rare_categories = category_counts[category_counts < 10].index
    # df_a['category'] = df_a['category'].replace(rare_categories, 'Other')
    
    # -------------------------------------------------------------------------
    # 8. Create Derived Variables (if needed)
    # -------------------------------------------------------------------------
    print("\nCreating derived variables...")
    # Example: Calculate per capita rates
    # df_a['rate_per_capita'] = (df_a['count'] / df_a['population']) * 100000
    
    # Example: Create categorical bins
    # df_a['age_group'] = pd.cut(df_a['age'], 
    #                             bins=[0, 18, 35, 50, 65, 100],
    #                             labels=['0-17', '18-34', '35-49', '50-64', '65+'])
    
    # -------------------------------------------------------------------------
    # 9. Validate Data
    # -------------------------------------------------------------------------
    print("\nValidating cleaned data...")
    # Check data types
    print("\nData types:")
    print(df_a.dtypes)
    
    # Check value ranges
    # print("\nValue ranges:")
    # print(df_a.describe())
    
    # -------------------------------------------------------------------------
    # 10. Save Cleaned Data
    # -------------------------------------------------------------------------
    print(f"\nSaving cleaned Dataset A...")
    print(f"Final shape: {df_a.shape}")
    df_a.to_csv(PROCESSED_DATA_A, index=False)
    print(f"Saved to: {PROCESSED_DATA_A}")
    
    return df_a


# ============================================================================
# DATASET B CLEANING
# ============================================================================

def clean_dataset_b():
    """
    Clean and prepare Dataset B (Secondary/Context dataset)
    """
    print("\n" + "="*80)
    print("Loading Dataset B...")
    df_b = pd.read_csv(RAW_DATA_B)
    
    print(f"Original shape: {df_b.shape}")
    print(f"Columns: {df_b.columns.tolist()}")
    
    # Apply similar cleaning steps as Dataset A
    # Adjust based on the specific characteristics of Dataset B
    
    # Clean column names
    df_b.columns = df_b.columns.str.lower().str.replace(' ', '_').str.replace('[^a-z0-9_]', '', regex=True)
    
    # Handle missing data
    # Clean and standardize join key field
    # etc.
    
    # Save cleaned data
    print(f"\nSaving cleaned Dataset B...")
    print(f"Final shape: {df_b.shape}")
    df_b.to_csv(PROCESSED_DATA_B, index=False)
    print(f"Saved to: {PROCESSED_DATA_B}")
    
    return df_b


# ============================================================================
# MERGE DATASETS
# ============================================================================

def merge_datasets(df_a, df_b):
    """
    Merge Dataset A and Dataset B on common key(s)
    """
    print("\n" + "="*80)
    print("Merging datasets...")
    
    # Example: Left join (keep all records from Dataset A)
    # df_merged = pd.merge(df_a, df_b, 
    #                      on='join_key',  # or on=['key1', 'key2'] for multiple keys
    #                      how='left',
    #                      suffixes=('_a', '_b'))
    
    # Example: Inner join (keep only matching records)
    # df_merged = pd.merge(df_a, df_b, 
    #                      on='join_key',
    #                      how='inner')
    
    # Check merge results
    # print(f"\nDataset A records: {len(df_a)}")
    # print(f"Dataset B records: {len(df_b)}")
    # print(f"Merged records: {len(df_merged)}")
    # print(f"Match rate: {len(df_merged)/len(df_a)*100:.1f}%")
    
    # Identify unmatched records
    # unmatched_a = df_a[~df_a['join_key'].isin(df_merged['join_key'])]
    # print(f"\nUnmatched records from A: {len(unmatched_a)}")
    
    # Save merged dataset
    # print(f"\nSaving merged dataset...")
    # df_merged.to_csv(MERGED_DATA, index=False)
    # print(f"Saved to: {MERGED_DATA}")
    
    # return df_merged
    pass


# ============================================================================
# DATA QUALITY REPORT
# ============================================================================

def generate_quality_report(df, dataset_name):
    """
    Generate a data quality report for a dataset
    """
    print(f"\n{'='*80}")
    print(f"DATA QUALITY REPORT: {dataset_name}")
    print('='*80)
    
    print(f"\n1. BASIC INFO")
    print(f"   Shape: {df.shape[0]} rows × {df.shape[1]} columns")
    print(f"   Memory usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
    
    print(f"\n2. MISSING DATA")
    missing = df.isnull().sum()
    missing_pct = (missing / len(df)) * 100
    missing_df = pd.DataFrame({
        'Missing_Count': missing,
        'Missing_Percent': missing_pct
    })
    print(missing_df[missing_df['Missing_Count'] > 0].sort_values('Missing_Count', ascending=False))
    
    print(f"\n3. DATA TYPES")
    print(df.dtypes.value_counts())
    
    print(f"\n4. DUPLICATES")
    print(f"   Total duplicate rows: {df.duplicated().sum()}")
    
    print(f"\n5. NUMERIC COLUMNS SUMMARY")
    print(df.describe())
    
    print(f"\n6. CATEGORICAL COLUMNS")
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols[:5]:  # Show first 5 categorical columns
        print(f"\n   {col}:")
        print(f"   Unique values: {df[col].nunique()}")
        print(f"   Top 5 values:\n{df[col].value_counts().head()}")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """
    Main execution function
    """
    print("="*80)
    print("DATS 6401 PROJECT 1 - DATA CLEANING")
    print("="*80)
    
    # Clean Dataset A
    df_a = clean_dataset_a()
    generate_quality_report(df_a, "Dataset A (Cleaned)")
    
    # Clean Dataset B
    df_b = clean_dataset_b()
    generate_quality_report(df_b, "Dataset B (Cleaned)")
    
    # Merge datasets
    # df_merged = merge_datasets(df_a, df_b)
    # generate_quality_report(df_merged, "Merged Dataset")
    
    print("\n" + "="*80)
    print("DATA CLEANING COMPLETE!")
    print("="*80)
    print("\nNext steps:")
    print("1. Review cleaned datasets in data/processed/")
    print("2. Import cleaned data into Tableau")
    print("3. Create visualizations")
    print("4. Build dashboard")


if __name__ == "__main__":
    main()
