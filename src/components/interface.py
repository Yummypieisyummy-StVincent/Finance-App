#This file creates the components of the window and calls their functionality from commands.py

import customtkinter as tk
import commands
from tkcalendar import DateEntry

tk.set_appearance_mode("SystemDefault")
tk.set_default_color_theme("blue")

def EntryBox(masterFrame, listFrame):
    entryFrame = tk.CTkFrame(master=masterFrame)

    JobBox = tk.CTkEntry(master=entryFrame, placeholder_text="Job")
    JobBox.pack(anchor="center")

    ReasonBox = tk.CTkEntry(master=entryFrame, placeholder_text="Reason of transaction")
    ReasonBox.pack(anchor="center")

    TransactionBox = tk.CTkEntry(master=entryFrame, placeholder_text="Amount")
    TransactionBox.pack(anchor="center")

    DateBox = DateEntry(master=entryFrame)
    DateBox.pack(anchor="center")

    AddButton = tk.CTkButton(master=entryFrame, text="Add", command=lambda: [commands.Add_Button(TransactionBox.get(), str(DateBox.get_date()), ReasonBox.get(), JobBox.get()), commands.Clear_Text(JobBox, ReasonBox, DateBox, TransactionBox), commands.populateListbox(listFrame)])
    AddButton.pack(anchor="center")

    entryFrame.pack(side="right", padx=10, pady=10)


def Labelbox(labelFrame):

    jobIndexFrame = tk.CTkFrame(master=labelFrame)
    dateIndexFrame = tk.CTkFrame(master=labelFrame)
    reasonIndexFrame = tk.CTkFrame(master=labelFrame)
    transactionIndexFrame = tk.CTkFrame(master=labelFrame)

    jobIndex = tk.CTkLabel(master=jobIndexFrame, text="Job", width=100)
    jobIndex.pack(side="left", padx=10, fill="x")
    dateIndex = tk.CTkLabel(master=dateIndexFrame, text="Date", width=65)
    dateIndex.pack(side="left", padx=10, fill="x")
    reasonIndex = tk.CTkLabel(master=reasonIndexFrame, text="Reason", width=200)
    reasonIndex.pack(side="left", padx=10, fill="x")
    transactionIndex = tk.CTkLabel(master=transactionIndexFrame, text="Transaction")
    transactionIndex.pack(side="right", padx=10, fill="x")

    jobIndexFrame.pack(side="left")
    dateIndexFrame.pack(side="left")
    reasonIndexFrame.pack(side="left")
    transactionIndexFrame.pack(side="left")

    labelFrame.pack()

def Scroll_Bar(ScrollFrame, listFrame):
    Scroll_Up = tk.CTkButton(master=ScrollFrame, text="Up", width=10, command=lambda: commands.Up_Button(listFrame, Scroll_Up))
    Scroll_Down = tk.CTkButton(master=ScrollFrame, text="Down", width=10, command=lambda: commands.Down_Button(listFrame, Scroll_Down))
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
    labelFrame = tk.CTkFrame(master=masterListFrame)
    Labelbox(labelFrame)
    listFrame = tk.CTkFrame(master=masterListFrame)
    listFrame.pack()
    masterListFrame.pack(side="left", padx=10, pady=10, fill="both")
    ScrollBar = tk.CTkFrame(master=ItemDisplay)
    Scroll_Bar(ScrollBar, listFrame)
    ScrollBar.pack(side="right", padx=10, pady=10, fill="y")
    
    EntryBox(UI, listFrame)
    

    

    OpenButton = tk.CTkButton(UI, text="Open", command=lambda: commands.Open_Button(UI, listFrame))
    OpenButton.place(relx=0.5, rely=0.6, anchor="center")

    SaveButton = tk.CTkButton(UI, text="Save", command=lambda: commands.Save_Button())
    SaveButton.place(relx=0.5, rely=0.65, anchor="center")
    
    return UI