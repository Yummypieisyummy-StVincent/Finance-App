import customtkinter as tk
import commands
from tkcalendar import DateEntry

tk.set_appearance_mode("SystemDefault")
tk.set_default_color_theme("blue")

def EntryBox(masterFrame):
    JobBox = tk.CTkEntry(master=masterFrame, placeholder_text="Job")
    JobBox.place(relx=0.5, rely=0.3, anchor="center")

    ReasonBox = tk.CTkEntry(master=masterFrame, placeholder_text="Reason of transaction")
    ReasonBox.place(relx=0.5, rely=0.35, anchor="center")

    TransactionBox = tk.CTkEntry(master=masterFrame, placeholder_text="Amount")
    TransactionBox.place(relx=0.5, rely=0.4, anchor="center")

    DateBox = DateEntry(master=masterFrame)
    DateBox.place(relx=0.5, rely=0.45, anchor="center")

    AddButton = tk.CTkButton(master=masterFrame, text="Add", command=lambda: [commands.Add_Button(TransactionBox.get(), str(DateBox.get_date()), ReasonBox.get(), JobBox.get()), commands.Clear_Text(JobBox, ReasonBox, DateBox, TransactionBox)])
    AddButton.place(relx=0.5, rely=0.5, anchor="center")

def interface():
    UI = tk.CTk()
    UI.geometry("800x600")
    UI.title("Finance Tracker")

    EntryBox(UI)
    

    OpenButton = tk.CTkButton(UI, text="Open", command=lambda: commands.Open_Button())
    OpenButton.place(relx=0.5, rely=0.6, anchor="center")

    SaveButton = tk.CTkButton(UI, text="Save", command=lambda: commands.Save_Button())
    SaveButton.place(relx=0.5, rely=0.65, anchor="center")
    
    return UI