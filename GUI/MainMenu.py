import tkinter
from tkinter import messagebox
from random import randint

COUNT = 0
WINDOWS = list()

class WorldParameters:
    '''Параметры вселенной'''

    Scale = {'little': 4, 'medium': 2, 'large': 1}

    def __init__(self):
        self.update()

    def update(self, tick = 0, chaos = 0,  food = 0, poison = 0,
               t_1 = 0,t_2 = 0, t_3 = 0, numB1 = 0, numB2 = 0,
               numB3 = 0, mode = "large"):
        self.TickUniverse = int(tick)
        self.ChaosMoment = int(chaos)
        self.AmountOfFood = int(food)
        self.AmountOfPoison = int(poison)
        #generation period of food and poison
        self.T_1 = int(t_1)
        self.T_2 = int(t_2)
        self.T_3 = int(t_3)

        #start number of bots in each bioms
        self.NumBots1 = int(numB1)
        self.NumBots2 = int(numB2)
        self.NumBots3 = int(numB3)

        self.set_world_size(mode)

    def set_world_size(self, mode):
        MAX_WORLD_SIZE = 400
        self.WorldSize = MAX_WORLD_SIZE // self.Scale[mode]

    def __bool__(self):
        print("[LOG] Проверка параметров")
        if not 0 < self.TickUniverse < 1000:
            return False
        if not 0 < self.ChaosMoment < 1000:
            return False
        if not 0 < self.AmountOfFood < 1000:
            return False
        if not 0 < self.AmountOfPoison < 1000:
            return False
        if not 0 < self.T_1 < 1000:
            return False
        if not 0 < self.T_2 < 1000:
            return False
        if not 0 < self.T_3 < 1000:
            return False
        if not 0 < self.NumBots1 < 100:
            return False
        if not 0 < self.NumBots2 < 100:
            return False
        if not 0 < self.NumBots3 < 100:
            return False
        print("[LOG] OK")
        return True

    def print_in_log(self):
        print(f'TickOfUniverse = {self.TickUniverse}')
        print(f'ChaosMoment = {self.ChaosMoment}')
        print(f'AmountOfFood = {self.AmountOfFood}')
        print(f'AmountOfPoison = {self.AmountOfPoison}')
        print(f'Biom1 = {self.Biom1}')
        print(f'Biom2 = {self.Biom2}')
        print(f'Biom3 = {self.Biom3}')
        print(f'NumBots1 = {self.NumBots1}')
        print(f'NumBots2 = {self.NumBots2}')
        print(f'NumBots3 = {self.NumBots3}')
        print(f'WorldSize = {self.WorldSize}')
        print('\n')


def InfoParameters():
    messagebox.showinfo("Information", "BLA BLA BLA")

def CloseWindow(win):
    global COUNT
    COUNT = 0
    win.destroy()

def CloseAllWindow():
    global WINDOWS
    for i in WINDOWS:
        CloseWindow(i)


def AddStrOfTable(win, _text1, _text2, _row, _from = 1, _to = 99):
    ''' Вспомогательная функция добавления строки
        таблицы в окно с параметрами.
        -> 2 spin бокса и 2 кнопки'''
    tkinter.Label(win, text=_text1).grid(row=_row, column=0, sticky='W', padx=10, pady=10)
    winParam1 = tkinter.Spinbox(win, width=7, from_=_from, to=_to)
    winParam1.grid(row=_row, column=1, padx=10)
    randButton1 = tkinter.Button(win, text="rand", width=4)
    randButton1.grid(row=_row, column=2, sticky='W')
    tkinter.Label(win, text=_text2).grid(row=_row, column=3, sticky='E')
    winParam2 = tkinter.Spinbox(win, width=7, from_=_from, to=_to)
    winParam2.grid(row=_row, column=4, sticky='W', padx=10)
    randButton2 = tkinter.Button(win, text="rand", width=4)
    randButton2.grid(row=_row, column=5, sticky='W')
    tkinter.Label(win, text= "").grid(row=_row, column=6, sticky='W', padx=10, pady=10) #I KNOW IT IS BAD, I WILL FIX IT LATER
    return winParam1, winParam2, randButton1, randButton2


