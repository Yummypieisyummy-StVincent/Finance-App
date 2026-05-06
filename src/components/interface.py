#This file creates the components of the window and calls their functionality from commands.py

import customtkinter as tk
import commands
from tkcalendar import DateEntry

tk.set_appearance_mode("SystemDefault")
tk.set_default_color_theme("blue")

listsArray = [] # This is the array that holds the job, date, reason, and transaction lists

def Entry_Box(masterFrame, listsArray, statsFrameArray, summaryFrameArray, ItemDisplay):
    entryFrame = tk.CTkFrame(master=masterFrame)

    JobBox = tk.CTkEntry(master=entryFrame, placeholder_text="Job / Place")
    JobBox.pack(anchor="center", padx=5, pady=5)

    ClientBox = tk.CTkEntry(master=entryFrame, placeholder_text="Client Name")
    ClientBox.pack(anchor="center", padx=5, pady=5)

    ReasonBox = tk.CTkEntry(master=entryFrame, placeholder_text="Reason of transaction")
    ReasonBox.pack(anchor="center", padx=5, pady=5)

    TransactionBox = tk.CTkEntry(master=entryFrame, placeholder_text="Amount")
    TransactionBox.pack(anchor="center", padx=5, pady=5)

    DateBox = DateEntry(master=entryFrame)
    DateBox.pack(anchor="center", padx=5, pady=5)
    
    # Category dropdown
    CategoryBox = tk.CTkComboBox(master=entryFrame, values=["-", "Freelance", "Contract", "Side Gig", "Other"], state="readonly")
    CategoryBox.set("-")
    CategoryBox.pack(anchor="center", padx=5, pady=5)
    
    # Taxable checkbox
    TaxableVar = tk.BooleanVar()
    TaxableCheck = tk.CTkCheckBox(master=entryFrame, text="Taxable Income", variable=TaxableVar)
    TaxableCheck.pack(anchor="center", padx=5, pady=5)
    
    # Payment status dropdown
    StatusBox = tk.CTkComboBox(master=entryFrame, values=["Pending", "Paid", "Overdue"], state="readonly")
    StatusBox.set("Pending")
    StatusBox.pack(anchor="center", padx=5, pady=5)

    def submit_entry(event=None):
        """Submit entry on Enter key or button click"""
        # Create entry with new fields
        import itemClass
        try:
            amount = float(TransactionBox.get()) if TransactionBox.get() else 0.0
            new_entry = itemClass.Entry(
                job=JobBox.get() or "-",
                date=str(DateBox.get_date()),
                description=ReasonBox.get() or "-",
                amount=amount,
                category=CategoryBox.get(),
                client_name=ClientBox.get() or "-",
                taxable=TaxableVar.get(),
                payment_status=StatusBox.get(),
                savings_percentage=None
            )
            commands.listOfEntries.append(new_entry)
            
            # Update index window so new entries render
            if commands.endIndex == len(commands.listOfEntries) - 1:
                commands.endIndex += 1
                commands.startIndex += 1
            if len(commands.listOfEntries) < 17:
                commands.startIndex = 0
                commands.endIndex = len(commands.listOfEntries)
            
            # Update UI
            if ItemDisplay.winfo_ismapped() == False:
                ItemDisplay.pack()
            
            # Clear form
            JobBox.delete(0, 'end')
            ClientBox.delete(0, 'end')
            ReasonBox.delete(0, 'end')
            TransactionBox.delete(0, 'end')
            CategoryBox.set("-")
            TaxableVar.set(False)
            StatusBox.set("Pending")
            DateBox.set_date(None)
            
            commands.populateListbox(listsArray, statsFrameArray, summaryFrameArray)
            JobBox.focus()
            return "break"
        except ValueError:
            print("Invalid amount")
            return "break"

    AddButton = tk.CTkButton(master=entryFrame, text="Add", command=lambda: submit_entry())
    AddButton.pack(anchor="center", padx=5, pady=5)

    # Bind Enter key to submit entry
    JobBox.bind("<Return>", submit_entry)
    ClientBox.bind("<Return>", submit_entry)
    ReasonBox.bind("<Return>", submit_entry)
    TransactionBox.bind("<Return>", submit_entry)
    
    # Bind Tab key for navigation (default behavior, but made explicit)
    JobBox.bind("<Tab>", lambda e: ClientBox.focus() or "break")
    ClientBox.bind("<Tab>", lambda e: ReasonBox.focus() or "break")
    ReasonBox.bind("<Tab>", lambda e: TransactionBox.focus() or "break")
    TransactionBox.bind("<Tab>", lambda e: DateBox.focus() or "break")

    entryFrame.pack(side="left", padx=10, pady=10)
    return JobBox, ClientBox, ReasonBox, TransactionBox, DateBox  # Return entry fields for keyboard shortcut focus


