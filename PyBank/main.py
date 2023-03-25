# The total number of months included in the dataset
    # counter; for loop on csv record and count how many records there are
    # start counter at zero, for loop +1
# The net total amount of "Profit/Losses" over the entire period
    # for loop, add a specific column to a total variable
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
    # calculate total, then average changes
# The greatest increase in profits (date and amount) over the entire period
    # find the greatest increase, then store; loop one by one to find the next GI, storing as
    # a new GI value is found
# The greatest decrease in profits (date and amount) over the entire period
    # find the greatest decrease, then store; loop one by one to find the next GD, storing as
    # a new GD value is found

# Step 1: read the CSV file
import os
import csv

# Variables
total_months = 0
net_total = 0
current_month_PL = 0

csvpath = os.path.join("/Users/jennabarkley/Desktop/Challenges/Python-Challenge/PyBank/Resources/budget_data.csv")

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)
    # Save the header, and read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}") #if needed

# Read each row of data after the header
    for row in csvreader:
        # print(row)

    # Step 2: The total number of months included in the dataset
        total_months+= 1
        # print(f"Total Months:  {total_months}")
    
    # Step 3: The net total amount of "Profit/Losses" over the entire period
        current_month_PL = int(row[1])
        net_total += current_month_PL
        # print(net_total)
            

