# The total number of votes cast
    # counter; for loop on csv record and count how many records there are
    # start counter at zero, for loop +1
# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.

# In addition, your final script should both print the analysis to the terminal 
# and export a text file with the results.

# Step 1: read the CSV file
import os
import csv

# Variables
total_votes = 0

csvpath = os.path.join("/Users/jennabarkley/Desktop/BootCamp Stuff/Module 3 Challenge/PyPoll/Resources/election_data.csv")

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Save the head, and read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        
        # Step 2: The total number of votes cast
        total_votes += 1
        print(total_votes)