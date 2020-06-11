import tkinter
from tkinter import messagebox
from random import randint

COUNT = 0
WINDOWS = list()


class WorldParameters:
    '''Параметры вселенной

    '''

    Scale = {'little': 4, 'medium': 2, 'large': 1}

    def __init__(self):
        self.update()
        self.set_world_size('little')

    def update(self, tick=0, chaos=0, food=0, poison=0,
               t_1=0, t_2=0, t_3=0, numB1=0, numB2=0, numB3=0):
        self.TickUniverse = int(tick)
        self.ChaosMoment = int(chaos)
        self.AmountOfFood = int(food)
        self.AmountOfPoison = int(poison)

        # generation period of food and poison
        self.T_1 = int(t_1)
        self.T_2 = int(t_2)
        self.T_3 = int(t_3)

        # start number of bots in each bioms
        self.NumBots1 = int(numB1)
        self.NumBots2 = int(numB2)
        self.NumBots3 = int(numB3)

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
        if not 0 < self.T_1 < 10:
            return False
        if not 0 < self.T_2 < 10:
            return False
        if not 0 < self.T_3 < 10:
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
        print(f'T_1 = {self.T_1}')
        print(f'T_2 = {self.T_2}')
        print(f'T_3 = {self.T_3}')
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


def GenField(win,_text, borders, interval = (1,99)):
    '''Вспомогательная функция, делает окно с параметрами'''
    line,col = borders
    tkinter.Label(win, text=_text).grid(row=line, column=col, sticky='W',
                                         padx=10, pady=10)
    winParam = tkinter.Spinbox(win, width=7, from_=interval[0], to=interval[1])
    winParam.grid(row=line, column=col+1, padx=10, pady=10)
    randButton = tkinter.Button(win, text="rand", width=4)
    randButton.grid(row=line, column=col+2, sticky='W',
                                         padx=10, pady=10)
    randButton.bind('<Button>', lambda event: RandValue(winParam, interval[0], interval[1]))

    return winParam

def RandValue(vidget, _from, to):
    vidget.delete(0, tkinter.END)
    vidget.insert(0, randint(_from, to))


def OldVariables(allvid: dict) -> None:
    for vidget in allvid:
        print(vidget)
        vidget.delete(0, tkinter.END)
        vidget.insert(0, allvid[vidget])