def Columns_(parentFrame):

    global listsArray

    list_bg = parentFrame.cget("fg_color")

    JobColumn = tk.CTkFrame(master=parentFrame, fg_color=list_bg)
    ClientColumn = tk.CTkFrame(master=parentFrame, fg_color=list_bg)
    DateColumn = tk.CTkFrame(master=parentFrame, fg_color=list_bg)
    ReasonColumn = tk.CTkFrame(master=parentFrame, fg_color=list_bg)
    TransactionColumn = tk.CTkFrame(master=parentFrame, fg_color=list_bg)
    TaxableColumn = tk.CTkFrame(master=parentFrame, fg_color=list_bg)
    SavingsColumn = tk.CTkFrame(master=parentFrame, fg_color=list_bg)
    RemoveButtonColumn = tk.CTkFrame(master=parentFrame, width=30, fg_color=list_bg)

    JobColumn.pack(side="left", fill="y")
    ClientColumn.pack(side="left", fill="y")
    DateColumn.pack(side="left", fill="y")
    ReasonColumn.pack(side="left", fill="y")
    TransactionColumn.pack(side="left", fill="y")
    TaxableColumn.pack(side="left", fill="y")
    SavingsColumn.pack(side="left", fill="y")
    RemoveButtonColumn.pack_propagate(False)
    RemoveButtonColumn.pack(side="right", fill="y")
    

    JobLabelFrame = tk.CTkFrame(master=JobColumn, fg_color=list_bg)
    ClientLabelFrame = tk.CTkFrame(master=ClientColumn, fg_color=list_bg)
    DateLabelFrame = tk.CTkFrame(master=DateColumn, fg_color=list_bg)
    ReasonLabelFrame = tk.CTkFrame(master=ReasonColumn, fg_color=list_bg)
    TransactionLabelFrame = tk.CTkFrame(master=TransactionColumn, fg_color=list_bg)
    TaxableLabelFrame = tk.CTkFrame(master=TaxableColumn, fg_color=list_bg)
    SavingsLabelFrame = tk.CTkFrame(master=SavingsColumn, fg_color=list_bg)
    RemoveButtonLabelFrame = tk.CTkFrame(master=RemoveButtonColumn, fg_color=list_bg)

    JobLabelFrame.pack(fill="x")
    ClientLabelFrame.pack(fill="x")
    DateLabelFrame.pack(fill="x")
    ReasonLabelFrame.pack(fill="x")
    TransactionLabelFrame.pack(fill="x")
    TaxableLabelFrame.pack(fill="x")
    SavingsLabelFrame.pack(fill="x")
    RemoveButtonLabelFrame.pack(fill="x")

    JobLabel = tk.CTkLabel(master=JobLabelFrame, text="Job/Place")
    JobLabel.pack(padx=10, pady=10)
    ClientLabel = tk.CTkLabel(master=ClientLabelFrame, text="Client")
    ClientLabel.pack(padx=10, pady=10)
    DateLabel = tk.CTkLabel(master=DateLabelFrame, text="Date")
    DateLabel.pack(padx=10, pady=10)
    ReasonLabel = tk.CTkLabel(master=ReasonLabelFrame, text="Reason")
    ReasonLabel.pack(padx=10, pady=10)
    TransactionLabel = tk.CTkLabel(master=TransactionLabelFrame, text="Transaction")
    TransactionLabel.pack(padx=10, pady=10)
    TaxableLabel = tk.CTkLabel(master=TaxableLabelFrame, text="Taxable")
    TaxableLabel.pack(padx=10, pady=10)
    SavingsLabel = tk.CTkLabel(master=SavingsLabelFrame, text="Savings")
    SavingsLabel.pack(padx=10, pady=10)
    RemoveButtonLabel = tk.CTkLabel(master=RemoveButtonLabelFrame, text=" ")
    RemoveButtonLabel.pack(padx=10, pady=10)

    JobListFrame = tk.CTkFrame(master=JobColumn, fg_color=list_bg)
    JobListFrame.pack()
    ClientListFrame = tk.CTkFrame(master=ClientColumn, fg_color=list_bg)
    ClientListFrame.pack()
    DateListFrame = tk.CTkFrame(master=DateColumn, fg_color=list_bg)
    DateListFrame.pack()
    ReasonListFrame = tk.CTkFrame(master=ReasonColumn, fg_color=list_bg)
    ReasonListFrame.pack()
    TransactionListFrame = tk.CTkFrame(master=TransactionColumn, fg_color=list_bg)
    TransactionListFrame.pack()
    TaxableListFrame = tk.CTkFrame(master=TaxableColumn, fg_color=list_bg)
    TaxableListFrame.pack()
    SavingsListFrame = tk.CTkFrame(master=SavingsColumn, fg_color=list_bg)
    SavingsListFrame.pack()
    RemoveButtonListFrame = tk.CTkFrame(master=RemoveButtonColumn, fg_color=list_bg)
    RemoveButtonListFrame.pack()

    listsArray.append(JobListFrame)
    listsArray.append(ClientListFrame)
    listsArray.append(DateListFrame)
    listsArray.append(ReasonListFrame)
    listsArray.append(TransactionListFrame)
    listsArray.append(TaxableListFrame)
    listsArray.append(SavingsListFrame)
    listsArray.append(RemoveButtonListFrame)
    return listsArray