def RandValue(vidget, _from, to):
        vidget.delete(0, tkinter.END)
        vidget.insert(0, randint(_from, to))

def OldVariables(allvid : dict) -> None:
    for vidget in allvid:
        vidget.delete(0, tkinter.END)
        vidget.insert(0, allvid[vidget])

def ParamWindow(parameters):
    '''Создание окна с параметрами вселенной и сохранение параметров'''
    def SaveParameters(parameters):
        '''Сохранить параметры'''
        parameters.update(tick.get(),
                          chaos.get(),
                          food.get(),
                          poison.get(),
                          biom1.get(),
                          biom2.get(),
                          biom3.get(),
                          numBots1.get(),
                          numBots2.get(),
                          numBots3.get())
        if not parameters:
            messagebox.showerror("Error", "Wrong value of parameters")


    def FullRandom(*args, **kwargs):
        '''установка рандомных параметров в заданных
           интервалах'''
        RandValue(tick, 1, 999)
        RandValue(chaos, 1, 999)
        RandValue(food, 1, 999)
        RandValue(poison, 1, 999)

        RandValue(biom1, 1, 999)
        RandValue(biom2, 1, 999)
        RandValue(biom3, 1, 999)

        RandValue(numBots1, 1, 99)
        RandValue(numBots2, 1, 99)
        RandValue(numBots3, 1, 99)

        SaveParameters(parameters)


    global COUNT, WINDOWS
    COUNT += 1
    if COUNT > 1:
        COUNT -= 1
        return
    
    win = tkinter.Tk()
    WINDOWS.append(win)

    win.title('Parameters window')
    win.protocol("WM_DELETE_WINDOW", lambda: CloseWindow(win))
    VidgAccord = dict() #This is the dictionary to match the name of the variable is a class field
 
    tick, chaos, randTick, randChaos = AddStrOfTable(win, "Тик вселенной", "Момент хаоса", 0, 1, 999)
    VidgAccord.update({tick:parameters.TickUniverse,chaos:parameters.ChaosMoment})
    food, poison, randFood, randPoison = AddStrOfTable(win, "Кол-во еды", "Кол-во яда:", 2, 1, 999)
    VidgAccord.update({food: parameters.AmountOfFood, poison: parameters.AmountOfPoison})
    randTick.bind('<Button>', lambda event: RandValue(tick, 1, 999))
    randChaos.bind('<Button>', lambda event: RandValue(chaos, 1, 999))
    randFood.bind('<Button>', lambda event: RandValue(food, 1, 999))
    randPoison.bind('<Button>', lambda event: RandValue(poison, 1, 999))

    tkinter.Label(win, text="Период генерации еды/яда").grid(row=4, column=3, sticky='W', columnspan=2)

    biom1, biom2, randBiom1, randBiom2 = AddStrOfTable(win, "Биом 1:", "Биом 2:", 5,1,999)
    VidgAccord.update({biom1: parameters.Biom1, biom2: parameters.Biom2})
    # biom1, biom2, randBiom1, randBiom2 = AddStrOfTable(win, "Биом 1:", "Биом 2:", 5)
    randBiom1.bind('<Button>', lambda event: RandValue(biom1, 1, 999))
    randBiom2.bind('<Button>', lambda event: RandValue(biom2, 1, 999))

    tkinter.Label(win, text="Биом 3:").grid(row=7, column=0, sticky='W', padx=10, pady=10)
    biom3 = tkinter.Spinbox(win, width=7, from_=1, to=99, textvariable=4)
    biom3.grid(row=7, column=1, padx=10)
    VidgAccord.update({biom3: parameters.Biom3})
    randBiom3 = tkinter.Button(win, text="rand", width=4)
    randBiom3.grid(row=7, column=2, sticky='W')
    randBiom3.bind('<Button>', lambda event: RandValue(biom3, 1, 999))


    tkinter.Label(win, text="Начальное кол-во ботов").grid(row=8, column=3, sticky='W', columnspan=2)

    numBots1, numBots2, randBots1, randBots2 = AddStrOfTable(win, "Биом 1:", "Биом 2:", 9, 1, 99)
    VidgAccord.update({numBots1: parameters.NumBots1, numBots2: parameters.NumBots2})
    numBots1.delete(0, tkinter.END)
    numBots1.insert(0, 2)
    randBots1.bind('<Button>', lambda event: RandValue(numBots1, 1, 99))
    randBots2.bind('<Button>', lambda event: RandValue(numBots2, 1, 99))

    tkinter.Label(win, text="Биом 3:").grid(row=11, column=0, sticky='W', padx=10, pady=10)
    numBots3 = tkinter.Spinbox(win, width=7, from_=1, to=99)
    VidgAccord.update({numBots3: parameters.NumBots3})
    numBots3.grid(row=11, column=1, padx=10)
    randBots3 = tkinter.Button(win, text="rand", width=4)
    randBots3.grid(row=11, column=2, sticky='W')
    randBots3.bind('<Button>', lambda event: RandValue(numBots3, 1, 99))

    buttonSave = tkinter.Button(win, text="Сохранить")
    buttonSave.grid(row=15, column=2)
    buttonSave.bind('<Button>', lambda event: SaveParameters(parameters))

    buttonRandAll = tkinter.Button(win, text="Рандом")
    buttonRandAll.grid(row=15, column=1)
    buttonRandAll.bind('<Button>', FullRandom)

    buttonInfo = tkinter.Button(win, text="Информация про параметры")
    buttonInfo.grid(row=15, column=3)
    buttonInfo.bind('<Button>', lambda event: InfoParameters())

    buttonLittle = tkinter.Button(win, text="Маленький")
    buttonLittle.grid(row=13, column=1)
    buttonLittle.bind('<Button>', lambda event: parameters.set_world_size("little"))

    buttonLittle = tkinter.Button(win, text="Средний")
    buttonLittle.grid(row=13, column=2)
    buttonLittle.bind('<Button>', lambda event: parameters.set_world_size("medium"))

    buttonLittle = tkinter.Button(win, text="Большой")
    buttonLittle.grid(row=13, column=3)
    buttonLittle.bind('<Button>', lambda event: parameters.set_world_size("large"))

    tkinter.Label(win, text="Выберите размер поля").grid(row=12, column=2, sticky='W', columnspan=2)
    tkinter.Label(win, text="").grid(row=14, column=2, sticky='W', columnspan=2)

    OldVariables(VidgAccord)




