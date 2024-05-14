import dataStorage
import itemClass
from datetime import date
from tkinter import *

listOfEntries = []

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
    if((transactionBox == "") or (dateBox == "") or (reasonBox == "") or (jobBox == "")):
        print("Missing input: " + transactionBox + " - " + dateBox + " - " + reasonBox + " - " + jobBox)
        transactionBox = 0.0
        dateBox = str(date.today())
        reasonBox = "-"
        jobBox = "-"
    try:
        newEntry = itemClass.Entry(jobBox, dateBox, reasonBox, float(transactionBox))
        print("Pass")
        listOfEntries.append(newEntry)
        print(listOfEntries)
    except ValueError:
        print("Invalid input: " + transactionBox + " - " + dateBox + " - " + reasonBox + " - " + jobBox)
        newEntry = None
        return

def Open_Button():
    global listOfEntries 
    listOfEntries = dataStorage.load()
    print("Open_Button list created")