def Scroll_Bar(ScrollFrame, listsArray, statsFrameArray, summaryFrameArray):
    Scroll_Up = tk.CTkButton(master=ScrollFrame, text="Up", width=10, command=lambda: commands.Up_Button(listsArray, statsFrameArray, summaryFrameArray))
    Scroll_Down = tk.CTkButton(master=ScrollFrame, text="Down", width=10, command=lambda: commands.Down_Button(listsArray, statsFrameArray, summaryFrameArray))
    Scroll_Up.pack(side="top", fill="x")
    Scroll_Down.pack(side="bottom")
    #Scroll_Up.configure(state="disabled")
    #Scroll_Down.configure(state="disabled")

def Stats_Box(masterFrame, statsArray):
    statsArray[0] = totalLabel = tk.CTkLabel(master=masterFrame, text="Total: $" + str(commands.totalMoney))
    statsArray[1] = expensesLabel = tk.CTkLabel(master=masterFrame, text="Total Expenses: -$" + str(commands.totalExpenses))
    statsArray[2] = incomeLabel = tk.CTkLabel(master=masterFrame, text="Total Income: +$" + str(commands.totalIncome))
    statsArray[3] = incomeRatio = tk.CTkLabel(master=masterFrame, text="Expense Percentage: " + str(commands.ratio))

