#This file gives the functionality of the components from interface.py

import dataStorage
import itemClass
from datetime import date
from tkinter import *
import customtkinter as tk
from customtkinter import CTkToplevel

listOfEntries = []
startIndex = 0 # This specifies the start index of the list - used when scrolling through large lists of entries
# StatsFrameArray = [TotalMoney, TotalExpenses, TotalIncome, Ratio]
totalMoney = 0 # [0]
totalExpenses = 0 # [1]
totalIncome = 0 # [2]
ratio = 0 # [3]
savings_percentage = 0 # Global savings percentage setting
tax_percentage = 0 # Global tax percentage setting

if(len(listOfEntries) < 17):# This specifies the end index of the list - used when scrolling through large lists of entries
    endIndex = len(listOfEntries)
else:
    endIndex = 16

def sortByJob(listsArray, statsFrameArray, summaryFrameArray=None):
    global listOfEntries
    listOfEntries = sorted(listOfEntries, key=lambda x: x.job)
    populateListbox(listsArray, statsFrameArray, summaryFrameArray)

def sortByDate(listsArray, statsFrameArray, summaryFrameArray=None):
    global listOfEntries
    listOfEntries = sorted(listOfEntries, key=lambda x: x.date)
    populateListbox(listsArray, statsFrameArray, summaryFrameArray)

def sortByAmount(listsArray, statsFrameArray, summaryFrameArray=None):
    global listOfEntries
    listOfEntries = sorted(listOfEntries, key=lambda x: x.amount)
    populateListbox(listsArray, statsFrameArray, summaryFrameArray)

def calculate(statsFrameArray, summaryFrameArray=None):
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
    if totalMoney == 0:
        percentage = 100.0 if expenses != 0 else 0.0
    else:
        percentage = abs((expenses/totalMoney)*100.0)
    ratio = round(percentage, 2)
    statsFrameArray[3].configure(text="Expense Percentage: " + str(ratio) + "%")
    
    if summaryFrameArray is not None:
        taxable_income, _ = get_tax_summary()
        total_savings = get_total_savings()
        tax_pct = globals().get('tax_percentage', 0)
        tax_set_aside = round(taxable_income * (tax_pct / 100), 2)
        spending_money = round(totalIncome - total_savings - tax_set_aside, 2)
        spending_after_expenses = round(spending_money + totalExpenses, 2)
        summaryFrameArray[0].configure(text="Savings set aside: $" + str("%.2f" % total_savings))
        summaryFrameArray[1].configure(text="Tax set aside: $" + str("%.2f" % tax_set_aside))
        summaryFrameArray[2].configure(text="Spending money: $" + str("%.2f" % spending_money))
        summaryFrameArray[3].configure(text="Spending after expenses: $" + str("%.2f" % spending_after_expenses))
    #return totalMoney

def reeval_indices():
    global endIndex, startIndex
    if(len(listOfEntries) < 17):
        endIndex = len(listOfEntries)
    if(endIndex > len(listOfEntries)):
        endIndex = len(listOfEntries)
        startIndex = endIndex - 16

