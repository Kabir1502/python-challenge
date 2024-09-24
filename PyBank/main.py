import csv
import os
csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip the header row
    data = list(csvreader)
    total_months = len(data)
    total_profit_losses = sum(int(row[1]) for row in data) # Total profit loss
    monthly_changes = []
    previous_value = int(data[0][1])  # The profit/loss for the first month

    #make list of total changes
    for i in range(1, len(data)):
        current_value = int(data[i][1])
        change = current_value - previous_value
        monthly_changes.append(change)
        previous_value = current_value

#Calculate greatest increase and decrease
average_change = sum(monthly_changes) / len(monthly_changes)
greatest_increase = max(monthly_changes)
greatest_decrease = min(monthly_changes)

#store dates
greatest_increase_date = data[monthly_changes.index(greatest_increase) + 1][0]
greatest_decrease_date = data[monthly_changes.index(greatest_decrease) + 1][0]
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Increase in Profits: {greatest_decrease_date} (${greatest_decrease})")

#Export results to a text file
with open("analysis/financial_analysis.txt", "w") as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit_losses}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase:.2f})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease:.2f})\n")
