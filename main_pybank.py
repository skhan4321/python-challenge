import csv 

import os 

csvpath = os.path.join("PyBank","budget_data.csv")
#variables
#variables
total_months = 0
total_revenue = 0 
change_revenue = [] 
previous_revenue = 0
revenue_average = 0 
#current_value = float(row["Profit/Losses"])
change_dates=[]



# open the file and run code
with open(csvpath,'r') as budget_analysis:
    csvreader = csv.DictReader(budget_analysis)
    for row in csvreader:
        current_value = float(row["Profit/Losses"])
        total_months = total_months + 1
        total_revenue = total_revenue + current_value
        change_revenue.append(current_value - previous_revenue)
        previous_revenue = current_value
        dates = (row['Date'])
        change_dates.append(dates)
        
#revenue change        
max_decrease=min(change_revenue)
max_increase=max(change_revenue)

max_decrease_index=change_revenue.index(max_decrease)
min_date=change_dates[max_decrease_index]

max_increase_index=change_revenue.index(max_increase)
max_date = change_dates[max_increase_index] 

        
change_revenue.remove(change_revenue[0])


revenue_average = round(sum(change_revenue)/(total_months - 1), 2)

print("Total Months: " + str(total_months))
print("Total: " + "$", int(total_revenue))
print("Average Change: " + "$" + str(revenue_average))

#print("Greatest Decrease in Profits: ",  min_date, max_decrease)
print("Greatest Increase in Profits: ", max_date,"($",int(max_increase),")")
print("Greatest Decrease in Profits: ", min_date,"($",int(max_decrease),")")


#output file
output_file = open("output_file","w")
output_file.write("Total Months: " + str(total_months))
output_file.close()
