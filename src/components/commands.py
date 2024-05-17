#This file gives the functionality of the components from interface.py

import dataStorage
import itemClass
from datetime import date
from tkinter import *
import customtkinter as tk
from customtkinter import CTkToplevel

listOfEntries = []
startIndex = 0 #This specifies the start index of the list - used when scrolling through large lists of entries

def populateListbox(listFrame):
    global startIndex
    start = startIndex
    for entry in listFrame.winfo_children():
        print(entry)
        entry.destroy()
    for entry in range(start, len(listOfEntries), start+1):
        itemFrame = tk.CTkFrame(master=listFrame)
        job = tk.CTkLabel(master=itemFrame, text=listOfEntries[entry].job, width=50)
        date = tk.CTkLabel(master=itemFrame, text=listOfEntries[entry].date, width=50)
        reason = tk.CTkLabel(master=itemFrame, text=listOfEntries[entry].description, width=50)
        transaction = tk.CTkLabel(master=itemFrame, text=listOfEntries[entry].amount, width=50)
        job.pack(side="left", padx=10)
        date.pack(side="left", padx=10)
        reason.pack(side="left", padx=10)
        transaction.pack(side="left", padx=10)
        itemFrame.pack()

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

def Overwrite_Button():
    global listOfEntries
    listOfEntries.clear() #Possible Remove
    listOfEntries = dataStorage.load()

def Open_Button(UI, listFrame):  
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

    populateListbox(listFrame)

def Down_Button(listFrame, button):
    global startIndex
    if(startIndex < len(listOfEntries)):
        button.configure(state=ACTIVE)
        startIndex = startIndex + 1
    #if(startIndex == len(listOfEntries)):
    #    button.configure(state=DISABLED)
    populateListbox(listFrame)

def Up_Button(listFrame, button):
    global startIndex
    if(startIndex > 0):
        button.configure(state=ACTIVE)
        startIndex = startIndex - 1
    #if(startIndex == 0):
    #    button.configure(state=DISABLED)
    populateListbox(listFrame)