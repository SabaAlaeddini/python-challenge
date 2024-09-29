# Required Libraries
import csv
import os

# Paths for input and output files
input_file_path = os.path.join(".", "Resources", "budget_data.csv")  # Input CSV file path
output_file_path = os.path.join("..", "analysis", "budget_analysis.txt")  # Output text file path

# Initialize variables to accumulate financial data
total_months = 0
total_income = 0

# Initialize additional variables for tracking financial analysis
monthly_changes = []
greatest_increase = ["", 0]  # [date, amount]
greatest_decrease = ["", 0]  # [date, amount]

# Read and process the CSV financial data
with open(input_file_path) as financial_file:
    csv_reader = csv.reader(financial_file)
    # Skip the header row
    next(csv_reader)
    
    # Capture the first row of data
    first_row = next(csv_reader)
    total_months += 1
    total_income += int(first_row[1])
    previous_month_income = int(first_row[1])
    
    # Analyze the data row by row
    for row in csv_reader:
        total_months += 1
        total_income += int(row[1])
        
        # Calculate monthly change
        monthly_change = int(row[1]) - previous_month_income
        previous_month_income = int(row[1])
        monthly_changes.append(monthly_change)
        
        # Identify the highest profit increase
        if monthly_change > greatest_increase[1]:
            greatest_increase[0] = str(row[0])
            greatest_increase[1] = monthly_change
        
        # Identify the highest loss decrease
        if monthly_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = monthly_change

# Calculate average monthly change
average_monthly_change = sum(monthly_changes) / len(monthly_changes)

# Prepare output summary
rounded_avg_change = round(average_monthly_change, 2)
increase_month = greatest_increase[0].split("-")
decrease_month = greatest_decrease[0].split("-")

report = (
    f"\nFinancial Summary\n"
    f"--------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Income: ${total_income}\n"
    f"Average Monthly Change: ${rounded_avg_change}\n"
    f"Greatest Increase in Profits: {increase_month[1]}-{increase_month[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {decrease_month[1]}-{decrease_month[0]} (${greatest_decrease[1]})\n"
)

# Display the report
print(report)

# Save the report to a text file
with open(output_file_path, "w") as output_file:
    output_file.write(report)