from tkinter import filedialog
import json

def load(itemList):
    file = filedialog.askopenfile(mode="r", filetypes=[("JSON Files", "*.json")], defaultextension=".json")
    if file is None:
        return
    try:
        data = json.load(file)
        for entry in data:
            itemList.append(entry)
    except json.JSONDecodeError:
        print("File could not be parsed.")
    file.close()
    return itemList

def save(itemList):
    file = filedialog.asksaveasfile(mode="w", filetypes=[("JSON Files", "*.json")], defaultextension=".json")
    if file is None:
        return
    json.dump({item.to_dict() for item in itemList}, file, indent=1)
    file.close()