def populateListbox(listsArray, statsFrameArray, summaryFrameArray=None):
    global startIndex, endIndex

    if(len(listOfEntries) > 0):
        start = startIndex
        end = min(endIndex, len(listOfEntries))
        for list in listsArray:
            for entry in list.winfo_children():
                entry.destroy()
        for entry in range(start, end):
            job = tk.CTkLabel(master=listsArray[0], text=listOfEntries[entry].job)
            client = tk.CTkLabel(master=listsArray[1], text=listOfEntries[entry].client_name)
            date_label = tk.CTkLabel(master=listsArray[2], text=listOfEntries[entry].date)
            reason = tk.CTkLabel(master=listsArray[3], text=listOfEntries[entry].description)
            transaction = tk.CTkLabel(master=listsArray[4], text=str("%.2f" %listOfEntries[entry].amount))
            taxable = tk.CTkLabel(master=listsArray[5], text="Yes" if listOfEntries[entry].taxable else "No")
            savings = tk.CTkLabel(master=listsArray[6], text=str("%.2f" %get_entry_savings_amount(listOfEntries[entry])))
            def confirm_remove(entry_index=entry):
                Popup = CTkToplevel()
                Popup.grab_set()
                Popup.title("Confirm Delete")
                Popup.geometry("420x120")
                tk.CTkLabel(Popup, text="Delete this entry? This cannot be undone.").pack(padx=10, pady=10)
                tk.CTkButton(
                    Popup,
                    text="Delete",
                    fg_color="red",
                    command=lambda: [listOfEntries.pop(entry_index), reeval_indices(), populateListbox(listsArray, statsFrameArray, summaryFrameArray), calculate(statsFrameArray, summaryFrameArray), Popup.destroy()]
                ).pack(padx=10, pady=5)
                tk.CTkButton(Popup, text="Cancel", command=Popup.destroy).pack(padx=10, pady=5)

            removeButton = tk.CTkButton(master=listsArray[7], text="X", fg_color="red", command=confirm_remove)
            job.pack(padx=10)
            client.pack(padx=10)
            date_label.pack(padx=10)
            reason.pack(padx=10)
            transaction.pack(padx=10)
            taxable.pack(padx=10)
            savings.pack(padx=10)
            removeButton.pack()
        calculate(statsFrameArray, summaryFrameArray)

def get_entry_savings_amount(entry):
    """Calculate savings using entry override or global default."""
    if entry.amount <= 0:
        return 0.0
    percentage = entry.savings_percentage
    if percentage in (None, 0):
        percentage = savings_percentage
    return round(entry.amount * (percentage / 100), 2)

def Save_Button():
    if(listOfEntries != None):
        dataStorage.save(listOfEntries)
    else:
        print("No data to save")

def Clear_Text(JobBox, ReasonBox, DateBox, TransactionBox):
    JobBox.delete(0, 'end')
    ReasonBox.delete(0, 'end')
    DateBox.date = date.today()
    TransactionBox.delete(0, 'end')
    JobBox.placeholder_text = "Job"
    ReasonBox.placeholder_text = "Reason of transaction"
    TransactionBox.placeholder_text = "Amount"

def Add_Button(transactionBox, dateBox, reasonBox, jobBox, ItemDisplay):

    global listOfEntries, startIndex, endIndex

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
    
    if(ItemDisplay.winfo_ismapped() == False):
        ItemDisplay.pack()

    try:
        newEntry = itemClass.Entry(
            jobBox, 
            dateBox, 
            reasonBox, 
            float(transactionBox),
            category="-",
            client_name="-",
            taxable=False,
            payment_status="Pending",
            savings_percentage=savings_percentage
        )
        listOfEntries.append(newEntry)
        print(listOfEntries)
    except ValueError:
        print("Invalid input")
        newEntry = None
        return
    if(endIndex == len(listOfEntries)-1):
        endIndex += 1
        startIndex += 1
    if(len(listOfEntries) < 17):
        startIndex = 0
        endIndex = len(listOfEntries)

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

def Open_Button(UI, listsArray, statsFrameArray, summaryFrameArray, ItemDisplay):  
    global listOfEntries, startIndex, endIndex

    if((len(listOfEntries) != 0) and len(listOfEntries) > 0):
        Popup = CTkToplevel(UI)
        Popup.grab_set()
        Popup.title("Warning")
        Popup.geometry("500x100")
        tk.CTkLabel(Popup, text="Are you sure you want to open a new file? Current data will be overwritten!").pack()
        tk.CTkButton(Popup, text="Yes", command=lambda: [Overwrite_Button(), Popup.destroy(), Set_Start()]).pack()
        tk.CTkButton(Popup, text="No", command=Popup.destroy).pack()
    else:
        listOfEntries = dataStorage.load()
        if(listOfEntries == None):
            listOfEntries = []
        if((ItemDisplay.winfo_ismapped() == False) and (listOfEntries != [])):
            ItemDisplay.pack()
    if(listOfEntries != []):
        startIndex = 0
        if(len(listOfEntries) > 16):
            endIndex = 16
        else:
            endIndex = len(listOfEntries)
        populateListbox(listsArray, statsFrameArray, summaryFrameArray)

