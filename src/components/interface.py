#This file creates the components of the window and calls their functionality from commands.py

import customtkinter as tk
import commands
from tkcalendar import DateEntry

tk.set_appearance_mode("SystemDefault")
tk.set_default_color_theme("blue")

listsArray = []

def EntryBox(masterFrame, listsArray):
    entryFrame = tk.CTkFrame(master=masterFrame)

    JobBox = tk.CTkEntry(master=entryFrame, placeholder_text="Job")
    JobBox.pack(anchor="center")

    ReasonBox = tk.CTkEntry(master=entryFrame, placeholder_text="Reason of transaction")
    ReasonBox.pack(anchor="center")

    TransactionBox = tk.CTkEntry(master=entryFrame, placeholder_text="Amount")
    TransactionBox.pack(anchor="center")

    DateBox = DateEntry(master=entryFrame)
    DateBox.pack(anchor="center")

    AddButton = tk.CTkButton(master=entryFrame, text="Add", command=lambda: [commands.Add_Button(TransactionBox.get(), str(DateBox.get_date()), ReasonBox.get(), JobBox.get()), commands.Clear_Text(JobBox, ReasonBox, DateBox, TransactionBox), commands.populateListbox(listsArray)])
    AddButton.pack(anchor="center")

    entryFrame.pack(side="right", padx=10, pady=10)


def Columns(parentFrame):

    global listsArray

    JobColumn = tk.CTkFrame(master=parentFrame, width=20)
    JobColumn.pack(side="left", fill="y")
    DateColumn = tk.CTkFrame(master=parentFrame, width=20)
    DateColumn.pack(side="left", fill="y")
    ReasonColumn = tk.CTkFrame(master=parentFrame, width=20)
    ReasonColumn.pack(side="left", fill="y")
    TransactionColumn = tk.CTkFrame(master=parentFrame, width=20)
    TransactionColumn.pack(side="left", fill="y")

    JobLabelFrame = tk.CTkFrame(master=JobColumn)
    JobLabelFrame.pack()
    DateLabelFrame = tk.CTkFrame(master=DateColumn)
    DateLabelFrame.pack()
    ReasonLabelFrame = tk.CTkFrame(master=ReasonColumn)
    ReasonLabelFrame.pack()
    TransactionLabelFrame = tk.CTkFrame(master=TransactionColumn)
    TransactionLabelFrame.pack()

    JobLabel = tk.CTkLabel(master=JobLabelFrame, text="Job")
    JobLabel.pack()
    DateLabel = tk.CTkLabel(master=DateLabelFrame, text="Date")
    DateLabel.pack()
    ReasonLabel = tk.CTkLabel(master=ReasonLabelFrame, text="Reason")
    ReasonLabel.pack()
    TransactionLabel = tk.CTkLabel(master=TransactionLabelFrame, text="Transaction")
    TransactionLabel.pack()

    JobListFrame = tk.CTkFrame(master=JobColumn)
    JobListFrame.pack()
    DateListFrame = tk.CTkFrame(master=DateColumn)
    DateListFrame.pack()
    ReasonListFrame = tk.CTkFrame(master=ReasonColumn)
    ReasonListFrame.pack()
    TransactionListFrame = tk.CTkFrame(master=TransactionColumn)
    TransactionListFrame.pack()

    listsArray.append(JobListFrame)
    listsArray.append(DateListFrame)
    listsArray.append(ReasonListFrame)
    listsArray.append(TransactionListFrame)
    return listsArray

def Scroll_Bar(ScrollFrame, listsArray):
    Scroll_Up = tk.CTkButton(master=ScrollFrame, text="Up", width=10, command=lambda: commands.Up_Button(listsArray, Scroll_Up))
    Scroll_Down = tk.CTkButton(master=ScrollFrame, text="Down", width=10, command=lambda: commands.Down_Button(listsArray, Scroll_Down))
    Scroll_Up.pack(side="top")
    Scroll_Down.pack(side="bottom")
    #Scroll_Up.configure(state="disabled")
    #Scroll_Down.configure(state="disabled")

def interface():
    UI = tk.CTk()
    UI.geometry("800x600")
    UI.title("Finance Tracker")

    ItemDisplay = tk.CTkFrame(master=UI)
    ItemDisplay.pack(side="left")
    masterListFrame = tk.CTkFrame(master=ItemDisplay, width=500)
    masterListFrame.pack_propagate(False)
    listsArray = Columns(masterListFrame)
    #labelFrame = tk.CTkFrame(master=masterListFrame)
    #Labelbox(labelFrame)
    #listFrame = tk.CTkFrame(master=masterListFrame)
    #listFrame.pack()
    masterListFrame.pack(side="left", padx=10, pady=10, fill="both")
    ScrollBar = tk.CTkFrame(master=ItemDisplay)
    Scroll_Bar(ScrollBar, listsArray)
    ScrollBar.pack(side="right", padx=10, pady=10, fill="y")
    
    EntryBox(UI, listsArray)
    

    

    OpenButton = tk.CTkButton(UI, text="Open", command=lambda: commands.Open_Button(UI, listsArray))
    OpenButton.place(relx=0.5, rely=0.6, anchor="center")

    SaveButton = tk.CTkButton(UI, text="Save", command=lambda: commands.Save_Button())
    SaveButton.place(relx=0.5, rely=0.65, anchor="center")
    
    return UI