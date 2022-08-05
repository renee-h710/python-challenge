import os
import csv
from turtle import position


file = os.path.join('Resources','election_data.csv')

with open(file) as election_data:
    reader = csv.reader(election_data,delimiter=',')
    header = next(reader,None)
    print('Election Results')
    print('------------------------------------')
 
    totalVotes = 0
    winningVotes = 0
    winner = ""
    candidates =[]
    candidate_index= 0
    candidateVotes= []
    candidatePercentage= []
    

    #first pass, get list of candidates and total votes
    for row in reader:
        totalVotes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
            candidateVotes.append(1)
            candidatePercentage.append(1)
        else:
            candidate_index = candidates.index(row[2])# # The total number of votes each candidate won
            candidateVotes[candidate_index]+=1 
            if candidateVotes[candidate_index] > winningVotes:
                winningVotes= candidateVotes[candidate_index]
                winner = candidates[candidate_index]
        
       # The total number of votes cast
    print(f"Total Votes: {totalVotes}")
    print('------------------------------------')
    # A complete list of candidates who received votes
       
  

    for person in candidates:
        candidate_index = candidates.index(person)
        percent = "{:.00%}".format((candidateVotes[candidate_index]/totalVotes))
        candidatePercentage[candidate_index] = percent# # The percentage of votes each candidate won


    def printCandidates(int):
        print(f'{candidates[int]}: {candidatePercentage[int]} ({candidateVotes[int]})')
    

    printCandidates(0)
    printCandidates(1)
    printCandidates(2)
    print('-----------------------------------')
    print(f'Winner: {winner}')
    

 # The winner of the election based on popular vote