from audioop import avg
import os 
import csv

from numpy import diff 

csvpath = os.path.join('Resources','budget_data.csv')


totalMonths = []
total = []
totalChange = []
avgChange = 0

with open(csvpath) as csvfile:
    csvreader= csv.reader(csvfile,delimiter=',')
    next(csvreader)
    for row in csvreader:
        # print(row)
        total.append(int(row[1]))
        totalMonths.append(row[0])
        
    print("Financial Analysis")
    print("--------------------------------------------")
    #   The total number of months included in the dataset
    print(f"Total Months: {len(totalMonths)}")
    # The net total amount of "Profit/Losses" over the entire period
    print(f"Total: ${sum(total)}")


    for i in range(1,len(total)):
        totalChange.append(total[i] - total[i-1])
        avgChange =sum(totalChange)/len(totalChange)
        maxChange = max(totalChange)
        minChange = min(totalChange)
        maxDate = str(totalMonths[totalChange.index(maxChange)+1])
        minDate = str(totalMonths[totalChange.index(minChange)+1])
    

    # The changes in "Profit/Losses" over the entire period, and then the average of those changes
    print(f"Average Change: ${round(avgChange,2)}")
    # The greatest increase in profits (date and amount) over the entire period
    print(f"Greatest Increase in Profits: {maxDate} (${maxChange})")
    # The greatest decrease in profits (date and amount) over the entire period
    print(f"Greatest Decrease in Profits: {minDate} (${minChange})")


# final result should also write a text file
output_path = os.path.join("Resources",'FinAnalysis.txt')

with open(output_path, 'w') as file:
    file.write('Financial Analysis \n -------------------------------------------- \n')
    file.write('Total Months: ' + str(len(totalMonths)) +'\n')  
    file.write('Total: $' + str(sum(total))+ '\n') 
    file.write('Average Change: $'+ str(round(avgChange,2)) +'\n') 
    file.write('Greatest Increase in Profits: '+ maxDate + ' $'+ str(maxChange) +'\n') 
    file.write('Greatest Decrease in Profits: '+ minDate +' $'+ str(minChange) +'\n') 
   

