import pandas as pd


file_path = "Resources/election_data.csv"  # Path to CSV file
data = pd.read_csv(file_path)

#Calculate total number of votes cast
total_votes = data["Ballot ID"].nunique()

print(f"Total Votes: {total_votes}")
#Get a complete list of candidates who received votes
candidates = data["Candidate"].unique()

print("Candidates who received votes:", candidates)
#Calculate the vote count and percentage for each candidate
vote_counts = data["Candidate"].value_counts()
vote_percentages = (vote_counts / total_votes) * 100

for candidate in vote_counts.index:
    print(f"{candidate}: {vote_percentages[candidate]:.3f}% ({vote_counts[candidate]})")
#Determine the winner based on popular vote
winner = vote_counts.idxmax()

print(f"Winner: {winner}")

# Export results to a text file
with open("analysis/election_results.txt", "w") as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate in vote_counts.index:
        file.write(f"{candidate}: {vote_percentages[candidate]:.3f}% ({vote_counts[candidate]})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")
