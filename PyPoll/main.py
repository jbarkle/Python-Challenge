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
percent_vote = []

csvpath = os.path.join("Resources/election_data.csv")

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

    # Step 4: The percentage of votes each candidate won
    # variables for popular votes
    pop_vote = votes_list[0]
    pop_vote_index = 0
    # use len on candidate list then count total votes
    for count in range(len(candidates_list)):
        # convert to percent
        percentage = votes_list[count]/total_votes*100
        #keep a list of percentages
        percent_vote.append(percentage)
        # define winner vote count
        if votes_list[count] > pop_vote:
            pop_vote_index = count
    election_winner = candidates_list[pop_vote_index]
    # round to thousandths
    percent_vote = [round (i,3) for i in percent_vote]
    
# Step 7: Print an analysis to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for count in range(len(candidates_list)):
    print(f"{candidates_list[count]}: {percent_vote[count]}% ({votes_list[count]})")
print("-------------------------")
print(f"Winner: {election_winner}")
print("-------------------------")

# Step 8: Save as a txt file
# specify the file to write to
output_file = os.path.join("/Users/jennabarkley/Desktop/Challenges/Python-Challenge/PyPoll/Analysis/election_analysis.txt")

# # open file using write mode, specify variable to hold contents
with open(output_file, 'w') as text:
# write contents, don't forget to end each line with \n
    text.write("Election Results\n")
    text.write("-------------------------\n")
    text.write(f"Total Votes: {total_votes}\n")
    text.write("-------------------------\n")
    for count in range(len(candidates_list)):
        text.write(f"{candidates_list[count]}: {percent_vote[count]}% ({votes_list[count]})\n")
    text.write("-------------------------\n")
    text.write(f"Winner: {election_winner}\n")
    text.write("-------------------------\n")