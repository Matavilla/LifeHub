import tkinter
from random import randint

class WorldParameters:
    '''Сохранение параметров вселенной'''
    def __init__(self, tik = 0,    chaosMoment = 0,
                 amountOfFood = 0, amountOfPoison = 0,
                 biom1 = 0,     biom2 = 0,    biom3 = 0,
                 numBots1 = 0,  numBots2 = 0, numBots3 = 0):
        self.tikOfUniverse = float(tik)
        self.chaosMoment = int(chaosMoment)
        self.amountOfFood = int(amountOfFood)
        self.amountOfPoison = int(amountOfPoison)
        #generation period of food and poison
        self.biom1 = int(biom1)
        self.biom2 = int(biom2)
        self.biom3 = int(biom3)

        self.numBots1 = int(numBots1)
        self.numBots2 = int(numBots2)
        self.numBots3 = int(numBots3)


    def check(self):
        print("Проверка параметров")


parameters = WorldParameters()


# def randValue(_from, to, vidget):
#     vidget.delete(0, tkinter.END)
#     vidget.insert(0, randint(_from, to))

def AddStrOfTable(win, _text1, _text2, _row, _from = 0, _to = 100):
    ''' Вспомогательная функция добавления строки
        таблицы в окно с параметрами.
        -> 2 spin бокса и 2 кнопки'''
    tkinter.Label(win, text=_text1).grid(row=_row, column=0, sticky='W', padx=10, pady=10)
    winParam1 = tkinter.Spinbox(win, width=7, from_=_from, to=_to)
    winParam1.grid(row=_row, column=1, padx=10)
    randButton1 = tkinter.Button(win, text="rand", width=4)
    randButton1.grid(row=_row+1, column=1, sticky='N')
    tkinter.Label(win, text=_text2).grid(row=_row, column=2, sticky='E')
    winParam2 = tkinter.Spinbox(win, width=7, from_=_from, to=_to)
    winParam2.grid(row=_row, column=3, sticky='E', padx=10)
    randButton2 = tkinter.Button(win, text="rand", width=4)
    randButton2.grid(row=_row+1, column=3, sticky='N')
    return winParam1, winParam2, randButton1, randButton2



def randValue(vidget, _from, to):
        vidget.delete(0, tkinter.END)
        vidget.insert(0, randint(_from, to))



def ParamWindow(*args, **kwargs):
    '''Создание окна с параметрами вселенной и сохранение параметров'''
    def SaveParameters(*args, **kwargs):
        '''Сохранить параметры'''
        global parameters
        parameters.tikOfUniverse = float(tik.get())
        parameters.chaosMoment = int(chaos.get())
        parameters.amountOfFood = int(food.get())
        parameters.amountOfPoison = int(poison.get())
        parameters.biom1 = int(biom1.get())
        parameters.biom2 = int(biom2.get())
        parameters.biom3 = int(biom3.get())
        parameters.numBots1 = int(numBots1.get())
        parameters.numBots2 = int(numBots2.get())
        parameters.numBots3 = int(numBots3.get())

    def FullRandom(*args, **kwargs):
        randValue(tik, 0, 1000)
        randValue(chaos, 0, 1000)
        randValue(food, 0, 1000)
        randValue(poison, 0, 1000)
        randValue(biom1, 0, 1000)
        randValue(biom2, 0, 1000)
        randValue(biom3, 0, 1000)
        randValue(numBots1, 0, 100)
        randValue(numBots2, 0, 100)
        randValue(numBots3, 0, 100)


    win = tkinter.Tk()
    win.title('Parameters window')

    tik, chaos, randTik, randChaos = AddStrOfTable(win, "Тик вселенной", "Момент хаоса", 0, 0, 1000)
    food, poison, randFood, randPoison = AddStrOfTable(win, "Кол-во еды", "Кол-во яда:", 2, 0, 1000)

    randTik.bind('<Button>', lambda x: randValue(tik, 0, 1000))
    randChaos.bind('<Button>', lambda x: randValue(chaos, 0, 1000))
    randFood.bind('<Button>', lambda x: randValue(food, 0, 1000))
    randPoison.bind('<Button>', lambda x: randValue(poison, 0, 1000))

    tkinter.Label(win, text="Период генерации еды/яда").grid(row=4, column=1, sticky='W', columnspan=2)

    biom1, biom2, randBiom1, randBiom2 = AddStrOfTable(win, "Биом 1:", "Биом 2:", 5)
    randBiom1.bind('<Button>', lambda x: randValue(biom1, 0, 1000))
    randBiom2.bind('<Button>', lambda x: randValue(biom2, 0, 1000))

    tkinter.Label(win, text="Биом 3:").grid(row=7, column=0, sticky='W', padx=10, pady=10)

    biom3 = tkinter.Spinbox(win, width=7, from_=0, to=1000)
    biom3.grid(row=7, column=1, padx=10)
    randBiom3 = tkinter.Button(win, text="rand", width=4)
    randBiom3.grid(row=7, column=2, sticky='W')
    randBiom3.bind('<Button>', lambda x: randValue(biom3, 0, 1000))

    tkinter.Label(win, text="Начальное кол-во ботов").grid(row=8, column=1, sticky='W', columnspan=2)

    numBots1, numBots2, randBots1, randBots2 = AddStrOfTable(win, "Биом 1:", "Биом 2:", 9, 0, 100)
    randBots1.bind('<Button>', lambda x: randValue(numBots1, 0, 100))
    randBots2.bind('<Button>', lambda x: randValue(numBots2, 0, 100))

    tkinter.Label(win, text="Биом 3:").grid(row=11, column=0, sticky='W', padx=10, pady=10)
    numBots3 = tkinter.Spinbox(win, width=7, from_=0, to=100)
    numBots3.grid(row=11, column=1, padx=10)
    randBots3 = tkinter.Button(win, text="rand", width=4)
    randBots3.grid(row=11, column=2, sticky='W')
    randBots3.bind('<Button>', lambda x: randValue(numBots3, 0, 100))

    buttonSave = tkinter.Button(win, text="Сохнанить")
    buttonSave.grid(row=12, column=2)
    buttonSave.bind('<Button>', SaveParameters)

    buttonRandAll = tkinter.Button(win, text="Рандом")
    buttonRandAll.grid(row=12, column=1)
    buttonRandAll.bind('<Button>', FullRandom)



def PrintParam(*args, **kwargs):
    ''' Вывести все параметры на экран (для проверки) '''
    global parameters
    print(f'tikOfUniverse = {parameters.tikOfUniverse}')
    print(f'chaosMoment = {parameters.chaosMoment}')
    print(f'amountOfFood = {parameters.amountOfFood}')
    print(f'amountOfPoison = {parameters.amountOfPoison}')
    print(f'biom1 = {parameters.biom1}')
    print(f'biom2 = {parameters.biom2}')
    print(f'biom3 = {parameters.biom3}')
    print(f'numBots1 = {parameters.numBots1}')
    print(f'numBots2 = {parameters.numBots2}')
    print(f'numBots3 = {parameters.numBots3}')
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
    ParamBtn.bind('<Button>', ParamWindow)

    Btn = tkinter.Button(mainWindow, text = 'Начать симуляцию', font = 'Arial 24', bd = 5, width = 25)
    Btn.grid(row = 4, column = 2, padx = 20, pady = 20)

    startBtn.bind('<Button>', PrintParam)

    mainWindow.mainloop()
