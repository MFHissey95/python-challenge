# Import os module
import os
# Import module for reading CSV
import csv

# Path to collect data from the PyBank folder
csv_path = 'budget_data.csv'

# Define variables
total_months = 0
net_total = 0
previous_amount = 0
total_changes = 0
average_change = 0
greatest_increase = -100000
greatest_decrease = 100000
greatest_increase_date = ""
greatest_decrease_date = ""

# Open and read in the CSV file
with open(csv_path) as csvfile:
    
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip header line
    header = next(csvreader)
    
    # Read & Loop through each row of data after the header 
    for row in csvreader:
        
        # Calculate total months
        total_months = total_months + 1
        # Calculate net total of profits and losses
        net_total = net_total + float(row[1])

            # Taking each change in profit into account
        if  previous_amount != 0:
            previous_amount = float(row[1]) - float(previous_amount)
            total_changes = total_changes + previous_amount

            # Calculating the Greatest Increase
        if  previous_amount >= greatest_increase:
            greatest_increase = previous_amount
            greatest_increase_date = row[0]


            # Calculating the Greatest Decrease
        if  previous_amount <= greatest_decrease:
            greatest_decrease = previous_amount
            greatest_decrease_date = row[0]

    previous_amount = row[1]

# Calculating the average change
average_change = total_changes / (total_months - 1)


# Print the header for "Financial Analysis" & following results
print("''''''''''''''''''''''''''''''''''''")
print("Financial Analysis")
print("___________________________________ ")
print("Total Months: " + str(total_months))
print("Total: $" + str(int(net_total)))
print("Average Change: " +  str(round(average_change, 2)))
print("Greatest Increase in Profits: " + greatest_increase_date + "  ($" + str(int(greatest_increase))+ ")")
print("Greatest Decrease in Profits: " + greatest_decrease_date + "  ($" + str(int(greatest_decrease))+ ")")

# Export text file w/ results
import sys
file = open('Financial_Analysis_Final.txt', 'a')
sys.stdout = file

print("''''''''''''''''''''''''''''''''''''")
print("Financial Analysis")
print("___________________________________ ")
print("Total Months: " + str(total_months))
print("Total: $" + str(int(net_total)))
print("Average Change: " +  str(round(average_change, 2)))
print("Greatest Increase in Profits: " + greatest_increase_date + "  ($" + str(int(greatest_increase))+ ")")
print("Greatest Decrease in Profits: " + greatest_decrease_date + "  ($" + str(int(greatest_decrease))+ ")")

file.close()