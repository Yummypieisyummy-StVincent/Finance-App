import dataStorage
import itemClass
from datetime import date
def Add_Button(transactionBox = 0.0, dateBox="-", reasonBox="-", jobBox="-"):
    try:
        newEntry = itemClass.Entry(jobBox, dateBox, reasonBox, float(transactionBox))
        dataStorage.save(newEntry)
    except ValueError:
        print("Invalid input: " + transactionBox + " - " + dateBox + " - " + reasonBox + " - " + jobBox)
        newEntry = None
        return

#def Open_Button():
#    currentFile = dataStorage.openFile()