def ParamWindow(parameters):
    '''Создание окна с параметрами вселенной и сохранение параметров

    '''
    def SaveParameters(parameters):
        '''Сохранить параметры

        '''
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
        '''Установка рандомных параметров в заданных
        интервалах

        '''
        RandValue(tick, 1, 999)
        RandValue(chaos, 1, 999)
        RandValue(food, 1, 999)
        RandValue(poison, 1, 999)

        RandValue(biom1, 1, 9)
        RandValue(biom2, 1, 9)
        RandValue(biom3, 1, 9)

        RandValue(numBots1, 1, 99)
        RandValue(numBots2, 1, 99)
        RandValue(numBots3, 1, 99)

        SaveParameters(parameters)

    def MakeWindowResizable(window,columns, lines):
        '''Делает окно растягиваемым '''
        for i in range(columns):
            window.grid_columnconfigure(i,weight=1)
        for i in range(lines):
            window.grid_rowconfigure(i,weight=1)




    global COUNT, WINDOWS
    COUNT += 1
    if COUNT > 1:
        COUNT -= 1
        return

    win = tkinter.Tk()
    MakeWindowResizable(win,7,13)
    WINDOWS.append(win)

    win.title('Parameters window')
    win.protocol("WM_DELETE_WINDOW", lambda: CloseWindow(win))

    VidgAccord = dict()

    tick = GenField(win, "Tик вселенной" ,(0,0), (1,999))
    VidgAccord.update({tick:parameters.TickUniverse})

    chaos = GenField(win, "Момент хаоса" ,(0,4), (1,999))
    VidgAccord.update({chaos: parameters.ChaosMoment})

    food = GenField(win, "Кол-во еды", (2,0), (1,999))
    VidgAccord.update({food: parameters.AmountOfFood})

    poison = GenField(win, "Кол-во яда", (2,4), (1,999))
    VidgAccord.update({poison: parameters.AmountOfPoison})

    tkinter.Label(win, text="Период генерации еды/яда").grid(row=4,
                                                           sticky='WE',
                                                           padx=10,
                                                           pady=10,
                                                           columnspan=7)

    biom1 = GenField(win, "Биом 1:", (5,0), (1,999))
    VidgAccord.update({biom1: parameters.T_1})

    biom2 = GenField(win, "Биом 2", (5,4), (1,999))
    VidgAccord.update({biom2:parameters.T_2})

    biom3 = GenField(win, "Биом 3:", (7,0),(1,999))
    VidgAccord.update({biom3: parameters.T_3})


    tkinter.Label(win, text="Начальное кол-во ботов").grid(row=8,
                                                           sticky='WE',
                                                           padx=10,
                                                           pady=10,
                                                           columnspan=7)

    numBots1 = GenField(win, "Биом 1:", (9,0))
    VidgAccord.update({numBots1: parameters.NumBots1})

    numBots2 = GenField(win, "Биом 2:", (9,4))
    VidgAccord.update({numBots2: parameters.NumBots2})

    numBots3 = GenField(win, "Биом 3:", (11,0))
    VidgAccord.update({numBots3: parameters.NumBots3})


    buttonSave = tkinter.Button(win, text="Сохранить", height = 2, width = 10)
    buttonSave.grid(row=15, column=3)
    buttonSave.bind('<Button>', lambda event: SaveParameters(parameters))

    buttonRandAll = tkinter.Button(win, text="Рандом", height = 2, width = 10)
    buttonRandAll.grid(row=15, column=1)
    buttonRandAll.bind('<Button>', FullRandom)

    buttonInfo = tkinter.Button(win, text="Информация", height = 2, width = 10)
    buttonInfo.grid(row=15, column=5,padx = 10, pady = 10)
    buttonInfo.bind('<Button>', lambda event: InfoParameters())

    tkinter.Label(win, text="Выберите размер поля").grid(row=12,
                                                           sticky='WE',
                                                           padx=30,
                                                           pady=30,
                                                           columnspan=7)

    buttonLittle = tkinter.Button(win, text="Маленький", height = 1, width = 10)
    buttonLittle.grid(row=13, column=1)
    buttonLittle.bind('<Button>',
                      lambda event: parameters.set_world_size("little"))

    buttonLittle = tkinter.Button(win, text="Средний", height = 1, width = 10)
    buttonLittle.grid(row=13, column=3)
    buttonLittle.bind('<Button>',
                      lambda event: parameters.set_world_size("medium"))

    buttonLittle = tkinter.Button(win, text="Большой", height = 1, width = 10)
    buttonLittle.grid(row=13, column=5)
    buttonLittle.bind('<Button>',
                      lambda event: parameters.set_world_size("large"))


    tkinter.Label(win, text="").grid(row=14,
                                     column=2,
                                     sticky='W',
                                     columnspan=2)

    OldVariables(VidgAccord)


def StartMenu(wPar):
    global WINDOWS
    mainWindow = tkinter.Tk()
    WINDOWS.append(mainWindow)

    mainWindow.configure(background='black')
    mainWindow.title('LifeHub')
    mainWindow.protocol("WM_DELETE_WINDOW",
                        lambda: (_ for _ in ()).throw(SystemExit(0)))

    w = mainWindow.winfo_screenwidth()
    h = mainWindow.winfo_screenheight()

    geometry_str = f'{w // 2}x{h // 2}+{w // 2 - w // 4}+{h // 2 - h // 4}'
    mainWindow.geometry(geometry_str)
    mainWindow.columnconfigure(1, weight=1)
    mainWindow.columnconfigure(3, weight=1)
    mainWindow.rowconfigure(1, weight=1)
    mainWindow.rowconfigure(5, weight=1)

    startBtn = tkinter.Button(mainWindow,
                              text='Начать симуляцию',
                              font='Arial 24',
                              bd=5, width=25,
                              bg="#FFA500",
                              activebackground="#FFA500")

    startBtn.grid(row=2, column=2, padx=20, pady=20)
    startBtn.bind('<Button>', lambda event: CloseAllWindow())

    paramBtn = tkinter.Button(mainWindow,
                              text='Задать параметры вселенной',
                              font='Arial 24',
                              bd=5, width=25,
                              bg="#FFA500",
                              activebackground="#FFA500")

    paramBtn.grid(row=3, column=2, padx=20, pady=20)
    paramBtn.bind('<Button>', lambda event: ParamWindow(wPar))

    # btn = tkinter.Button(mainWindow,
    #                      text='Начать симуляцию',
    #                      font='Arial 24',
    #                      bd=5, width=25)
    # btn.grid(row=4, column=2, padx=20, pady=20)

    mainWindow.mainloop()
