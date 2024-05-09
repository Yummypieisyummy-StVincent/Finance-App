import tkinter
import customtkinter as tk
import commands
tk.set_appearance_mode("SystemDefault")
tk.set_default_color_theme("blue")

def interface():
    UI = tk.CTk()
    UI.geometry("800x600")
    UI.title("Finance Tracker")

    AddButton = tk.CTkButton(UI, text="Add", command=commands.Add_Button)
    AddButton.place(relx=0.5, rely=0.5, anchor="center")

    AddBox = tk.CTkEntry(UI)
    AddBox.place(relx=0.5, rely=0.4, anchor="center", userInput=commands.addBox)
    return UI