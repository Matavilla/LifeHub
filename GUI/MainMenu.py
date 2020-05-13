import tkinter
import random

class WorldParameters:
    '''Сохранение параметров вселенной'''
    def __init__(self, tik = 0,    chaosMoment = 0,
                 amountOfFood = 0, amountOfPoison = 0,
                 biom1 = 0,        biom2 = 0,
                 biom3 = 0):
        self.tikOfUniverse = tik
        self.chaosMoment = chaosMoment
        self.amountOfFood = amountOfFood
        self.amountOfPoison = amountOfPoison
        #generation period of food and poison
        self.biom1 = biom1
        self.biom2 = biom2
        self.biom3 = biom3


    def check(self):
        print("Проверка параметров")


parameters = WorldParameters()

def addStr(win, _text1, _text2, _row, _from = 0, _to = 100):
    ''' Вспомогательная функция добавления строки
        таблицы в окно с параметрами.
        -> 2 spin бокса'''
    tkinter.Label(win, text=_text1).grid(row=_row, column=0, sticky='W', padx=10, pady=10)
    winParam1 = tkinter.Spinbox(win, width=7, from_=_from, to=_to)
    winParam1.grid(row=_row, column=1, padx=10)
    randButton1 = tkinter.Button(win, width=3)
    tkinter.Label(win, text=_text2).grid(row=_row, column=2, sticky='E')
    winParam2 = tkinter.Spinbox(win, width=7, from_=_from, to=_to)
    winParam2.grid(row=_row, column=3, sticky='E', padx=10)
    return winParam1, winParam2, randButton1, randButton2

def paramWindow(*args, **kwargs):
    '''Создание окна с параметрами вселенной и сохранение параметров'''
    def saveParameters(*args, **kwargs):
        '''Сохранить параметры'''
        global parameters
        parameters.tikOfUniverse = tik.get()
        parameters.chaosMoment = chaos.get()
        parameters.amountOfFood = food.get()
        parameters.amountOfPoison = poison.get()
        parameters.biom1 = biom1.get()
        parameters.biom2 = biom2.get()
        parameters.biom3 = biom3.get()

    win = tkinter.Tk()
    win.title('Parameters window')

    tik, chaos = addStr(win, "Тик вселенной", "Момент хаоса", 0, 0, 1000)
    food, poison = addStr(win, "Кол-во еды", "Кол-во яда:", 1, 0, 1000)

    tkinter.Label(win, text="Период генерации еды/яда").grid(row=2, column=1, sticky='W', columnspan=2)

    biom1, biom2 = addStr(win, "Биом 1:", "Биом 2:", 3)

    tkinter.Label(win, text="Биом 3:").grid(row=4, column=0, sticky='W', padx=10, pady=10)

    biom3 = tkinter.Spinbox(win, width=7, from_=0, to=100)
    biom3.grid(row=4, column=1, padx=10)
    
    button = tkinter.Button(win, text="Сохнанить")
    button.grid(row=5, column=1, columnspan=2)
    button.bind('<Button>', saveParameters)



def printParam(*args, **kwargs):
    ''' Вывести все параметры на экран (для проверки) '''
    global parameters
    print(f'tikOfUniverse = {parameters.tikOfUniverse}')
    print(f'chaosMoment = {parameters.chaosMoment}')
    print(f'amountOfFood = {parameters.amountOfFood}')
    print(f'amountOfPoison = {parameters.amountOfPoison}')
    print(f'biom1 = {parameters.biom1}')
    print(f'biom2 = {parameters.biom2}')
    print(f'biom3 = {parameters.biom3}')
    print('\n')


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

    startBtn.bind('<Button>', printParam)

    mainWindow.mainloop()
