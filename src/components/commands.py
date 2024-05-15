import dataStorage
import itemClass
from datetime import date
from tkinter import *
import customtkinter as tk
from customtkinter import CTkToplevel

listOfEntries = []

def populateListbox(listFrame):
    for entry in listFrame.winfo_children():
        entry.destroy()
    for entry in listOfEntries:
        itemFrame = tk.CTkFrame(master=listFrame)
        job = tk.CTkLabel(master=itemFrame, text=entry.job, width=50)
        date = tk.CTkLabel(master=itemFrame, text=entry.date, width=50)
        reason = tk.CTkLabel(master=itemFrame, text=entry.description, width=50)
        transaction = tk.CTkLabel(master=itemFrame, text=entry.amount, width=50)
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

def Open_Button(UI, listFrame):  
    global listOfEntries 

    if(len(listOfEntries) > 0):
        Popup = CTkToplevel(UI)
        Popup.grab_set()
        Popup.title("Warning")
        Popup.geometry("500x100")
        tk.CTkLabel(Popup, text="Are you sure you want to open a new file? Current data will be overwritten!").pack()
        tk.CTkButton(Popup, text="Yes", command=lambda: [dataStorage.load(), Popup.destroy()]).pack()
        tk.CTkButton(Popup, text="No", command=Popup.destroy).pack()
    else:
        listOfEntries = dataStorage.load()
    print("Open_Button list created")

    populateListbox(listFrame)