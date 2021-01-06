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
                decrease_month = row[0]

        last_profit = int(row[1])
         # The total number of months included in the dataset
        months = months + 1
        print(row)
    # The net total amount of "Profit/Losses" over the entire period
        profit_loss = profit_loss + int(row[1])

print("Financial Analysis")
print("----------------------------")
print("Total Months:" + str(months))
print("Total Revenue:" + str(profit_loss))

# The average of the changes in "Profit/Losses" over the entire period
average_change = (last_profit - first_profit)/ (months - 1)
print("Average Change in Revenue: $" + str(average_change))

# The greatest increase in profits (date and amount) over the entire period
print("Greatest Increase in Revenue: " + increase_month + " ($" + str(int(greatest_increase)) + ")")


# The greatest decrease in losses (date and amount) over the entire period
print("Greatest Decrease in Revenue: " + decrease_month + " ($" + str(int(greatest_decrease)) + ")")

# Exporting results to a txt file
output_file = os.path.join("PyBank Results.txt")

with open(output_file, 'w', newline='') as file:
    text = csv.writer(file)
    text.writerow(["Financial Analysis"])
    text.writerow(["----------------------------"])
    text.writerow(["Total Months:" + str(months)])
    text.writerow(["Total Revenue:" + str(profit_loss)])
    text.writerow(["Average Change in Revenue: $" + str(average_change)])
    text.writerow(["Greatest Increase in Revenue: " + increase_month + " ($" + str(int(greatest_increase)) + ")"])
    text.writerow(["Greatest Decrease in Revenue: " + decrease_month + " ($" + str(int(greatest_decrease)) + ")"])