def Sort_Button(masterFrame, listsArray, statsFrameArray, summaryFrameArray):
    SortFrame = tk.CTkFrame(master=masterFrame)
    SortLabel = tk.CTkLabel(master=SortFrame, text="Sort by:")
    SortAmount = tk.CTkButton(master=SortFrame, text="Amount", command=lambda: [commands.sortByAmount(listsArray, statsFrameArray, summaryFrameArray), commands.Set_Start(), commands.Set_End()])
    SortDate = tk.CTkButton(master=SortFrame, text="Date", command=lambda: [commands.sortByDate(listsArray, statsFrameArray, summaryFrameArray), commands.Set_Start(), commands.Set_End()])
    SortJob = tk.CTkButton(master=SortFrame, text="Job", command=lambda: [commands.sortByJob(listsArray, statsFrameArray, summaryFrameArray), commands.Set_Start(), commands.Set_End()])
    
    
    SortLabel.pack()
    SortAmount.pack()
    SortDate.pack()
    SortJob.pack()
    SortFrame.pack(pady=10, padx=10)

def Settings_Button(masterFrame, app_config, statsFrameArray, summaryFrameArray):
    """Create settings button and modal for configuration"""
    def open_settings():
        settings_window = tk.CTkToplevel()
        settings_window.title("Settings")
        settings_window.geometry("400x260")
        
        # Savings percentage setting
        savings_label = tk.CTkLabel(settings_window, text="Savings Percentage (%):", font=("Helvetica", 12))
        savings_label.pack(padx=10, pady=10)
        
        savings_entry = tk.CTkEntry(settings_window)
        savings_entry.insert(0, str(app_config.get('savings_percentage', 0)))
        savings_entry.pack(padx=10, pady=5)

        tax_label = tk.CTkLabel(settings_window, text="Tax Percentage (%):", font=("Helvetica", 12))
        tax_label.pack(padx=10, pady=10)

        tax_entry = tk.CTkEntry(settings_window)
        tax_entry.insert(0, str(app_config.get('tax_percentage', 0)))
        tax_entry.pack(padx=10, pady=5)
        
        def save_settings():
            try:
                savings_pct = float(savings_entry.get())
                tax_pct = float(tax_entry.get())
                if not (0 <= savings_pct <= 100):
                    print("Savings percentage must be between 0 and 100")
                    return
                if not (0 <= tax_pct <= 100):
                    print("Tax percentage must be between 0 and 100")
                    return
                app_config['savings_percentage'] = savings_pct
                app_config['tax_percentage'] = tax_pct
                commands.savings_percentage = savings_pct
                commands.tax_percentage = tax_pct
                import dataStorage
                dataStorage.save_config(app_config)
                commands.calculate(statsFrameArray, summaryFrameArray)
                settings_window.destroy()
            except ValueError:
                print("Invalid percentage value")
        
        save_btn = tk.CTkButton(settings_window, text="Save", command=save_settings)
        save_btn.pack(padx=10, pady=10)
        
        settings_window.grab_set()
    
    SettingsButton = tk.CTkButton(master=masterFrame, text="⚙ Settings", command=open_settings)
    SettingsButton.pack(padx=10, pady=5)

