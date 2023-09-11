import pandas as pd

# Extract data from csv
data = pd.read_csv('daily_sales.csv')
print(data)

# Transform data: Calculate total sales per day
total_sales = data.groupby('Date').Amount.sum().reset_index()
print(total_sales)

# Load data into new CSV
# total_sales.to_csv('total_daily_sales.csv', index=False)

daily_sales_data = pd.read_csv('total_daily_sales.csv')
