# Module for reading CSV files
import os
import csv
#Open the CSV file and skip the header
csvpath = os.path.join('PyBank','Resources', 'budget_data.csv')
txtpath = os.path.join('PyBank','Resources','financial_analysis.txt')
with open (csvpath, newline="") as csv_file:
    csv_reader= csv.reader(csv_file, delimiter=",")
    header = next(csv_reader)

    # create the variables
    row = next(csv_reader)
    month_counter = 1
    total_profit = 0
    total_profit_change = 0

    # those variables need to be read as int instead of a string
    min_profit = int(row[1])
    max_profit = int(row[1])
    previous_profit = int(row[1])
    total_profit = int(row[1])

    # read one row at a time
    for row in csv_reader:
        #increase counter for number in months
        month_counter = month_counter + 1
        profit = int(row[1])

        #add to sum
        total_profit = total_profit + profit
        #find change in profit between this month and last month
        profit_change = profit - previous_profit
        #add change in profit to net change in profit for data set
        total_profit_change = total_profit_change + profit_change

        #determine if change in profit is a max or min for data set thus far
        if profit_change > max_profit:
            max_month = row[0]
            max_profit = profit_change

        if profit_change < min_profit:
            min_month = row[0]
            min_profit = profit_change

        #set previous profit to profit
        previous_profit = profit

    #finish calculations
    average_profit = total_profit/month_counter
    average_profit_change = total_profit_change/(month_counter-1)
    
    #print analysis to terminal
    print("-------------------------------------------------------")
    print(f"Financial Analysis")
    print("-------------------------------------------------------")
    print(f"Total Months: {month_counter}")
    print(f"Total: ${total_profit}")
    print(f"Average Change: ${round(average_profit_change,2)}")
    print(f"Greatest Increase in Profits: {max_month} (${max_profit})")
    print(f"Greatest Decrease in Profits: {min_month} (${min_profit})")
    print("-------------------------------------------------------")
    
    #print to text file
    with open("financial_analysis.txt", "w") as text_file:
        text_file.write("-------------------------------------------------------\n")
        text_file.write(f"Financial Analysis\n")
        text_file.write("-------------------------------------------------------\n")
        text_file.write(f"Total Months: {month_counter}\n")
        text_file.write(f"Total: ${total_profit}\n")
        text_file.write(f"Average Change: ${round(average_profit_change,2)}\n")
        text_file.write(f"Greatest Increase in Profits: {max_month} (${max_profit})\n")
        text_file.write(f"Greatest Decrease in Profits: {min_month} (${min_profit})\n")
        text_file.write("-------------------------------------------------------\n")