#import libraries
import os
import csv

#define variables
candidate_chosen = []
vote_candidate = {}
total_votes = 0

#establish csv path
rel_path = '../Resources/election_data.csv'

#open and read csv
with open (rel_path) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    headers = next(csv_reader)

#total votes for each candidate
    for row in csv_reader:
        total_votes += 1
        candidate_picked = row[2]
        if candidate_picked not in candidate_chosen:
            candidate_chosen.append(candidate_picked)
            vote_candidate[candidate_picked] = 0
        vote_candidate[candidate_picked] += 1


#Determine percentage of votes for each candidate
DD_Votes = float(vote_candidate['Diana DeGette'])
per_votes_DD = (float(DD_Votes)/float(total_votes)) * 100
CS_Votes = float(vote_candidate['Charles Casper Stockham'])
per_votes_CS = (float(CS_Votes)/float(total_votes)) * 100
RD_Votes = float(vote_candidate['Raymon Anthony Doane'])
per_votes_RD = (float(RD_Votes)/float(total_votes)) * 100


#print statements
print("")
print('---text')
print('Election Results')
print('---------------------------')
print(f'Total Votes: {total_votes}')
print('---------------------------')
print('Charles Casper Stockham:', str("{:.3f}%".format(per_votes_CS)), "(" + str(int(CS_Votes)),")")
print('Diana DeGette:', str("{:.3f}%".format(per_votes_DD)), "(" + str(int(DD_Votes)),")")
print('Raymon Anthony Doane:', str("{:.3f}%".format(per_votes_RD)), "(" + str(int(RD_Votes)),")")
print('---------------------------')
print('Winner:  Diana DeGette')
print('---------------------------')
print('---')







