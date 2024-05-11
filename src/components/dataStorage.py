from tkinter import filedialog
import itemClass
import json

def save(itemClassObject):
    file = filedialog.asksaveasfile(mode="w", defaultextension=".json")
    if file is None:
        return
    json.dump(itemClassObject.to_dict(), file, indent=1)
    