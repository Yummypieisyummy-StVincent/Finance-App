import dataStorage
addBox = None
def Add_Button(newVal):
    try:
        addBox = float(newVal)
        print("Add")
        print(newVal)
    except ValueError:
        print("You must enter a number")
        print(addBox)

def Open_Button():
    currentFile = dataStorage.openFile()