def StartMenu(wPar):
    global WINDOWS
    mainWindow = tkinter.Tk()
    WINDOWS.append(mainWindow)

    mainWindow.configure(background='black')
    mainWindow.title('LifeHub')
    mainWindow.protocol("WM_DELETE_WINDOW", lambda: (_ for _ in ()).throw(SystemExit(0)))

    w = mainWindow.winfo_screenwidth()
    h = mainWindow.winfo_screenheight()
    mainWindow.geometry(f'{w // 2}x{h // 2}+{w // 2 - w // 4}+{h // 2 - h // 4}')
    mainWindow.columnconfigure(1, weight = 1)
    mainWindow.columnconfigure(3, weight = 1)
    mainWindow.rowconfigure(1, weight = 1)
    mainWindow.rowconfigure(5, weight = 1)


    startBtn = tkinter.Button(mainWindow, text = 'Начать симуляцию', font = 'Arial 24', bd = 5, width = 25, bg = "#FFA500", activebackground = "#FFA500")
    startBtn.grid(row = 2, column = 2, padx = 20, pady = 20)
    startBtn.bind('<Button>', lambda event: CloseAllWindow())

    paramBtn = tkinter.Button(mainWindow, text = 'Задать параметры вселенной', font = 'Arial 24', bd = 5, width = 25, bg = "#FFA500", activebackground = "#FFA500")
    paramBtn.grid(row = 3, column = 2, padx = 20, pady = 20)
    paramBtn.bind('<Button>', lambda event: ParamWindow(wPar))

#    btn = tkinter.Button(mainWindow, text = 'Начать симуляцию', font = 'Arial 24', bd = 5, width = 25)
#    btn.grid(row = 4, column = 2, padx = 20, pady = 20)

    mainWindow.mainloop()
