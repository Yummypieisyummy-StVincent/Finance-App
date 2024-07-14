#This file gives the functionality of the components from interface.py

import dataStorage
import itemClass
from datetime import date
from tkinter import *
import customtkinter as tk
from customtkinter import CTkToplevel

listOfEntries = []
startIndex = 0 # This specifies the start index of the list - used when scrolling through large lists of entries
endIndex = 16
# StatsFrameArray = [TotalMoney, TotalExpenses, TotalIncome, Ratio]
totalMoney = 0 # [0]
totalExpenses = 0 # [1]
totalIncome = 0 # [2]
ratio = 0 # [3]

def sortByJob(listsArray, statsFrameArray):
    global listOfEntries
    listOfEntries = sorted(listOfEntries, key=lambda x: x.job)
    populateListbox(listsArray, statsFrameArray)

def sortByDate(listsArray, statsFrameArray):
    global listOfEntries
    listOfEntries = sorted(listOfEntries, key=lambda x: x.date)
    populateListbox(listsArray, statsFrameArray)

def sortByAmount(listsArray, statsFrameArray):
    global listOfEntries
    listOfEntries = sorted(listOfEntries, key=lambda x: x.amount)
    populateListbox(listsArray, statsFrameArray)

def calculate(statsFrameArray):
    global totalMoney, totalExpenses, totalIncome
    totalMoney = totalIncome = totalExpenses = ratio = 0.0
    for entry in listOfEntries:
        totalMoney += round(entry.amount, 2)
        if(entry.amount < 0):
            totalExpenses += round(entry.amount, 2)
        if(entry.amount > 0):
            totalIncome += round(entry.amount, 2)
    statsFrameArray[0].configure(text="Total profit: $" + str("%.2f" %totalMoney))
    statsFrameArray[1].configure(text="Total expenses: $" + str("%.2f" %totalExpenses))
    statsFrameArray[2].configure(text="Total income: $" + str("%.2f" %totalIncome))

    expenses = abs(round(totalExpenses, 2))
    percentage = (expenses/totalMoney)*100.0
    ratio = round(percentage, 2)
    statsFrameArray[3].configure(text="Expense Percentage: " + str(ratio) + "%")
    #return totalMoney

def populateListbox(listsArray, statsFrameArray):
    global startIndex, endIndex
    start = startIndex
    end = endIndex
    for list in listsArray:
        for entry in list.winfo_children():
            entry.destroy()
    for entry in range(start, end):
        job = tk.CTkLabel(master=listsArray[0], text=listOfEntries[entry].job)
        date = tk.CTkLabel(master=listsArray[1], text=listOfEntries[entry].date)
        reason = tk.CTkLabel(master=listsArray[2], text=listOfEntries[entry].description)
        transaction = tk.CTkLabel(master=listsArray[3], text=str("%.2f" %listOfEntries[entry].amount))
        removeButton = tk.CTkButton(master=listsArray[4], text="X", fg_color="red", command=lambda entry=entry: [listOfEntries.pop(entry), populateListbox(listsArray, statsFrameArray), calculate(statsFrameArray)])
        job.pack(padx=10)
        date.pack(padx=10)
        reason.pack(padx=10)
        transaction.pack(padx=10)
        removeButton.pack()
    calculate(statsFrameArray)

def Save_Button():
    dataStorage.save(listOfEntries)

def Clear_Text(JobBox, ReasonBox, DateBox, TransactionBox):
    JobBox.delete(0, 'end')
    ReasonBox.delete(0, 'end')
    DateBox.date = date.today()
    TransactionBox.delete(0, 'end')
    JobBox.placeholder_text = "Job"
    ReasonBox.placeholder_text = "Reason of transaction"
    TransactionBox.placeholder_text = "Amount"

def Add_Button(transactionBox, dateBox, reasonBox, jobBox):

    if(transactionBox == ""):
        print("Missing input: transactionBox: " + transactionBox)
        transactionBox = 0.0
    if(dateBox == ""):
        print("Missing input: dateBox: " + dateBox)
        dateBox = str(date.today())
    if(reasonBox == ""):
        print("Missing input: reasonBox: " + reasonBox)
        reasonBox = "-"
    if(jobBox == ""):
        print("Missing input: jobBox: " + jobBox)
        jobBox = "-"
        
    try:
        newEntry = itemClass.Entry(jobBox, dateBox, reasonBox, float(transactionBox))
        listOfEntries.append(newEntry)
        print(listOfEntries)
    except ValueError:
        print("Invalid input")
        newEntry = None
        return

def Set_Start():
    global startIndex
    startIndex = 0

def Set_End():
    global endIndex
    endIndex = 16

def Overwrite_Button():
    global listOfEntries
    listOfEntries.clear() # Possible Remove
    listOfEntries = dataStorage.load()

def Open_Button(UI, listsArray, statsFrameArray):  
    global listOfEntries, startIndex

    if(len(listOfEntries) > 0):
        Popup = CTkToplevel(UI)
        Popup.grab_set()
        Popup.title("Warning")
        Popup.geometry("500x100")
        tk.CTkLabel(Popup, text="Are you sure you want to open a new file? Current data will be overwritten!").pack()
        tk.CTkButton(Popup, text="Yes", command=lambda: [Overwrite_Button(), Popup.destroy(), Set_Start()]).pack()
        tk.CTkButton(Popup, text="No", command=Popup.destroy).pack()
    else:
        listOfEntries = dataStorage.load()

    populateListbox(listsArray, statsFrameArray)
#def disableCheckDown(button):
#    if(startIndex == len(listOfEntries)):
#        button.configure(state=DISABLED)
#    else:
#        button.configure(state=NORMAL)
#
#def disableCheckUp(button):
#    if(startIndex == 0):
#        button.configure(state=DISABLED)
#    else:
#        button.configure(state=NORMAL)

def Down_Button(listFrame, statsFrameArray):
    global startIndex, endIndex
    start = startIndex
    end = endIndex
    if((startIndex < len(listOfEntries) - 16)):
        startIndex += 1
    if(endIndex < len(listOfEntries)):
        endIndex += 1
    if((startIndex != start) and (endIndex != end)):
    #    print("Test 1.Down")
        populateListbox(listFrame, statsFrameArray)
    #if((startIndex == start) and (endIndex == end)):
    #    print("Test 2.Down")

def Up_Button(listFrame, statsFrameArray):
    global startIndex, endIndex
    start = startIndex
    end = endIndex
    if(startIndex > 0):
        startIndex -= 1
    if(endIndex > 16):
        endIndex -= 1
    if((startIndex != start) and (endIndex != end)):
    #    print("Test 1.Up")
        populateListbox(listFrame, statsFrameArray)
    #if((startIndex == start) and (endIndex == end)):
    #    print("Test 2.Up")