def Reports_Window():
    """Create a reporting window with multiple views"""
    reports_window = tk.CTkToplevel()
    reports_window.title("Financial Reports")
    reports_window.geometry("700x600")
    
    # Create a scrollable frame for content
    main_frame = tk.CTkScrollableFrame(reports_window)
    main_frame.pack(padx=10, pady=10, fill="both", expand=True)
    
    # Tax Summary Section
    tax_frame = tk.CTkFrame(main_frame)
    tax_frame.pack(padx=10, pady=10, fill="x")
    
    tax_label = tk.CTkLabel(tax_frame, text="Tax Summary", font=("Helvetica", 14, "bold"))
    tax_label.pack(anchor="w", padx=5, pady=5)
    
    taxable, non_taxable = commands.get_tax_summary()
    tax_pct = commands.tax_percentage
    tax_set_aside = round(taxable * (tax_pct / 100), 2)
    tax_info = tk.CTkLabel(
        tax_frame,
        text=(
            f"Taxable Income: ${taxable:.2f}\n"
            f"Non-Taxable Income: ${non_taxable:.2f}\n"
            f"Tax Percentage: {tax_pct}%\n"
            f"Tax to Set Aside: ${tax_set_aside:.2f}"
        ),
        justify="left"
    )
    tax_info.pack(anchor="w", padx=20, pady=5)
    
    # Savings Summary Section
    savings_frame = tk.CTkFrame(main_frame)
    savings_frame.pack(padx=10, pady=10, fill="x")
    
    savings_label = tk.CTkLabel(savings_frame, text="Savings Tracking", font=("Helvetica", 14, "bold"))
    savings_label.pack(anchor="w", padx=5, pady=5)
    
    total_savings = commands.get_total_savings()
    savings_pct = commands.savings_percentage
    savings_info = tk.CTkLabel(
        savings_frame,
        text=f"Savings Percentage: {savings_pct}%\nSavings to Set Aside: ${total_savings:.2f}",
        justify="left"
    )
    savings_info.pack(anchor="w", padx=20, pady=5)

    # Total Set Aside Section
    total_set_aside_frame = tk.CTkFrame(main_frame)
    total_set_aside_frame.pack(padx=10, pady=10, fill="x")

    total_set_aside_label = tk.CTkLabel(total_set_aside_frame, text="Total", font=("Helvetica", 14, "bold"))
    total_set_aside_label.pack(anchor="w", padx=5, pady=5)

    total_set_aside = round(total_savings + tax_set_aside, 2)
    total_income = round(taxable + non_taxable, 2)
    total_set_aside_info = tk.CTkLabel(
        total_set_aside_frame,
        text=f"Total Income: ${total_income:.2f}\nTotal to Set Aside: ${total_set_aside:.2f}",
        justify="left"
    )
    total_set_aside_info.pack(anchor="w", padx=20, pady=5)
    
    # Monthly Breakdown Section
    monthly_frame = tk.CTkFrame(main_frame)
    monthly_frame.pack(padx=10, pady=10, fill="x")
    
    monthly_label = tk.CTkLabel(monthly_frame, text="Monthly Income Breakdown", font=("Helvetica", 14, "bold"))
    monthly_label.pack(anchor="w", padx=5, pady=5)
    
    monthly_data = commands.get_monthly_breakdown()
    if monthly_data:
        monthly_text = "\n".join([f"{month}: ${amount:.2f}" for month, amount in monthly_data.items()])
        monthly_info = tk.CTkLabel(monthly_frame, text=monthly_text, justify="left")
    else:
        monthly_info = tk.CTkLabel(monthly_frame, text="No income data")
    monthly_info.pack(anchor="w", padx=20, pady=5)
    
    # Category Breakdown Section
    category_frame = tk.CTkFrame(main_frame)
    category_frame.pack(padx=10, pady=10, fill="x")
    
    category_label = tk.CTkLabel(category_frame, text="Income by Category", font=("Helvetica", 14, "bold"))
    category_label.pack(anchor="w", padx=5, pady=5)
    
    category_data = commands.get_category_breakdown()
    if category_data:
        category_text = "\n".join([f"{cat}: ${amount:.2f}" for cat, amount in category_data.items()])
        category_info = tk.CTkLabel(category_frame, text=category_text, justify="left")
    else:
        category_info = tk.CTkLabel(category_frame, text="No category data")
    category_info.pack(anchor="w", padx=20, pady=5)
    
    # Export Button
    export_frame = tk.CTkFrame(main_frame)
    export_frame.pack(padx=10, pady=10, fill="x")
    
    export_btn = tk.CTkButton(export_frame, text="Export to CSV", command=lambda: commands.export_to_csv() and reports_window.after(500, lambda: print("Export complete")))
    export_btn.pack(anchor="center", padx=5, pady=5)
    
    reports_window.grab_set()

def Summary_Box(masterFrame, summaryArray):
    summaryArray[0] = tk.CTkLabel(master=masterFrame, text="Savings set aside: $0.00")
    summaryArray[1] = tk.CTkLabel(master=masterFrame, text="Tax set aside: $0.00")
    summaryArray[2] = tk.CTkLabel(master=masterFrame, text="Spending money: $0.00")
    summaryArray[3] = tk.CTkLabel(master=masterFrame, text="Spending after expenses: $0.00")

