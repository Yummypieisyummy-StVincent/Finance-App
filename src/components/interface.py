#This file creates the components of the window and calls their functionality from commands.py

import customtkinter as tk
import commands
from tkcalendar import DateEntry

tk.set_appearance_mode("SystemDefault")
tk.set_default_color_theme("blue")

listsArray = [] # This is the array that holds the job, date, reason, and transaction lists

def Entry_Box(masterFrame, listsArray, statsFrameArray):
    entryFrame = tk.CTkFrame(master=masterFrame)

    JobBox = tk.CTkEntry(master=entryFrame, placeholder_text="Job / Place")
    JobBox.pack(anchor="center")

    ReasonBox = tk.CTkEntry(master=entryFrame, placeholder_text="Reason of transaction")
    ReasonBox.pack(anchor="center")

    TransactionBox = tk.CTkEntry(master=entryFrame, placeholder_text="Amount")
    TransactionBox.pack(anchor="center")

    DateBox = DateEntry(master=entryFrame)
    DateBox.pack(anchor="center")

    AddButton = tk.CTkButton(master=entryFrame, text="Add", command=lambda: [commands.Add_Button(TransactionBox.get(), str(DateBox.get_date()), ReasonBox.get(), JobBox.get()), commands.Clear_Text(JobBox, ReasonBox, DateBox, TransactionBox), commands.populateListbox(listsArray, statsFrameArray)])
    AddButton.pack(anchor="center")

    entryFrame.pack(padx=10, pady=10)


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
    JobLabelFrame.pack(fill="x")
    DateLabelFrame.pack(fill="x")
    ReasonLabelFrame.pack(fill="x")
    TransactionLabelFrame.pack(fill="x")

    JobLabel = tk.CTkLabel(master=JobLabelFrame, text="Job/Place")
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

def Scroll_Bar(ScrollFrame, listsArray, statsFrameArray):
    Scroll_Up = tk.CTkButton(master=ScrollFrame, text="Up", width=10, command=lambda: commands.Up_Button(listsArray, statsFrameArray))
    Scroll_Down = tk.CTkButton(master=ScrollFrame, text="Down", width=10, command=lambda: commands.Down_Button(listsArray, statsFrameArray))
    Scroll_Up.pack(side="top", fill="x")
    Scroll_Down.pack(side="bottom")
    #Scroll_Up.configure(state="disabled")
    #Scroll_Down.configure(state="disabled")

def Stats_Box(masterFrame):
    statsArray = [tk.CTkLabel, tk.CTkLabel, tk.CTkLabel, tk.CTkLabel]
    statsFrame = tk.CTkFrame(master=masterFrame)

    statsArray[0] = totalLabel = tk.CTkLabel(master=statsFrame, text="Total: $" + str(commands.totalMoney))
    statsArray[1] = expensesLabel = tk.CTkLabel(master=statsFrame, text="Total Expenses: -$" + str(commands.totalExpenses))
    statsArray[2] = incomeLabel = tk.CTkLabel(master=statsFrame, text="Total Income: +$" + str(commands.totalIncome))
    statsArray[3] = incomeRatio = tk.CTkLabel(master=statsFrame, text="Expense Percentage: " + str(commands.ratio))


    totalLabel.pack()
    expensesLabel.pack()
    incomeLabel.pack()
    incomeRatio.pack()
    statsFrame.pack(padx=10, pady=10)
    return statsArray

def Sort_Button(masterFrame, listsArray, statsFrameArray):
    SortFrame = tk.CTkFrame(master=masterFrame)
    SortLabel = tk.CTkLabel(master=SortFrame, text="Sort by:")
    SortAmount = tk.CTkButton(master=SortFrame, text="Amount", command=lambda: [commands.sortByAmount(listsArray, statsFrameArray), commands.Set_Start(), commands.Set_End()])
    SortDate = tk.CTkButton(master=SortFrame, text="Date", command=lambda: [commands.sortByDate(listsArray, statsFrameArray), commands.Set_Start(), commands.Set_End()])
    SortJob = tk.CTkButton(master=SortFrame, text="Job", command=lambda: [commands.sortByJob(listsArray, statsFrameArray), commands.Set_Start(), commands.Set_End()])
    
    
    SortLabel.pack()
    SortAmount.pack()
    SortDate.pack()
    SortJob.pack()
    SortFrame.pack()

def interface():
    UI = tk.CTk()
    UI.geometry("1200x600")
    UI.title("Finance Tracker")

    FileFrame = tk.CTkFrame(master=UI) #This is the frame containing the list, scroll bar, and open/save buttons
    FileFrame.pack(padx=10, pady=10, side="left")

    statsFrame = tk.CTkFrame(master=UI)

    statsFrameArray = Stats_Box(statsFrame) #This is the frame containing the information about the transactions

    ItemDisplay = tk.CTkFrame(master=FileFrame) #This is the frame containing the list and scroll bar
    ItemDisplay.pack(side="top")

    masterListFrame = tk.CTkFrame(master=ItemDisplay, width=550, height=490) #This is the frame containing the list
    masterListFrame.pack_propagate(False)

    listsArray = Columns_(masterListFrame)
    Sort_Button(UI, listsArray, statsFrameArray)

    masterListFrame.pack(side="left", padx=10, pady=10, fill="both")

    ScrollBar = tk.CTkFrame(master=ItemDisplay)
    Scroll_Bar(ScrollBar, listsArray, statsFrameArray)
    ScrollBar.pack(side="right", padx=10, pady=10, fill="y")

    Entry_Box(statsFrame, listsArray, statsFrameArray)

    statsFrame.pack(side="right", padx=10, pady=10)

    OpenButton = tk.CTkButton(master=FileFrame, text="Open", command=lambda: commands.Open_Button(UI, listsArray, statsFrameArray))
    OpenButton.pack(side="bottom")

    SaveButton = tk.CTkButton(master=FileFrame, text="Save", command=lambda: commands.Save_Button())
    SaveButton.pack(side="bottom")

    return UI