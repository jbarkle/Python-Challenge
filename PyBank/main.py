# The total number of months included in the dataset
    # counter; for loop on csv record and count how many records there are
    # start counter at zero, for loop +1
# The net total amount of "Profit/Losses" over the entire period
    # for loop, add a specific column (index 1) to a total variable
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
    # calculate total, then average changes; store months and profit loss changes in a list
    # update previous month to current month for each iteration
# The greatest increase in profits (date and amount) over the entire period
    # find the max value in the profit loss change list, retrieve with month value in list
# The greatest decrease in profits (date and amount) over the entire period
    # find the min value in the profit loss change list, retrieve with month value in list

# Step 1: read the CSV file
import os
import csv

# Variables
total_months = 0
net_total = 0
PL_change = 0
previous_month_PL = 0
current_month_PL = 0
months = []
PL_changes = []

csvpath = os.path.join("/Users/jennabarkley/Desktop/Challenges/Python-Challenge/PyBank/Resources/budget_data.csv")

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)
    # Save the header, and read the header row first
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}") if needed

# Read each row of data after the header
    for row in csvreader:
        # print(row)

    # Step 2: The total number of months included in the dataset
        total_months+= 1
    
    # Step 3: The net total amount of "Profit/Losses" over the entire period
        current_month_PL = int(row[1])
        net_total += current_month_PL

    # Step 4: The changes in "Profit/Losses" over the entire period, and then the average of those changes
        if (total_months == 1):
            previous_month_PL = current_month_PL
            continue
        else: #track changes in profit loss and append to profit loss list and month list
            PL_change = current_month_PL - previous_month_PL
            months.append(row[0])
            PL_changes.append(PL_change)
            #update previous month to current month
            previous_month_PL = current_month_PL
    # sum/avg changes
    sum_PL = sum(PL_changes)
    avg_PL_change = sum_PL / (total_months - 1)
    
