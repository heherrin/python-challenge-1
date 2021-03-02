# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 15:23:47 2021

@author: heath
"""

import csv

#read in csv
with open ('/Users/heath/python-challenge/PyPoll/election_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    
    #create empty lists for candidates & votes
    candidates = []
    votes = []
    
    #append unique candidates to candidates list & count votes received for each candidate
    for row in csvreader:
        if row[2] not in candidates:
            candidates.append(row[2])
            votes.append(1)
        else:
            count = candidates.index(row[2])
            votes[count] += 1
     
    #count total votes for the election
    count_votes = sum(votes)
    
    #write f-string to display total election votes
    total_vote_count = (
        f"Election Results\n"
        f"--------------------\n"
        f"Total Votes: {count_votes}\n"
        f"--------------------\n"
        )
   
    #calculate % of votes received & create list for %s for all 4 candidates
    votes_percentage = [round(votes[x]/count_votes*100,3) for x in range(0,len(votes))]
    

#calculate winner based on max vote receiver
winner = {candidates[votes.index(max(votes))]}   
#wite f-string to display the election winner
election_winner = (
    f"--------------------\n"
    f"Winner: {winner}\n"
    )


#print f-strings for total votes & winner as well as 
print(total_vote_count)
for x in range(0,len(candidates)):
        print(f"Candidate: {candidates[x]} {votes_percentage[x]}% ({votes[x]})")
print(election_winner)

#write results to txt file
with open("PYPollElectionResults.txt", "w") as txt_file:
    txt_file.write(total_vote_count)
    for x in range(0,len(candidates)):
        print(f"Candidate: {candidates[x]} {votes_percentage[x]}% ({votes[x]})", file=txt_file)
    txt_file.write(election_winner)
    

                   
                     




    
    
    
        
    

    
      

        
        
        
    
    