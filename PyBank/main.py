# Step 1: read the CSV file
import os
import csv
csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    # Save the header, and read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

# Read each row of data after the header
    for row in csvreader:
        print(row)