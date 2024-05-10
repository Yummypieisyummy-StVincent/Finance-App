import tkinter
import customtkinter as tk
import commands
from tkcalendar import DateEntry

tk.set_appearance_mode("SystemDefault")
tk.set_default_color_theme("blue")

def interface():
    UI = tk.CTk()
    UI.geometry("800x600")
    UI.title("Finance Tracker")

    JobBox = tk.CTkEntry(UI, placeholder_text="Job")
    JobBox.place(relx=0.5, rely=0.3, anchor="center")

    ReasonBox = tk.CTkEntry(UI, placeholder_text="Reason of transaction")
    ReasonBox.place(relx=0.5, rely=0.35, anchor="center")

    DateBox = DateEntry(UI)
    DateBox.place(relx=0.5, rely=0.45, anchor="center")

    AddBox = tk.CTkEntry(UI, placeholder_text="Amount")
    AddBox.place(relx=0.5, rely=0.4, anchor="center")

    AddButton = tk.CTkButton(UI, text="Add", command=lambda: commands.Add_Button(AddBox.get()))
    AddButton.place(relx=0.5, rely=0.5, anchor="center")

    OpenButton = tk.CTkButton(UI, text="Open", command=lambda: commands.Open_Button)
    OpenButton.place(relx=0.5, rely=0.6, anchor="center")
    return UI