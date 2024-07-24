#This file manages the data storage and load of the application

from tkinter import filedialog
import json
import itemClass

currentFile = None

def load():
    global currentFile
    itemList = []
    File = filedialog.askopenfile(mode="r", filetypes=[("JSON Files", "*.json")], defaultextension=".json")
    if File is None:
        return
    try:
        print(File)
        data = json.load(File)
        for entry in data:
            entry = itemClass.Entry(entry['job'], entry['date'], entry['description'], entry['amount'])
            itemList.append(entry)
    except json.JSONDecodeError:
        print("File could not be parsed.")
    File.close()
    currentFile = File.name
    return itemList

def save(itemList):
    global currentFile
    File = open(currentFile, "w")
    if(File is not None):
        json.dump([item.to_dict() for item in itemList], File, indent=1)
        print("File saved")
        File.close()
    elif(File is None and len(itemList) != 0):
        File = filedialog.asksaveasfile(mode="w", filetypes=[("JSON Files", "*.json")], defaultextension=".json")
        if File is None:
            return
        json.dump([item.to_dict() for item in itemList], File, indent=1)
        print("New file saved")
        currentFile = File.name
        File.close()

def close_program():
    #if(currentFile is not None):
    #    currentFile.close()
    print("File closed")