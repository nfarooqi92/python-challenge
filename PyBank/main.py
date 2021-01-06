import os
import csv

months = 0
profit_loss = 0
csvpath = os.path.join( 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header

    for row in csvreader:
        if months == 0:
            first_profit = int(row[1])
            greatest_increase = 0
            greatest_decrease = 0
        

        if months != 0:
            change_profit = int(row[1]) - last_profit
            if change_profit > greatest_increase:
                greatest_increase = change_profit
                increase_month = row[0]
            elif change_profit < greatest_decrease:
                greatest_decrease = change_profit
                decerease_month = row[0]

        last_profit = int(row[1])
         # The total number of months included in the dataset
        months = months + 1
        print(row)
    # The net total amount of "Profit/Losses" over the entire period
        profit_loss = profit_loss + int(row[1])

print(months) 
print(profit_loss)

# The average of the changes in "Profit/Losses" over the entire period
average_change = (last_profit - first_profit)/ (months - 1)
print(average_change)

# The greatest increase in profits (date and amount) over the entire period
print(greatest_increase)

# The greatest decrease in losses (date and amount) over the entire period
print(greatest_decrease)