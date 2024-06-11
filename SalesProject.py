# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 23:04:11 2024

@author: Gaxton Okobah

How many sales have they made with amounts more than 1000
How many sales have they made that belong to the Category "Tops" and have a Quantity of 3.
The Total Sales by Category
Average Amount by Category and Status
Total Sales by Fulfilment and Shipment Type
"""

import pandas as pd
#Load the sales data from the excel file into a pandas Dataframe

sales_data = pd.read_excel('sales_data.xlsx')

# =============================================================================
# Exploring the data
# =============================================================================

#get summary of sales data
sales_data.info()

sales_data.describe()

#looking at columns
print(sales_data.columns)

#having a look at the first rows of data

print(sales_data.head())

#check data types of columns
print(sales_data.dtypes)

# =============================================================================
# Cleaning the data
# =============================================================================

#Check for missing values in our sales data
print(sales_data.isnull().sum())

#drop any row that has missing values
sales_data_dropped = sales_data.dropna()

#drop rows with missing amounts based on the amopunt column
sales_data_cleaned = sales_data.dropna(subset =['Amount'])

#Check for missing values in our sales data cleaned
print(sales_data_cleaned.isnull().sum())

# =============================================================================
# Slicing and filtering Data
# =============================================================================

#Select a subset of our data based on the Category Column
category_data = sales_data[sales_data["Category"]== 'Top']
print(category_data)

#Select subset of data where the amount > 1000
high_amount_data = sales_data[sales_data['Amount'] > 1000]
print(high_amount_data)

#select a subset of data based on multiple conditions
filetered_data = sales_data[(sales_data['Category'] == 'Top') & (sales_data['Qty'] ==3)]


# =============================================================================
# Aggregating Data
# =============================================================================
#total sales by category
category_totals = sales_data.groupby('Category')['Amount'].sum()
category_totals = sales_data.groupby('Category', as_index=False)['Amount'].sum()
category_totals = category_totals.sort_values('Amount', ascending=False)

#calculate the average Amount by Category and fulfilment
fulfilment_average = sales_data.groupby(['Category', 'Fulfilment'], as_index=False)['Amount'].mean()
fulfilment_average = fulfilment_average.sort_values('Amount', ascending=False)

#Calculate the average amount by category and Status
status_averages = sales_data.groupby(['Category', 'Status'], as_index=False)['Amount'].mean()
status_averages = status_averages.sort_values('Amount', ascending=False)

#calculate total sales by shipment

total_sales_shipandful = sales_data.groupby(['Courier Status', 'Fulfilment'], as_index=False)['Amount'].sum()
total_sales_shipandful = total_sales_shipandful.sort_values('Amount', ascending=False)
total_sales_shipandful.rename(columns={'Courier Status' : 'Shipment'},inplace = True)

# =============================================================================
# Exporting Data
# =============================================================================
status_averages.to_excel('average_sales_by_category_and_status.xlsx', index=False)
total_sales_shipandful.to_excel('total_sales_by_ship_and_fulfil.xlsx', index=False)
























