#This file manages the data storage and load of the application

from tkinter import filedialog
import json
import itemClass
import os

currentFile = None
CONFIG_FILE = "config.json"
DEFAULT_CONFIG = {
    "savings_percentage": 0,
    "tax_percentage": 0,
    "window_width": 1200,
    "window_height": 700
}

def load_config():
    """Load configuration from config.json"""
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r') as f:
                config = json.load(f)
                # Merge with defaults to handle missing keys
                return {**DEFAULT_CONFIG, **config}
        except json.JSONDecodeError:
            print("Config file corrupted, using defaults")
            return DEFAULT_CONFIG
    else:
        # Create default config file
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG

def save_config(config):
    """Save configuration to config.json"""
    try:
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f, indent=2)
        print("Config saved")
    except Exception as e:
        print(f"Error saving config: {e}")

def load():
    global currentFile
    itemList = []
    File = filedialog.askopenfile(mode="r", filetypes=[("JSON Files", "*.json")], defaultextension=".json")
    if File is None:
        return
    try:
        print(File)
        data = json.load(File)
        for entry_data in data:
            entry = itemClass.Entry.from_dict(entry_data)
            itemList.append(entry)
    except json.JSONDecodeError:
        print("File could not be parsed.")
    File.close()
    currentFile = File.name
    return itemList

def save(itemList):
    global currentFile
    if currentFile is not None:
        try:
            with open(currentFile, "w") as File:
                json.dump([item.to_dict() for item in itemList], File, indent=2)
                print("File saved")
        except Exception as e:
            print(f"Error saving file: {e}")
    elif len(itemList) != 0:
        File = filedialog.asksaveasfile(mode="w", filetypes=[("JSON Files", "*.json")], defaultextension=".json")
        if File is None:
            return
        json.dump([item.to_dict() for item in itemList], File, indent=2)
        print("New file saved")
        currentFile = File.name
        File.close()

def close_program():
    #if(currentFile is not None):
    #    currentFile.close()
    print("File closed")