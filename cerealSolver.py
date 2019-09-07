#import modules
import os
import csv

#open the csv
cerealCSV=os.path.join(".","cereal.csv")
    #create my csv reader
with open (cerealCSV,"r", encoding="UTF-8") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csvHeader = next(csvreader)
    print(f"The header is {csvHeader}")
    #iterate rows (for loop)
    for row in csvreader:
        #if statement (if the cereal contains 5 or more grams of fiber, print)
        if float (row[7]) >= 5:
            #print row if conditions meets
            print(row)
