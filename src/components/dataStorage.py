from tkinter import filedialog
import json
import itemClass

def load():
    itemList = []
    file = filedialog.askopenfile(mode="r", filetypes=[("JSON Files", "*.json")], defaultextension=".json")
    if file is None:
        return
    try:
        print(file)
        data = json.load(file)
        for entry in data:
            entry = itemClass.Entry(entry['job'], entry['date'], entry['description'], entry['amount'])
            itemList.append(entry)
    except json.JSONDecodeError:
        print("File could not be parsed.")
    file.close()
    return itemList

def save(itemList):
    file = filedialog.asksaveasfile(mode="w", filetypes=[("JSON Files", "*.json")], defaultextension=".json")
    if file is None:
        return
    json.dump([item.to_dict() for item in itemList], file, indent=1)
    file.close()