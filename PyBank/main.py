import os
import csv

Py_Bank = os.path.join("Resources","budget_data.csv")


# Open and read csv
with open(Py_Bank) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")
    
    #count number of months
    total_months=0
    total_profit=0
    greatest_increase = 0
    greatest_decrease = 0
    change = []
    previous_month = 0
    for row in csvreader:
        total_months= total_months + 1
   
        total_profit = total_profit + int(row[1])

        change.append(int(row[1]) - previous_month)
        if (int(row[1])-previous_month) > greatest_increase:
            greatest_increase = (int(row[1])-previous_month)

            greatest_increase_month = row[0]
        
        if (int(row[1]) - previous_month) < greatest_decrease:
            greatest_decrease = (int(row[1])-previous_month)
            greatest_decrease_month = row[0]

        previous_month = int(row[1])

    change.pop(0)

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: {total_profit}")
        

    Average_Change = sum(change) / len(change)
    print(f"Average Change: {Average_Change}")

#find and print greatest increase and decrease
 
      

    print(f"Greatest Increase in Profits: {greatest_increase_month} {greatest_increase}")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} {greatest_decrease}")

with open("Analysis/analysis.txt","w") as Analysis:

    Analysis.write(
        "Financial Analysis\n"
        "---------------------------- \n"
        f"Total Months: {total_months}\n"
        f"Total: {total_profit}\n"
        f"Average Change: {Average_Change}\n"
        f"Greatest Increase in Profits: {greatest_increase_month} {greatest_increase}\n"
        f"Greatest Decrease in Profits: {greatest_decrease_month} {greatest_decrease}\n"
    )