#First we'll import the os module
#This will allow us to create file paths across operating systems
import os

#Module for reading CSV files
import csv

#Name file to read
csvPath = os.path.join("Resources", "election_data.csv")

#CSV reader specifies delimiter and variable that holds contents
with open(csvPath) as cvsFile:
    csvReader = csv.reader(cvsFile, delimiter=',')
    next(csvReader)

    #Define votes
    total_votes = 0

    #Put candidates in dictonary
    candidates = dict()

    #for loop through the file
    for row in csvReader:
         #Count the total number of votes cast
        total_votes += 1
            
        #Find and append unique candidates to dictionary
        if row[2] not in candidates:
            candidates[row[2]] = 1
        else:
            candidates[row[2]] += 1

    #Define the candidate percentage
    def percentage_votes(candidate):

    #Function to calculate percentage of votes each candidate won
        percent_won = (candidate / total_votes) * 100
        #Put return to complete equation
        return percent_won

    #Determine election winner 
    winner = max(candidates, key= candidates.get)

#Finish my Printing
print("Election Results")
print("-------------------------")

#The total number of votes cast
print("Total Votes: " + str(total_votes))
print("-------------------------")

#A complete list of candidates who received votes, their percentages votes won, and number of votes won
for key, value, in candidates.items():
    print(f"{key}: {percentage_votes(value):.3f}% ({value})")
print("-------------------------")

#The winner of the election based on popular vote.
print("Winner: " + str(winner))
print("-------------------------")

# Export results to a new txt file
output_file = os.path.join("PyPoll Results.txt")

with open(output_file, 'w', newline='') as file:
    text = csv.writer(file)
    text.writerow(["Election Resultes"])
    text.writerow(["----------------------------"])
    text.writerow(["Total Votes: " + str(total_votes)])
    text.writerow(["----------------------------"])
    for key, value, in candidates.items():
        text.writerow([(f"{key}: {percentage_votes(value):.3f}% ({value})")])
    text.writerow(["----------------------------"])
    text.writerow(["Winner: " + str(winner)])
    text.writerow(["----------------------------"])