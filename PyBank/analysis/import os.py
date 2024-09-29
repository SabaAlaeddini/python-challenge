import os
import csv

budget_data = os.path.join("..", "Resources", "budget_data.csv")

total_months = 0
net_total = 0
previous_profit = 0
changes = []
greatest_increase = ["", 0]  # [date, amount]
greatest_decrease = ["", 0]  # [date, amount]

# Read the CSV file
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip the header

    for row in csvreader:
        total_months += 1
        date = row[0]
        profit_loss = int(row[1])
        net_total += profit_loss

        # Calculate changes
        if total_months > 1:
            change = profit_loss - previous_profit
            changes.append(change)

            # Check for greatest increase
            if change > greatest_increase[1]:
                greatest_increase[0] = date
                greatest_increase[1] = change

            # Check for greatest decrease
            if change < greatest_decrease[1]:
                greatest_decrease[0] = date
                greatest_decrease[1] = change

        previous_profit = profit_loss

# Calculate average change
average_change = sum(changes) / len(changes)

# Print the analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Export the results to a text file
with open('financial_analysis.txt', 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")