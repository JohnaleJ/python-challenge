# Importing the os module to utilize various os
import os
budgetcsvpath = os.path.join('Resources', 'budget_data.csv')

# Importing csv and reading the csv file
import csv
with open(budgetcsvpath, newline= '') as budgetcsvfile:

    #CSV reader with delimiter
    budgetcsvreader = csv.reader(budgetcsvfile, delimiter=',')
      
    # Read the header 
    budgetcsv_header = next(budgetcsvreader)
   # print(f"Budget CSV Header: {budgetcsv_header}")

   
   
    #create variables to hold the date and profit or loss
    date = []
    profit_loss = []
    profit_loss_value = []
    profit_loss_change = []


    # Append date and profit or loss data into their empty lists
    for row in budgetcsvreader:
      
        date.append(row[0])
        profit_loss.append(row[1])

    # Modify the text values in Profit or Loss to numerical value
    profit_loss_value = [int(i) for i in profit_loss]

    # Calculate the profit/loss change between each period and append to list ended up referencing https://www.tutorialspoint.com/calculate-difference-between-adjacent-elements-in-given-list-using-python 
    
    for j in range (1, len(profit_loss_value)):
        profit_loss_change.append(profit_loss_value[j] - profit_loss_value[j-1])

    #Print Summary Statistics to terminal
    print(f"Total Months:  {len(date)}")
    print(f"Total: ${sum(profit_loss_value)}")
    print(f"Average Change:  ${sum(profit_loss_change)/ len(profit_loss_change)}")

    # code to check the index location for min and max to identify field in date list +1
    # for l in range (len(profit_loss_change)):
    #     print(f"Index {l}: {profit_loss_change[l]}")

  
    print(f"Greatest Increase in Profits: {date[25]} (${max(profit_loss_change)})")
    print(f"Greatest Decrease in Profits: {date[44]} (${min(profit_loss_change)})")
    
    # Write file of the results to specified location
    
    budget_output_path = os.path.join ('Analysis', 'PyPoll_Analysis.txt')

    # Open the file using "write" mode and specify variable for contents. 
    with open(budget_output_path, 'w', newline = '') as txtfile:

        # Write the first row (headers)
        txtfile.write('Financial Analysis''\n')

        # Write the second row (headers)
        txtfile.write('--------------------''\n')

        #Write Summary Statistics to File
        txtfile.write(f"Total Months:  {len(date)}"'\n')
        txtfile.write(f"Total: ${sum(profit_loss_value)}"'\n')
        txtfile.write(f"Average Change:  ${sum(profit_loss_change)/ len(profit_loss_change)}"'\n')
        txtfile.write(f"Greatest Increase in Profits: {date[25]} (${max(profit_loss_change)})"'\n')
        txtfile.write(f"Greatest Decrease in Profits: {date[44]} (${min(profit_loss_change)})"'\n')
    