def Down_Button(listFrame, statsFrameArray, summaryFrameArray=None):
    global startIndex, endIndex
    start = startIndex
    end = endIndex
    if((startIndex < len(listOfEntries) - 16)):
        startIndex += 1
    if(endIndex < len(listOfEntries)):
        endIndex += 1
    if((startIndex != start) and (endIndex != end)):
    #    print("Test 1.Down")
        populateListbox(listFrame, statsFrameArray, summaryFrameArray)
    #if((startIndex == start) and (endIndex == end)):
    #    print("Test 2.Down")

def Up_Button(listFrame, statsFrameArray, summaryFrameArray=None):
    global startIndex, endIndex
    start = startIndex
    end = endIndex
    if(startIndex > 0):
        startIndex -= 1
    if(endIndex > 16):
        endIndex -= 1
    if((startIndex != start) and (endIndex != end)):
    #    print("Test 1.Up")
        populateListbox(listFrame, statsFrameArray, summaryFrameArray)
    #if((startIndex == start) and (endIndex == end)):
    #    print("Test 2.Up")

# ==================== REPORTING FUNCTIONS ====================

def get_tax_summary():
    """Calculate taxable vs non-taxable income"""
    taxable_income = 0.0
    non_taxable_income = 0.0
    
    for entry in listOfEntries:
        if entry.amount > 0:  # Only count income
            if entry.taxable:
                taxable_income += entry.amount
            else:
                non_taxable_income += entry.amount
    
    return round(taxable_income, 2), round(non_taxable_income, 2)

def get_total_savings():
    """Calculate total savings across all entries"""
    total = sum(get_entry_savings_amount(entry) for entry in listOfEntries)
    return round(total, 2)

def get_monthly_breakdown():
    """Group income by month"""
    monthly = {}
    for entry in listOfEntries:
        if entry.amount > 0:  # Only income
            month = entry.date[:7] if len(entry.date) >= 7 else entry.date  # Extract YYYY-MM
            if month not in monthly:
                monthly[month] = 0.0
            monthly[month] += entry.amount
    
    # Sort by month
    return {k: round(v, 2) for k, v in sorted(monthly.items())}

def get_category_breakdown():
    """Group income by category"""
    categories = {}
    for entry in listOfEntries:
        if entry.amount > 0:  # Only income
            cat = entry.category if entry.category != "-" else "Uncategorized"
            if cat not in categories:
                categories[cat] = 0.0
            categories[cat] += entry.amount
    
    # Sort by amount (descending)
    return {k: round(v, 2) for k, v in sorted(categories.items(), key=lambda x: x[1], reverse=True)}

def export_to_csv(filename=None):
    """Export all entries to CSV file"""
    if filename is None:
        import dataStorage as ds
        File = ds.filedialog.asksaveasfile(mode="w", filetypes=[("CSV Files", "*.csv")], defaultextension=".csv")
        if File is None:
            return False
        filename = File.name
        File.close()
    
    try:
        with open(filename, 'w', newline='') as f:
            # Write headers
            headers = "Date,Job/Place,Client,Category,Description,Amount,Taxable,Payment Status,Savings Amount\n"
            f.write(headers)
            
            # Write data
            for entry in listOfEntries:
                taxable_str = "Yes" if entry.taxable else "No"
                savings_amount = get_entry_savings_amount(entry)
                line = f"{entry.date},{entry.job},{entry.client_name},{entry.category},{entry.description},{entry.amount:.2f},{taxable_str},{entry.payment_status},{savings_amount:.2f}\n"
                f.write(line)
        
        print(f"CSV exported to {filename}")
        return True
    except Exception as e:
        print(f"Error exporting CSV: {e}")
        return False