import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.preprocessing import StandardScaler

from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import psycopg2
import numpy as np


def list_missing_values(df):
    """
    Finds missing values and returns a summary.

    Args:
        df: The DataFrame to check for missing values.

    Returns:
        A summary of missing values, including the number of missing values per column.
    """

    null_counts = df.isnull().sum()
    missing_value = null_counts
    percent_of_missing_value = 100 * null_counts / len(df)
    data_type=df.dtypes

    missing_data_summary = pd.concat([missing_value, percent_of_missing_value,data_type], axis=1)
    missing_data_summary_table = missing_data_summary.rename(columns={0:"Missing values", 1:"Percent of Total Values",2:"DataType" })
    missing_data_summary_table = missing_data_summary_table[missing_data_summary_table.iloc[:, 1] != 0].sort_values('Percent of Total Values', ascending=False).round(1)

    print(f"From {df.shape[1]} columns selected, there are {missing_data_summary_table.shape[0]} columns with missing values.")

    return missing_data_summary_table


# Define a function to identify outliers using the IQR method
def identify_outliers_iqr(df):
    outlier_indices = []
    
    for col in df.select_dtypes(include=['float64', 'int64']).columns:  # Only consider numerical columns
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        
        # Define the lower and upper bounds
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        # Find outliers
        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
        outlier_indices.extend(outliers.index.tolist())
        
        # Print summary
        print(f'Column: {col}')
        print(f'Outliers: {outliers[col].count()}')
        print(f'Lower Bound: {lower_bound}, Upper Bound: {upper_bound}')
        print('-' * 30)

    return outlier_indices


def visualize_outlies(df):
    # Select only the numerical columns
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns

    # Calculate the number of rows and columns for the subplot grid
    num_cols = 3  # Number of columns for subplots
    num_rows = (len(numerical_cols) + num_cols - 1) // num_cols  # Calculate number of rows needed

    plt.figure(figsize=(15, 5 * num_rows))  # Adjusting the figure size

    for i, col in enumerate(numerical_cols):
        plt.subplot(num_rows, num_cols, i + 1)  # Creating subplots
        sns.boxplot(x=df[col])  # Boxplot for each numerical column
        plt.title(f'Box plot for {col}')  # Title for each subplot

    plt.tight_layout()  # Adjust layout to prevent overlap
    plt.show()  # Display the plots
    
    

def user_aggregation(df_cleaned):
    user_aggregation = df_cleaned.groupby(['IMSI', 'MSISDN/Number']).agg(
        number_of_sessions=('Bearer Id', 'count'),
        total_session_duration=('Dur. (ms)', 'sum'),
        total_DL_data=('Total DL (Bytes)', 'sum'),
        total_UL_data=('Total UL (Bytes)', 'sum'),
        total_HTTP_DL_data=('HTTP DL (Bytes)', 'sum'),
        total_HTTP_UL_data=('HTTP UL (Bytes)', 'sum'),
        total_Social_Media_DL_data=('Social Media DL (Bytes)', 'sum'),
        total_Social_Media_UL_data=('Social Media UL (Bytes)', 'sum')
    ).reset_index()
    print(user_aggregation)
    
    
def seg_user_into_deciles(df_cleaned):
    # Create a new column for total data (DL + UL)
    df_cleaned['Total Data (Bytes)'] = df_cleaned['Total DL (Bytes)'] + df_cleaned['Total UL (Bytes)']

    # Calculate the decile classes based on the total session duration
    df_cleaned['Decile Class'] = pd.qcut(df_cleaned['Dur. (ms)'], 10, labels=False)  # 0-9 labels

    # Group by Decile Class to compute total data
    decile_summary = df_cleaned.groupby('Decile Class')['Total Data (Bytes)'].sum().reset_index()

    print("Total Data per Decile Class:")
    print(decile_summary)



