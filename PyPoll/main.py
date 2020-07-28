import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
  
    csv_header = next(csvfile)
    

#The total number of votes cast
    total_votes=0
    candidate_votes = {}
    max_votes = 0
    votes = candidate_votes.values()

    for row in csvreader:
        total_votes = total_votes + 1
        candidate_name = row[2]
        
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
        else:
            candidate_votes[candidate_name] = 1

    print("Election Results")
    print("----------------------------")
    print(f"Total votes cast: {total_votes}")
    print("----------------------------")
    for name, vote_count in candidate_votes.items():
        percent_vote = (vote_count/total_votes)
        percent_vote = "{:.2%}".format(percent_vote)
        print(f"{name}: {percent_vote} ({vote_count})")
    print("----------------------------")

with open("Analysis/analysis.txt","w") as Analysis:

    
    Analysis.write("Election Results\n")
    Analysis.write("----------------------------\n")
    Analysis.write(f"Total votes cast: {total_votes}\n")
    Analysis.write("----------------------------\n")
    for name, vote_count in candidate_votes.items():
        percent_vote = (vote_count/total_votes)
        percent_vote = "{:.2%}".format(percent_vote)
        Analysis.write(f"{name}: {percent_vote} ({vote_count})\n")
    Analysis.write("----------------------------\n")
    



