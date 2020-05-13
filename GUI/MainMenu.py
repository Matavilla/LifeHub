import tkinter

def paramWindow(*args, **kwargs):
    win = tkinter.Tk()
    win.title('Parameters window')
 
    tkinter.Label(win, text="Текст0:").grid(row=0, column=0, sticky='W', padx=10, pady=10)
    winParam = tkinter.Spinbox(win, width=7, from_=0, to=100)
    winParam.grid(row=0, column=1, padx=10)
    tkinter.Label(win, text="Текст1:").grid(row=0, column=2, sticky='E')
    winParam = tkinter.Spinbox(win, width=7, from_=0, to=100)
    winParam.grid(row=0, column=3, sticky='E', padx=10)

    tkinter.Label(win, text="Текст2:").grid(row=1, column=0, sticky='W', padx=10, pady=10)
    winParam = tkinter.Spinbox(win, width=7, from_=0, to=100)
    winParam.grid(row=1, column=1, padx=10)
    tkinter.Label(win, text="Текст3:").grid(row=1, column=2, sticky='E')
    winParam = tkinter.Spinbox(win, width=7, from_=0, to=100)
    winParam.grid(row=1, column=3, sticky='E', padx=10)

    tkinter.Label(win, text="Текст4:").grid(row=2, column=0, sticky='W', padx=10, pady=10)
    winParam = tkinter.Spinbox(win, width=7, from_=0, to=100)
    winParam.grid(row=2, column=1, padx=10)
    tkinter.Label(win, text="Текст5:").grid(row=2, column=2, sticky='E')
    winParam = tkinter.Spinbox(win, width=7, from_=0, to=100)
    winParam.grid(row=2, column=3, sticky='E', padx=10)
    
    tkinter.Button(win, text="Фиксировать").grid(row=3, column=1, columnspan=2)

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
    ParamBtn.bind('<Button>', paramWindow)

    Btn = tkinter.Button(mainWindow, text = 'Начать симуляцию', font = 'Arial 24', bd = 5, width = 25)
    Btn.grid(row = 4, column = 2, padx = 20, pady = 20)

    mainWindow.mainloop()
