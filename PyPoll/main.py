import os
import csv

csvpath = os.path.join("..", "Resources", "election_data.csv")

total_votes=0
cand_dict = {}
winner=""
winner_votes=0

with open(csvpath, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")

	next(csvreader, None)

	for row in csvreader:
		voter_id = row[0]
		county = str(row[1])
		candidate = str(row[2])
		total_votes = total_votes + 1
		if candidate in cand_dict:
			cand_dict[candidate] = cand_dict[candidate] + 1
		else:
			cand_dict[candidate] = 1
			

print("Election Results")
print("-------------------------")
print(f'Total Votes: {total_votes}')
for key, value in cand_dict.items():
	if (value > winner_votes):
		winner_votes = value
		winner = key
	percent = '{percent:.3%}'.format(percent=value/total_votes)
	print(f'{key}: {percent} ({value})')
print("-------------------------")
print(f'Winner: {winner}')
print("-------------------------")