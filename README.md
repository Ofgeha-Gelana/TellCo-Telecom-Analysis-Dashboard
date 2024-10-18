# Customer Engagement Metrics & K-Means Clustering Analysis

This project analyzes customer engagement metrics based on upload and download traffic across various applications (Google, Email, Youtube, Netflix, Gaming, Other) using k-means clustering. The goal is to classify users based on their engagement levels and provide insights into customer behavior.

## Project Overview

The following tasks are performed:

1. **Aggregate Customer Engagement Metrics**: 
   - Aggregation of upload and download traffic (in bytes) for each application per customer (MSISDN).
   - Reporting the top 10 customers per engagement metric.

2. **Normalize Engagement Metrics and K-Means Clustering**:
   - Normalization of engagement metrics.
   - Running K-means clustering to classify customers into 3 groups based on their engagement levels.
   - Analysis of the minimum, maximum, average, and total engagement metrics for each cluster.

3. **User Engagement by Application**:
   - Aggregation of user total traffic per application.
   - Identifying the top 10 most engaged users per application.

4. **Visualize the Top 3 Most Used Applications**:
   - Plotting the top 3 most used applications based on total traffic.

5. **Optimizing Number of Clusters (Elbow Method)**:
   - Determining the optimal number of clusters (k) using the elbow method.

## Project Structure

```bash
|-- data/               # Directory containing your dataset
|-- src/                # Source code directory
|   |-- aggregation.py   # Script to aggregate metrics per customer
|   |-- clustering.py    # Script to normalize data and perform K-means clustering
|   |-- visualization.py # Script to plot application usage and elbow method
|-- README.md           # This file
