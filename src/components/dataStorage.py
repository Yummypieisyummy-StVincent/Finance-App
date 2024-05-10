from tkinter import filedialog

def saveFile():
    currentFile = filedialog.asksaveasfilename()

def openFile():
    currentFile = filedialog.askopenfile(filetypes=[("Text Files", "*.txt")], defaultextension=".txt", title="Open File")
    return currentFile
