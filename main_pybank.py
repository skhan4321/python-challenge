import csv 

import os 

csvpath = os.path.join("PyBank","budget_data.csv")
#variables
total_months = 0
total_profit = 0 

# open the file and run code
with open(csvpath,'r') as budget_analysis:
    csvreader = csv.DictReader(budget_analysis)
    for row in csvreader:
        total_months = total_months + 1
        total_profit = total_profit + int(row["Profit/Losses"])
      
