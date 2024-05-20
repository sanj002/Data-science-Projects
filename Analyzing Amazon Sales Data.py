# Import necessary libraries
import pandas as pd

# Load the Amazon dataset
df = pd.read_csv('Downloads/Amazon Sales data.csv')

# Convert 'Order Date' to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Extract month, year, and yearly-month from 'Order Date'
df['Month'] = df['Order Date'].dt.month
df['Year'] = df['Order Date'].dt.year
df['Year-Month'] = df['Order Date'].dt.to_period('M')

# Calculate sales trend month-wise
monthly_sales = df.groupby('Month')['Total Revenue'].sum()

# Calculate sales trend year-wise
yearly_sales = df.groupby('Year')['Total Revenue'].sum()

# Calculate sales trend yearly-month-wise
yearly_monthly_sales = df.groupby('Year-Month')['Total Revenue'].sum()

# Display the sales trends
print("Month-wise Sales Trend:")
print(monthly_sales)

print("\nYear-wise Sales Trend:")
print(yearly_sales)

print("\nYearly-Month-wise Sales Trend:")
print(yearly_monthly_sales)
