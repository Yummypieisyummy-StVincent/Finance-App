from tkinter import filedialog
import json

file = None

def load(itemList):
    global file
    file = filedialog.askopenfile(mode="r", filetypes=[("JSON Files", "*.json")], defaultextension=".json")
    if file is None:
        return
    for entry in json.load(file):
        itemList.append(entry)
    #itemClassObject.from_dict(json.load(file))
    #return itemClassObject
    return itemList

def save(itemList):
    global file
    if file is None:
        file = filedialog.asksaveasfile(mode="w", filetypes=[("JSON Files", "*.json")], defaultextension=".json")
    if file is None:
        return
    json.dump(itemList, indent=1)