# The total number of votes cast
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
current_candidate = 0
candidates_list = []
votes_list = []

csvpath = os.path.join("/Users/jennabarkley/Desktop/BootCamp Stuff/Module 3 Challenge/PyPoll/Resources/election_data.csv")

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Save the head, and read the header row first
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}") if needed

    # Read each row of data after the header
    for row in csvreader:
        
        # Step 2: The total number of votes cast
        total_votes += 1
        
        # Step 3: A complete list of candidates who received votes, keep track
        current_candidate = (row[2])

        # Step 5: The total number of votes each candidate won
        # start a list for candidates, and a list for votes
        if (current_candidate in candidates_list):
            candidate_index = candidates_list.index(current_candidate)
            votes_list[candidate_index] = votes_list[candidate_index] + 1
        else: #track changes and append
            candidates_list.append(current_candidate)
            votes_list.append(1)

    