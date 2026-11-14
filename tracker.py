#command line expense tracker
#use this to record the money you spend, with it saving the
#records in a saved retrievable file

import csv

MY_FILE = "expenses-tracker.csv"

def adding_expenses(amount, category, date):

    with open(MY_FILE,"a",newline="") as p:
        csv.writer(p).writerow([amount,category,date])
        print("it saved!")

while True:
    print("A = ADD EXPENSE Q = QUIT")
    pick = input("pick: ").upper()

    if pick == "A":
        amount = float(input("Enter amount: "))
        category= input("Enter the category: ")
        date= input("Enter in the date: ")

        #calling
        adding_expenses(amount, category, date)
    elif pick == "Q":
        break

#will be adding onto this project progress nov 13th 9:03pm