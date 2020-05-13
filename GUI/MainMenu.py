import tkinter

def StartMenu():
    mainWindow = tkinter.Tk()
    mainWindow.title('LIFEHUB')
    mainWindow.geometry('640x480')
    startBtn = tkinter.Button(mainWindow, text = 'Начать симуляцию', font = 'Arial 24')
    startBtn.grid(row="5", column="10", rowspan = "2", columnspan = "5")
    mainWindow.mainloop()
