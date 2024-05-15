import customtkinter as tk
import commands
from tkcalendar import DateEntry

tk.set_appearance_mode("SystemDefault")
tk.set_default_color_theme("blue")

def gridLayout(masterFrame):
    masterFrame.rowconfigure(0, weight=1)
    masterFrame.rowconfigure(1, weight=1)
    masterFrame.columnconfigure(0, weight=1)
    masterFrame.columnconfigure(1, weight=1)
    masterFrame.columnconfigure(2, weight=1)

def centerWindow(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def EntryBox(masterFrame):
    entryFrame = tk.CTkFrame(master=masterFrame)
    #entryFrame.grid(row = 1, column = 2)

    JobBox = tk.CTkEntry(master=entryFrame, placeholder_text="Job")
    JobBox.pack(anchor="center")

    ReasonBox = tk.CTkEntry(master=entryFrame, placeholder_text="Reason of transaction")
    ReasonBox.pack(anchor="center")

    TransactionBox = tk.CTkEntry(master=entryFrame, placeholder_text="Amount")
    TransactionBox.pack(anchor="center")

    DateBox = DateEntry(master=entryFrame)
    DateBox.pack(anchor="center")

    AddButton = tk.CTkButton(master=entryFrame, text="Add", command=lambda: [commands.Add_Button(TransactionBox.get(), str(DateBox.get_date()), ReasonBox.get(), JobBox.get()), commands.Clear_Text(JobBox, ReasonBox, DateBox, TransactionBox)])
    AddButton.pack(anchor="center")

    entryFrame.pack(side="right", padx=10, pady=10)

def Listbox(masterFrame):
    listFrame = tk.CTkFrame(master=masterFrame)
    itemFrame1 = tk.CTkFrame(master=listFrame)
    itemFrame2 = tk.CTkFrame(master=listFrame)
    itemFrame3 = tk.CTkFrame(master=listFrame)
    itemFrame4 = tk.CTkFrame(master=listFrame)
    itemFrame5 = tk.CTkFrame(master=listFrame)

    jobIndex = tk.CTkLabel(master=itemFrame1, text="Job")
    jobIndex.pack(side="left", padx=10)
    dateIndex = tk.CTkLabel(master=itemFrame1, text="Date")
    dateIndex.pack(side="left", padx=10)
    reasonIndex = tk.CTkLabel(master=itemFrame1, text="Reason")
    reasonIndex.pack(side="left", padx=10)
    transactionIndex = tk.CTkLabel(master=itemFrame1, text="Transaction")
    transactionIndex.pack(side="left", padx=10)

    listFrame.pack(side="left", padx=10, pady=10)

    #listFrame.grid(row=0, column=0, columnspan=2, sticky="nsew")
    itemFrame1.pack()
    itemFrame2.pack()
    itemFrame3.pack()
    itemFrame4.pack()
    itemFrame5.pack()


def interface():
    UI = tk.CTk()
    UI.geometry("800x600")
    #centerWindow(UI)
    UI.title("Finance Tracker")


    #gridLayout(UI)
    Listbox(UI)
    EntryBox(UI)
    
    

    #OpenButton = tk.CTkButton(UI, text="Open", command=lambda: commands.Open_Button(UI))
    #OpenButton.place(relx=0.5, rely=0.6, anchor="center")
#
    #SaveButton = tk.CTkButton(UI, text="Save", command=lambda: commands.Save_Button())
    #SaveButton.place(relx=0.5, rely=0.65, anchor="center")
    
    return UI