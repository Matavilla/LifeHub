import tkinter

def StartMenu():
    mainWindow = tkinter.Tk()
    mainWindow.title('LIFEHUB')
    w = mainWindow.winfo_screenwidth()
    h = mainWindow.winfo_screenheight()
    mainWindow.geometry(f'{w // 2}x{h // 2}+{w // 2 - w // 4}+{h // 2 - h // 4}')
    mainWindow.columnconfigure(1, weight = 1)
    mainWindow.columnconfigure(3, weight = 1)
    mainWindow.rowconfigure(1, weight = 1)
    mainWindow.rowconfigure(5, weight = 1)
    

    startBtn = tkinter.Button(mainWindow, text = 'Начать симуляцию', font = 'Arial 24', bd = 5, width = 25)
    startBtn.grid(row = 2, column = 2, padx = 20, pady = 20)

    ParamBtn = tkinter.Button(mainWindow, text = 'Задать параметры вселенной', font = 'Arial 24', bd = 5, width = 25)
    ParamBtn.grid(row = 3, column = 2, padx = 20, pady = 20)

    Btn = tkinter.Button(mainWindow, text = 'Начать симуляцию', font = 'Arial 24', bd = 5, width = 25)
    Btn.grid(row = 4, column = 2, padx = 20, pady = 20)

    mainWindow.mainloop()
