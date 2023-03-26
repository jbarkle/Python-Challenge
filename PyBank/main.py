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
    
    # Step 5 & 6: The greatest increase & decrease in profits (date and amount) over the entire period
    # find the greatest increase/decrease in the list using max/min
    greatest_increase = max(PL_changes)
    greatest_decrease = min(PL_changes)
    # find the indices of increase/decrease in the list
    increase_month = PL_changes.index(greatest_increase)
    decrease_month = PL_changes.index(greatest_decrease)
    # store the month values to retrieve with greatest increase/decrease
    GI_month = months[increase_month]
    GD_month = months[decrease_month]

# Step 7: Print an analysis to terminal
print("Financial Analysis")
print("---------------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${int((100*avg_PL_change-0.5)) / 100}")
print(f"Greatest Increase in Profits: {GI_month} (${greatest_increase})")
print(f"Greatest Decrease in Losses: {GD_month} (${greatest_decrease})")

# Step 8: Save as a txt file
# specify the file to write to
output_file = os.path.join("/Users/jennabarkley/Desktop/Challenges/Python-Challenge/PyBank/Analysis/financial_analysis.txt")

# open file using write mode, specify variable to hold contents
with open(output_file, 'w') as text:
    # write contents, don't forget to end each line with \n
    text.write("Financial Analysis\n")
    text.write("---------------------------------------------------\n")
    text.write(f"Total Months: {total_months}\n")
    text.write(f"Total: ${net_total}\n")
    text.write(f"Average Change: ${int((100*avg_PL_change-0.5)) / 100}\n")
    text.write(f"Greatest Increase in Profits: {GI_month} (${greatest_increase})\n")
    text.write(f"Greatest Decrease in Losses: {GD_month} (${greatest_decrease})\n")