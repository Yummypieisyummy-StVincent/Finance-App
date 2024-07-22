#This file manages the data storage and load of the application

from tkinter import filedialog
import json
import itemClass
currentFileRead = None
currentFileWrite = None

def load():
    global currentFileWrite
    itemList = []
    file = filedialog.askopenfile(mode="r", filetypes=[("JSON Files", "*.json")], defaultextension=".json")
    if file is None:
        return
    try:
        currentFileWrite = open(file.name, "w")
        print(file)
        data = json.load(file)
        for entry in data:
            entry = itemClass.Entry(entry['job'], entry['date'], entry['description'], entry['amount'])
            itemList.append(entry)
    except json.JSONDecodeError:
        print("File could not be parsed.")
        itemList = []
    file.close()
    return itemList

def save(itemList):
    if(currentFileWrite is None):
        file = filedialog.asksaveasfile(mode="w", filetypes=[("JSON Files", "*.json")], defaultextension=".json")
        if file is None:
            return
        json.dump([item.to_dict() for item in itemList], file, indent=1)
        file.close()
    elif (currentFileWrite is not None):
        json.dump([item.to_dict() for item in itemList], currentFileWrite, indent=1)
        currentFileWrite.close()
