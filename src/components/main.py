import interface, dataStorage, commands
from tkinter.messagebox import askyesnocancel

# Load configuration on startup
app_config = dataStorage.load_config()

def window_close():
    answer = askyesnocancel("Exit", "Do you want to save before exiting?")
    if answer:
        dataStorage.save(commands.listOfEntries)
        #dataStorage.close_program()
        Application.quit()
    elif answer == False:
        #dataStorage.close_program()
        Application.quit()

Application = interface.interface(app_config)

Application.protocol("WM_DELETE_WINDOW", window_close)
Application.mainloop()