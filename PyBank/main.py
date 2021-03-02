# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 11:08:36 2021

@author: heath
"""
# import csv & os

import csv

#read csv
with open ('/Users/heath/python-challenge/PyBank/budget_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    
    
    #create empty lists to append data into
    profitloss = []
    date = []
    change = []

    #append data to lists for profit/loss & date
    for row in csvreader:

        profitloss.append(float(row[1]))
        date.append(row[0])
        
    for i in range(0,len(profitloss)):
        #append change to a list by subtracting current profit with prior profit
        change.append(profitloss[i] - profitloss[i-1])
        
        #calculate average monthly change
        avg_pl_change = sum(profitloss)/len(date)-1
        
        #calculate max montly change using max function
        max_change = max(change)
        
        #calculate min montly change using min function
        min_change = min(change)
        
        #calculate
        max_change_month = str(date[change.index(max(change))])
        min_change_month = str(date[change.index(min(change))])

#create variable for total dates
total_months = len(date)
#create variable for sum of profits/losses
sum_profit_loss = sum(profitloss)
 
#create f-string for results and for txt file       
results = (
	f"Financial Analysis\n"
	f"-------------------------\n"
	f"Total Months: {total_months}\n"
	f"Total: ${sum_profit_loss}\n"
	f"Average Change: ${avg_pl_change}\n"
	f"Greatest Increase in Profits: {max_change_month} (${max_change})\n"
	f"Greatest Decrease in Profits: {min_change_month} (${min_change})\n")

#print results
print(results)

#write results to txt file
with open("PYBankFinancials.txt", "w") as txt_file:
	txt_file.write(results)
	
   
        
    
    

    
            
           
           
           
        
        
        
        
        
        
        
        
        
        
        
   
    
    
    
        
   
    
        
        
        
        

        
           

    


   