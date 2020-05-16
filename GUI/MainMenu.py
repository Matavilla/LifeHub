import tkinter
import pygame
from tkinter import messagebox
from random import randint

count = 0

class WorldParameters:
    '''Сохранение параметров вселенной'''
    def __init__(self):
        self.update()
        #Game screen size
        pygame.init()
        self.ScreenWidth = pygame.display.Info().current_w
        self.ScreenHeight = pygame.display.Info().current_h

    def update(self, Tick = 1, chaos = 1,  food = 1, poison = 1,
               b1 = 1, b2 = 1, b3 = 1, numB1 = 1, numB2 = 1, numB3 = 1):
        self.TickUniverse = float(Tick)
        self.ChaosMoment = int(chaos)
        self.AmountOfFood = int(food)
        self.AmountOfPoison = int(poison)
        #generation period of food and poison
        self.Biom1 = int(b1)
        self.Biom2 = int(b2)
        self.Biom3 = int(b3)

        #start number of bots in each bioms
        self.NumBots1 = int(numB1)
        self.NumBots2 = int(numB2)
        self.NumBots3 = int(numB3)


    def check(self):
        print("[LOG] Проверка параметров")
        if not 0 < self.TickUniverse < 1000:
            return False
        if not 0 < self.ChaosMoment < 1000:
            return False
        if not 0 < self.AmountOfFood < 1000:
            return False
        if not 0 < self.AmountOfPoison < 1000:
            return False
        if not 0 < self.Biom1 < 1000:
            return False
        if not 0 < self.Biom2 < 1000:
            return False
        if not 0 < self.Biom3 < 1000:
            return False
        if not 0 < self.NumBots1 < 100:
            return False
        if not 0 < self.NumBots2 < 100:
            return False
        if not 0 < self.NumBots3 < 100:
            return False
        print("[LOG] OK")
        return True


def InfoParameters():
    messagebox.showinfo("Information", "BLA BLA BLA")




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
        vidget.delete(0,tkinter.END)
        vidget.insert(0,allvid[vidget])



def ParamWindow(parameters,window):
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
        if not parameters.check():
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

    def ScreenChange(screen,parameters, mode):
        pygame.init()
        width, height = pygame.display.Info().current_w, pygame.display.Info().current_h;
        # Modes={'little':4,"middle":3,"large":2}
        # screen.geometry("{}x{}".format(width//Modes[mode],height//Modes[mode]))
        Modes = {'little': (800, 600), 'medium': (1366, 768), 'large': (1600, 900)}
        screen.geometry("{}x{}".format(Modes[mode][0],Modes[mode][1]))
        parameters.ScreenWidth=Modes[mode][0]
        parameters.ScreenHeight=Modes[mode][1]



    def close(win):
        global count
        count = 0
        win.destroy()

    global count
    count += 1
    if count > 1:
        count -= 1
        return

    win = tkinter.Tk()
    win.title('Parameters window')
    win.protocol("WM_DELETE_WINDOW", lambda: close(win))
    VidgAccord=dict() #This is the dictionary to match the name of the variable is a class field

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
    biom3 = tkinter.Spinbox(win, width=7, from_=1, to=99,textvariable=4)
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

    buttonSave = tkinter.Button(win, text="Информация про параметры")
    buttonSave.grid(row=15, column=3)
    buttonSave.bind('<Button>', lambda event: InfoParameters())

    buttonLittle = tkinter.Button(win, text="Маленький")
    buttonLittle.grid(row=13, column=1)
    buttonLittle.bind('<Button>', lambda event: ScreenChange(window,parameters,"little"))

    buttonLittle = tkinter.Button(win, text="Средний")
    buttonLittle.grid(row=13, column=2)
    buttonLittle.bind('<Button>', lambda event: ScreenChange(window,parameters,"medium"))

    buttonLittle = tkinter.Button(win, text="Большой")
    buttonLittle.grid(row=13, column=3)
    buttonLittle.bind('<Button>', lambda event: ScreenChange(window,parameters,"large"))

    tkinter.Label(win, text="Выберите размер экрана").grid(row=12, column=2, sticky='W', columnspan=2)
    tkinter.Label(win, text="").grid(row=14, column=2, sticky='W', columnspan=2)

    OldVariables(VidgAccord)


def PrintParam(parameters):
    ''' Вывести все параметры на экран (для проверки) '''
    print(f'TickOfUniverse = {parameters.TickUniverse}')
    print(f'chaosMoment = {parameters.ChaosMoment}')
    print(f'amountOfFood = {parameters.AmountOfFood}')
    print(f'amountOfPoison = {parameters.AmountOfPoison}')
    print(f'biom1 = {parameters.Biom1}')
    print(f'biom2 = {parameters.Biom2}')
    print(f'biom3 = {parameters.Biom3}')
    print(f'NumBots1 = {parameters.NumBots1}')
    print(f'NumBots2 = {parameters.NumBots2}')
    print(f'NumBots3 = {parameters.NumBots3}')
    print('\n')


def StartMenu(wPar):
    count = 0
    mainWindow = tkinter.Tk()
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
    startBtn.bind('<Button>', lambda event: mainWindow.destroy())

    paramBtn = tkinter.Button(mainWindow, text = 'Задать параметры вселенной', font = 'Arial 24', bd = 5, width = 25, bg = "#FFA500", activebackground = "#FFA500")
    paramBtn.grid(row = 3, column = 2, padx = 20, pady = 20)
    paramBtn.bind('<Button>', lambda event: ParamWindow(wPar,mainWindow))

#    btn = tkinter.Button(mainWindow, text = 'Начать симуляцию', font = 'Arial 24', bd = 5, width = 25)
#    btn.grid(row = 4, column = 2, padx = 20, pady = 20)

    mainWindow.mainloop()
