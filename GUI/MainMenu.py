import tkinter


class WorldParameters:
    '''Сохранение параметров вселенной'''
    def __init__(self):
        self.update()

    def update(self, tik = 0, chaos = 0, food = 0, poison = 0, b1 = 0, b2 = 0, b3 = 0):
        self.TikUniverse = tik
        self.ChaosMoment = chaos
        self.AmountOfFood = food
        self.AmountOfPoison = poison
        #generation period of food and poison
        self.Biom1 = b1
        self.Biom2 = b2
        self.Biom3 = b3


    def check(self):
        print("Проверка параметров")


def addStr(win, _text1, _text2, _row, _from = 0, _to = 100):
    ''' Вспомогательная функция добавления строки
        таблицы в окно с параметрами.
        -> 2 spin бокса'''
    tkinter.Label(win, text=_text1).grid(row=_row, column=0, sticky='W', padx=10, pady=10)
    winParam1 = tkinter.Spinbox(win, width=7, from_=_from, to=_to)
    winParam1.grid(row=_row, column=1, padx=10)
    tkinter.Label(win, text=_text2).grid(row=_row, column=2, sticky='E')
    winParam2 = tkinter.Spinbox(win, width=7, from_=_from, to=_to)
    winParam2.grid(row=_row, column=3, sticky='E', padx=10)
    return winParam1, winParam2

def paramWindow(event, parameters):
    '''Создание окна с параметрами вселенной и сохранение параметров'''

    def saveParameters(event, parameters):
        '''Сохранить параметры'''

        parameters.update(tik.get(), 
                        chaos.get(),
                        food.get(), 
                        poison.get(), 
                        biom1.get(), 
                        biom2.get(), 
                        biom3.get())

    win = tkinter.Tk()
    win.title('Parameters window')

    tik, chaos = addStr(win, "Тик вселенной", "Момент хаоса", 0, 0, 1000)
    food, poison = addStr(win, "Кол-во еды", "Кол-во яда:", 1, 0, 1000)

    tkinter.Label(win, text="Период генерации еды/яда").grid(row=2, column=1, sticky='W', columnspan=2)

    biom1, biom2 = addStr(win, "Биом 1:", "Биом 2:", 3)

    tkinter.Label(win, text="Биом 3:").grid(row=4, column=0, sticky='W', padx=10, pady=10)

    biom3 = tkinter.Spinbox(win, width=7, from_=0, to=100)
    biom3.grid(row=4, column=1, padx=10)
    
    button = tkinter.Button(win, text="Сохранить")
    button.grid(row=5, column=1, columnspan=2)
    button.bind('<Button>', lambda event: saveParameters(event, parameters))



def printParam(event, parameters):
    ''' Вывести все параметры на экран (для проверки) '''

    print(f'tikOfUniverse = {parameters.TikUniverse}')
    print(f'chaosMoment = {parameters.ChaosMoment}')
    print(f'amountOfFood = {parameters.AmountOfFood}')
    print(f'amountOfPoison = {parameters.AmountOfPoison}')
    print(f'biom1 = {parameters.Biom1}')
    print(f'biom2 = {parameters.Biom2}')
    print(f'biom3 = {parameters.Biom3}')
    print('\n')


def StartMenu():
    wPar = WorldParameters()

    mainWindow = tkinter.Tk()
    mainWindow.configure(background='black')
    mainWindow.title('LIFEHUB')
    w = mainWindow.winfo_screenwidth()
    h = mainWindow.winfo_screenheight()
    mainWindow.geometry(f'{w // 2}x{h // 2}+{w // 2 - w // 4}+{h // 2 - h // 4}')
    mainWindow.columnconfigure(1, weight = 1)
    mainWindow.columnconfigure(3, weight = 1)
    mainWindow.rowconfigure(1, weight = 1)
    mainWindow.rowconfigure(5, weight = 1)
    

    startBtn = tkinter.Button(mainWindow, text = 'Начать симуляцию', font = 'Arial 24', bd = 5, width = 25, bg = "#FF8C00", activebackground = "#FF8C00")
    startBtn.grid(row = 2, column = 2, padx = 20, pady = 20)
    startBtn.bind('<Button>', lambda event: printParam(event, wPar))


    paramBtn = tkinter.Button(mainWindow, text = 'Задать параметры вселенной', font = 'Arial 24', bd = 5, width = 25, bg = "#FF8C00", activebackground = "#FF8C00")
    paramBtn.grid(row = 3, column = 2, padx = 20, pady = 20)
    paramBtn.bind('<Button>', lambda event: paramWindow(event, wPar))

#    btn = tkinter.Button(mainWindow, text = 'Начать симуляцию', font = 'Arial 24', bd = 5, width = 25)
#    btn.grid(row = 4, column = 2, padx = 20, pady = 20)

    mainWindow.mainloop()
