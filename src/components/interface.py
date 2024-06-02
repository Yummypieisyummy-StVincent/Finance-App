#This file creates the components of the window and calls their functionality from commands.py

import customtkinter as tk
import commands
from tkcalendar import DateEntry

tk.set_appearance_mode("SystemDefault")
tk.set_default_color_theme("blue")

listsArray = []

def Entry_Box(masterFrame, listsArray):
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


def Columns_(parentFrame):

    global listsArray

    JobColumn = tk.CTkFrame(master=parentFrame)
    DateColumn = tk.CTkFrame(master=parentFrame)
    ReasonColumn = tk.CTkFrame(master=parentFrame)
    TransactionColumn = tk.CTkFrame(master=parentFrame)
    JobColumn.pack(side="left", fill="y")
    DateColumn.pack(side="left", fill="y")
    ReasonColumn.pack(side="left", fill="y")
    TransactionColumn.pack(side="left", fill="y")

    JobLabelFrame = tk.CTkFrame(master=JobColumn)

    DateLabelFrame = tk.CTkFrame(master=DateColumn)

    ReasonLabelFrame = tk.CTkFrame(master=ReasonColumn)
    TransactionLabelFrame = tk.CTkFrame(master=TransactionColumn)
    JobLabelFrame.pack()
    DateLabelFrame.pack()
    ReasonLabelFrame.pack()
    TransactionLabelFrame.pack()

    JobLabel = tk.CTkLabel(master=JobLabelFrame, text="Job")
    JobLabel.pack(padx=10, pady=10)
    DateLabel = tk.CTkLabel(master=DateLabelFrame, text="Date")
    DateLabel.pack(padx=10, pady=10)
    ReasonLabel = tk.CTkLabel(master=ReasonLabelFrame, text="Reason")
    ReasonLabel.pack(padx=10, pady=10)
    TransactionLabel = tk.CTkLabel(master=TransactionLabelFrame, text="Transaction")
    TransactionLabel.pack(padx=10, pady=10)

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
    masterListFrame = tk.CTkFrame(master=ItemDisplay, width=550)
    masterListFrame.pack_propagate(False)
    listsArray = Columns_(masterListFrame)
    masterListFrame.pack(side="left", padx=10, pady=10, fill="both")
    ScrollBar = tk.CTkFrame(master=ItemDisplay)
    Scroll_Bar(ScrollBar, listsArray)
    ScrollBar.pack(side="right", padx=10, pady=10, fill="y")
    
    Entry_Box(UI, listsArray)
    

    FileFrame = tk.CTkFrame(master=UI)

    OpenButton = tk.CTkButton(master=FileFrame, text="Open", command=lambda: commands.Open_Button(UI, listsArray))
    OpenButton.pack()

    SaveButton = tk.CTkButton(master=FileFrame, text="Save", command=lambda: commands.Save_Button())
    SaveButton.pack()

    FileFrame.pack(padx=10, pady=10)
    
    return UI