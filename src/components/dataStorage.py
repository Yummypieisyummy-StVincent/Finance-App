from tkinter import filedialog
import json

file = None

def load(itemClassObject):
    global file
    file = filedialog.askopenfile(mode="r", filetypes=[("JSON Files", "*.json")], defaultextension=".json")
    if file is None:
        return
    itemClassObject.from_dict(json.load(file))
    return itemClassObject

def save(itemClassObject):
    global file
    if file is None:
        file = filedialog.asksaveasfile(mode="a", filetypes=[("JSON Files", "*.json")], defaultextension=".json")
    if file is None:
        return
    json.dump(itemClassObject.to_dict(), file, indent=1)