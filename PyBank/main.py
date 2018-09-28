import os
import csv

csvpath = os.path.join("..", "Resources", "budget_data.csv")

total_months = 0
total_profit = 0
previous_profit = 0
total_change = 0
greatest_increase = 0
increase_month = ""
greatest_decrease = 0
decrease_month = ""
profit = 0

with open(csvpath, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")

	next(csvreader, None)

	for row in csvreader:
		month = str(row[0])
		profit = int(row[1])
		total_months = total_months + 1
		total_profit = total_profit + profit
		if (previous_profit != 0):
			total_change = total_change + (profit - previous_profit)
			if (profit-previous_profit > greatest_increase):
				greatest_increase = profit-previous_profit
				greatest_month = month
			if (profit-previous_profit < greatest_decrease):
				greatest_decrease = profit-previous_profit
				decrease_month = month	
		previous_profit = profit
	average_change = round(total_change/(total_months-1),2)

print("Financial Analysis")
print("-------------")
print(f'Total Months: {total_months}')
print(f'Total: ${total_profit}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {greatest_month} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})')
		