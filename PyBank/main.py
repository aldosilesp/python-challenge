import csv
import os
import pandas as pd

data_file = "/Users/aldosilva/python-challenge/PyBank/Resources/budget_data.csv"
data_file_df = pd.read_csv(data_file)
data_file_df.head()

data_file_df.describe()

net = data_file_df["Profit/Losses"].sum()
print(net)

count = data_file_df["Profit/Losses"].count()
print(count)

data_file_df['Diff'] = data_file_df['Profit/Losses'] - data_file_df['Profit/Losses'].shift(1)
data_file_df

diff_average = data_file_df["Diff"].mean()
print(diff_average)

greatest_increase = data_file_df["Diff"].max()
print(greatest_increase)

greatest_decrease = data_file_df["Diff"].min()
print(greatest_decrease)

summary_df = pd.DataFrame({
    "Total Months" : [count],
    "Total" : [net],
    "Average Change" : [diff_average],
    "Greatest Increase in Profits" : [greatest_increase],
    "Greatest Decrease in Profits" : [greatest_decrease]
})
summary_df

summary_df.to_csv('/Users/aldosilva/python-challenge/PyBank/analysis/results.csv', index=None)