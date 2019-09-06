# Import os module
import os
# Import module for reading CSV
import csv
# Import sorting module
import operator

# Path to collect data from the PyPoll folder
csv_path = 'election_data.csv'

# Create dictionary assigning the count of Votes(Value) for each Candidate(Key)
electiondict = {}

# Define variable for Total Votes Cast
total_votes_cast = 0


# Open and read in the CSV file
with open(csv_path) as csvfile:
    
    # Splt the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header line
    header = next(csvreader)

    # Read & Loop through each row of data after the header 
    for row in csvreader:

        # Calculate total votes cast
        total_votes_cast = total_votes_cast + 1

        # Calculate total no. votes each candidate won
        if row[2] in electiondict.keys():

            electiondict[row[2]] +=1
        
        # If candidate isn't present in dictionary
        else:
            electiondict[row[2]] = 1
    
final_sorted = sorted(electiondict.items(), key=operator.itemgetter(1), reverse=True)

# Print the Election Results
print("''''''''''''''''''''''''")
print("Election Results")
print("_____________________________")
# Print Total Votes 
print("Total Votes: ",total_votes_cast)
print("_____________________________")
# Print Candidate Name, Percentage, Amount of Votes
for k, v in final_sorted:
    val=str(v)
    percent=round(float(val)/float(total_votes_cast))*100
    print(k + ": "+ str(percent) + '%' + '('+ str (v) + ')')
print("_____________________________")
#print(maximum = max(electiondict, key=electiondict.get))
print("_____________________________")

# Export text file w/ Election results
import sys
file = open('Election_Results_Final.txt', 'a')
sys.stdout = file

# Print the Election Results
print("''''''''''''''''''''''''")
print("Election Results")
print("_____________________________")
# Print Total Votes 
print("Total Votes: ",total_votes_cast)
print("_____________________________")
# Print Candidate Name, Percentage, Amount of Votes
for k, v in final_sorted:
    val=str(v)
    percent=(float(val)/float(total_votes_cast))*100
    print(k + ": "+ str(percent) + '%' + '('+ str (v) + ')')
print("_____________________________")
#print(maximum = max(electiondict, key=electiondict.get))
print("_____________________________")

file.close()