def interface(app_config=None):
    if app_config is None:
        app_config = {"savings_percentage": 0, "tax_percentage": 0, "window_width": 1200, "window_height": 700}
    
    # Store config in commands module for access
    commands.savings_percentage = app_config.get('savings_percentage', 0)
    commands.tax_percentage = app_config.get('tax_percentage', 0)
    
    UI = tk.CTk()
    window_width = app_config.get('window_width', 1200)
    window_height = app_config.get('window_height', 700)
    UI.geometry(f"{window_width}x{window_height}")
    UI.title("Finance Tracker")

    FileFrame = tk.CTkFrame(master=UI) #This is the frame containing the list, scroll bar, and open/save buttons
    FileFrame.pack(padx=10, pady=10, side="left")

    rightFrame = tk.CTkFrame(master=UI) # Contains the stats and the entry box
    statsFrameArray = [tk.CTkLabel, tk.CTkLabel, tk.CTkLabel, tk.CTkLabel] # This is the array that holds the stats labels, PACKED LATER
    Stats_Box(rightFrame, statsFrameArray) #This is the frame containing the information about the transactions
    summaryFrameArray = [tk.CTkLabel, tk.CTkLabel, tk.CTkLabel, tk.CTkLabel]

    Settings_Button(rightFrame, app_config, statsFrameArray, summaryFrameArray)
    
    ItemDisplay = tk.CTkFrame(master=FileFrame) #This is the frame containing the list and scroll bar
    #ItemDisplay.pack(side="top") #  <-------------

    masterListFrame = tk.CTkFrame(master=ItemDisplay, width=700, height=500) #This is the frame containing the list
    masterListFrame.pack_propagate(False)

    listsArray = Columns_(masterListFrame)
    Sort_Button(rightFrame, listsArray, statsFrameArray, summaryFrameArray)

    for label in statsFrameArray: #This is where stats are packed
        label.pack()

    masterListFrame.pack(side="left", padx=10, pady=10, fill="both")

    ScrollBar = tk.CTkFrame(master=ItemDisplay)
    Scroll_Bar(ScrollBar, listsArray, statsFrameArray, summaryFrameArray)
    ScrollBar.pack(side="right", padx=10, pady=10, fill="y")

    sidePanelFrame = tk.CTkFrame(master=rightFrame)
    sidePanelFrame.pack(padx=10, pady=10)

    summaryPanelFrame = tk.CTkFrame(master=sidePanelFrame)
    Summary_Box(summaryPanelFrame, summaryFrameArray)
    summaryPanelFrame.pack(side="left", padx=10, pady=10, fill="y")

    for label in summaryFrameArray:
        label.pack(anchor="w", padx=10, pady=5)

    entry_fields = Entry_Box(sidePanelFrame, listsArray, statsFrameArray, summaryFrameArray, ItemDisplay)

    rightFrame.pack(side="right", padx=10, pady=10)

    OpenButton = tk.CTkButton(master=FileFrame, text="Open", command=lambda: commands.Open_Button(UI, listsArray, statsFrameArray, summaryFrameArray, ItemDisplay))
    OpenButton.pack(side="bottom", padx=5, pady=5)

    SaveButton = tk.CTkButton(master=FileFrame, text="Save", command=lambda: commands.Save_Button())
    SaveButton.pack(side="bottom", padx=5, pady=5)
    
    ReportsButton = tk.CTkButton(master=FileFrame, text="📊 Reports", command=lambda: Reports_Window())
    ReportsButton.pack(side="bottom", padx=5, pady=5)

    # Keyboard shortcuts
    UI.bind("<Control-s>", lambda e: commands.Save_Button())
    UI.bind("<Control-l>", lambda e: commands.Open_Button(UI, listsArray, statsFrameArray, summaryFrameArray, ItemDisplay))

    return UI