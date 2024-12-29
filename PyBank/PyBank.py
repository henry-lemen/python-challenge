# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = ("PyBank/Resources/budget_data.csv")  # Input file path
file_to_output = ("PyBank/analysis/budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
previous_month_profit = 0
net_change_list = []
greatest_increase = ("", 0)
greatest_decrease = ("", 0)

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    

    # Track the total and net change
    

    # Process each row of data
    for row in reader:

        # Track the total
        total_months += 1
        total_net += int(row[1])
        net_change = int(row[1]) - previous_month_profit

        # Track the net change
        if total_months > 1: 
            net_change = int(row[1]) - previous_month_profit
            net_change_list.append(net_change)

        # Calculate the greatest increase in profits (month and amount)
        if net_change > greatest_increase[1]:
                greatest_increase = (row[0], net_change)
            

        # Calculate the greatest decrease in losses (month and amount)
        if net_change < greatest_decrease[1]:
                greatest_decrease = (row[0], net_change)


# Calculate the average net change across the months
average_net_change = sum(net_change_list) / len(net_change_list) if net_change_list else 0

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net:,.2f}\n"
    f"Average Change: ${average_net_change:,.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]:,.2f})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]:,.2f})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
