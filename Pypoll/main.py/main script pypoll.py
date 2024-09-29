# Required Libraries
import csv
import os

# Paths for input and output files
input_path = os.path.join("..", "Resources", "election_data.csv")  # Path for the input CSV file
output_path = os.path.join("..", "analysis", "election_analysis.txt")  # Path for the output text file

# Initialize variables for tracking election results
vote_total = 0  # Total number of votes cast
# Lists and dictionaries to keep track of candidates and their votes
candidate_names = []
votes_per_candidate = {}
# Track the candidate with the highest votes
top_candidate = ""
highest_vote_count = 0

# Read the CSV file and analyze the data
with open(input_path) as election_file:
    csv_reader = csv.reader(election_file)
    # Skip the initial header row
    next(csv_reader)
    # Process each row of election data
    for record in csv_reader:
        print(". ", end="")  # Loading indicator for large datasets
        vote_total += 1  # Increment the overall vote total
        name = record[2]  # Candidate's name from the row
        
        # If the candidate is new, add them to the list and dictionary
        if name not in candidate_names:
            candidate_names.append(name)
            votes_per_candidate[name] = 0
        
        # Increment the candidate's vote count
        votes_per_candidate[name] += 1

# Write the results to a text file
with open(output_path, "w") as result_file:
    print(f"\nTotal votes recorded: {vote_total}")  # Print total votes to terminal
    summary = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {vote_total}\n"
        f"-------------------------\n"
    )
    result_file.write(summary)
    
    # Calculate percentages and determine the winner
    for candidate in candidate_names:
        current_vote_count = votes_per_candidate[candidate]
        vote_percentage = (current_vote_count / vote_total) * 100
        rounded_percentage = round(vote_percentage, 3)
        
        # Update the winner if this candidate has the highest votes
        if current_vote_count > highest_vote_count:
            highest_vote_count = current_vote_count
            top_candidate = candidate
        
        # Format and print each candidate's details
        candidate_info = f"{candidate}: {current_vote_count} votes and {rounded_percentage}% share"
        print(candidate_info)
        candidate_summary = (
            f"{candidate}: {rounded_percentage}% ({current_vote_count})\n"
        )
        result_file.write(candidate_summary)
    
    # Prepare and print the winning candidate's summary
    winning_percentage = round((highest_vote_count / vote_total) * 100, 3)
    winner_summary = (
        f"-------------------------\n"
        f"Winning Candidate: {top_candidate}\n"
        f"Votes: {highest_vote_count}\n"
        f"Vote Percentage: {winning_percentage}%\n"
        f"-------------------------\n"
    )
    print(winner_summary)

    # Save the winning candidate summary to the output file
    winner_summary_file = (
        f"-------------------------\n"
        f"Winner: {top_candidate}\n"
        f"-------------------------\n"
    )
    result_file.write(winner_summary_file)