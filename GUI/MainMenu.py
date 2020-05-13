import tkinter
from random import randint

count = 0

class WorldParameters:
    '''Сохранение параметров вселенной'''
    def __init__(self):
        self.update()

    def update(self, tik = 0, chaos = 0,  food = 0, poison = 0, 
               b1 = 0, b2 = 0, b3 = 0, numB1 = 0, numB2 = 0, numB3 = 0):
        self.TikUniverse = float(tik)
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
        print("Проверка параметров")
        return True






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



def RandValue(vidget, _from, to):
        vidget.delete(0, tkinter.END)
        vidget.insert(0, randint(_from, to))




def ParamWindow(parameters):
    '''Создание окна с параметрами вселенной и сохранение параметров'''
    def SaveParameters(parameters):
        '''Сохранить параметры'''
        parameters.update(tik.get(), 
                        chaos.get(),
                        food.get(), 
                        poison.get(), 
                        biom1.get(), 
                        biom2.get(), 
                        biom3.get(),
                        numBots1.get(),
                        numBots2.get(),
                        numBots3.get())

    def FullRandom(*args, **kwargs):
        '''установка рандомных параметров в заданных
           интервалах'''
        RandValue(tik, 0, 1000)
        RandValue(chaos, 0, 1000)
        RandValue(food, 0, 1000)
        RandValue(poison, 0, 1000)
        RandValue(biom1, 0, 1000)
        RandValue(biom2, 0, 1000)
        RandValue(biom3, 0, 1000)
        RandValue(numBots1, 0, 100)
        RandValue(numBots2, 0, 100)
        RandValue(numBots3, 0, 100)

    global count
    count+=1
    if count > 1:
        count-=1
        return

    win = tkinter.Tk()
    win.title('Parameters window')

    tik, chaos, randTik, randChaos = AddStrOfTable(win, "Тик вселенной", "Момент хаоса", 0, 0, 1000)
    food, poison, randFood, randPoison = AddStrOfTable(win, "Кол-во еды", "Кол-во яда:", 2, 0, 1000)

    randTik.bind('<Button>', lambda event: RandValue(tik, 0, 1000))
    randChaos.bind('<Button>', lambda event: RandValue(chaos, 0, 1000))
    randFood.bind('<Button>', lambda event: RandValue(food, 0, 1000))
    randPoison.bind('<Button>', lambda event: RandValue(poison, 0, 1000))

    tkinter.Label(win, text="Период генерации еды/яда").grid(row=4, column=1, sticky='W', columnspan=2)

    biom1, biom2, randBiom1, randBiom2 = AddStrOfTable(win, "Биом 1:", "Биом 2:", 5)
    randBiom1.bind('<Button>', lambda event: RandValue(biom1, 0, 1000))
    randBiom2.bind('<Button>', lambda event: RandValue(biom2, 0, 1000))

    tkinter.Label(win, text="Биом 3:").grid(row=7, column=0, sticky='W', padx=10, pady=10)
    biom3 = tkinter.Spinbox(win, width=7, from_=0, to=1000)
    biom3.grid(row=7, column=1, padx=10)
    randBiom3 = tkinter.Button(win, text="rand", width=4)
    randBiom3.grid(row=7, column=2, sticky='W')
    randBiom3.bind('<Button>', lambda event: RandValue(biom3, 0, 1000))

    tkinter.Label(win, text="Начальное кол-во ботов").grid(row=8, column=1, sticky='W', columnspan=2)

    numBots1, numBots2, randBots1, randBots2 = AddStrOfTable(win, "Биом 1:", "Биом 2:", 9, 0, 100)
    randBots1.bind('<Button>', lambda event: RandValue(numBots1, 0, 100))
    randBots2.bind('<Button>', lambda event: RandValue(numBots2, 0, 100))

    tkinter.Label(win, text="Биом 3:").grid(row=11, column=0, sticky='W', padx=10, pady=10)
    numBots3 = tkinter.Spinbox(win, width=7, from_=0, to=100)
    numBots3.grid(row=11, column=1, padx=10)
    randBots3 = tkinter.Button(win, text="rand", width=4)
    randBots3.grid(row=11, column=2, sticky='W')
    randBots3.bind('<Button>', lambda event: RandValue(numBots3, 0, 100))


    buttonSave = tkinter.Button(win, text="Сохнанить")
    buttonSave.grid(row=12, column=2)
    buttonSave.bind('<Button>', lambda event: SaveParameters(parameters))

    buttonRandAll = tkinter.Button(win, text="Рандом")
    buttonRandAll.grid(row=12, column=1)
    buttonRandAll.bind('<Button>', FullRandom)



def PrintParam(parameters):
    ''' Вывести все параметры на экран (для проверки) '''
    print(f'tikOfUniverse = {parameters.TikUniverse}')
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
    startBtn.bind('<Button>', lambda event: PrintParam(wPar))
    #startBtn.bind('<Button>', lambda event: mainWindow.quit())

    paramBtn = tkinter.Button(mainWindow, text = 'Задать параметры вселенной', font = 'Arial 24', bd = 5, width = 25, bg = "#FF8C00", activebackground = "#FF8C00")
    paramBtn.grid(row = 3, column = 2, padx = 20, pady = 20)
    paramBtn.bind('<Button>', lambda event: ParamWindow(wPar))

#    btn = tkinter.Button(mainWindow, text = 'Начать симуляцию', font = 'Arial 24', bd = 5, width = 25)
#    btn.grid(row = 4, column = 2, padx = 20, pady = 20)

    mainWindow.mainloop()
