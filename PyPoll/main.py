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


   
    print(f'{candidates[0]}: {candidatePercentage[0]} ({candidateVotes[0]})')
    print(f'{candidates[1]}: {candidatePercentage[1]} ({candidateVotes[1]})')
    print(f'{candidates[2]}: {candidatePercentage[2]} ({candidateVotes[2]})')
    print('-----------------------------------')
    print(f'Winner: {winner}')
    

 # The winner of the election based on popular vote

# final result should also write a text file
output_path = os.path.join("analysis",'ElectionAnalysis.txt')

with open(output_path, 'w') as file:
    file.write('Election Results\n')
    file.write('------------------------------------\n')  
    file.write(f"Total Votes: {totalVotes}\n") 
    file.write('------------------------------------\n') 
    file.write(f'{candidates[0]}: {candidatePercentage[0]} ({candidateVotes[0]})\n') 
    file.write(f'{candidates[1]}: {candidatePercentage[1]} ({candidateVotes[1]})\n') 
    file.write(f'{candidates[2]}: {candidatePercentage[2]} ({candidateVotes[2]})\n') 
    file.write('------------------------------------\n') 
    file.write(f'Winner: {winner}\n') 
    