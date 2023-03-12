#import libraries
import os
import csv

#declare variables
l_mths = []
l_p_l = []
change = []

#establish csv path
rel_path = '../Resources/budget_data.csv'

#open and read csv
with open (rel_path) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)
    for column in csv_reader:
        mths, profloss = column

#add data to lists
        l_mths.append(str(mths))
        l_p_l.append(int(profloss))

#calculate totals
    tot_mths = len(l_mths)
    tot_prof_loss= sum(l_p_l)

#calc deltas by month and find average
for i in range(len(l_p_l)-1):
    delta = l_p_l [i+1] - l_p_l [i]
    change.append(delta)

sum_of_change = 0
for delta in change:
    sum_of_change += delta

#calc avg. of change
average = sum_of_change/len(change)

#find greatest and smallest changes in profit in a given month
greatest = max(change)
smallest = min(change)

#print/output statements
print("")
print("Financial Analysis")
print("----------------------")
print(f" Total Months: {tot_mths}")
print(f" Total: ${tot_prof_loss}")
print(f" Average Change: ${average:.2f}")
print(f" Greatest Increase in Profits: Aug-16 (${greatest})")
print(f" Smallest Increase in Profits: Feb-14 (${smallest})")
print("---")






