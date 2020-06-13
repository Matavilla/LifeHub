import tkinter
from tkinter import messagebox
from random import randint

COUNT = 0
WINDOWS = list()


class WorldParameters:
    """ Основной класс описывающий параметры мира содержащий глобальный словарь Scale

    :param Scale: Словарь соотносящий название с коэффицентом отношения """


    Scale = {'little': 4, 'medium': 2, 'large': 1}
    # Scale.__doc__ = "Словарь соотносящий название с коэффицентом отношения"

    def __init__(self):

        self.update()
        self.set_world_size('little')

    def update(self, tick=0, chaos=0, food=0,
               t_1=0, t_2=0, t_3=0, numB1=0, numB2=0, numB3=0):
        """ Обновление информации о составляющих мира

        :param tick: Тик вселенной
        :type tick: int
        :param chaos: Момент хаоса
        :type chaos: int
        :param food: Количество еды
        :type food: int
        :param t_1: Период генирации еды в первом биоме
        :type t_1: int
        :param t_2: Период генерации еды во втором биоме
        :type t_2: int
        :param t_3: Период генерации еды в третьем биоме
        :type t_3: int
        :param numB1: Начальное количество клеток в первом биоме
        :type numB1: int
        :param numB2: Начальное количество клеток во втором биоме
        :type numB2: int
        :param numB3: Начальное количество клеток в третьем биоме
        :type numB3: int
        :rtype: None
        :return: Обновляет информацию о мире
        """
        self.TickUniverse = int(tick)
        self.ChaosMoment = int(chaos)
        self.AmountOfFood = int(food)

        # generation period of food and poison
        self.T_1 = int(t_1)
        self.T_2 = int(t_2)
        self.T_3 = int(t_3)

        # start number of bots in each bioms
        self.NumBots1 = int(numB1)
        self.NumBots2 = int(numB2)
        self.NumBots3 = int(numB3)

    def set_world_size(self, mode):
        """ Устанавливает размер игровой карты в зависимости от параметра

        :param mode: Переменная характризующая размер
        :return: Сохрнаяет размер карты внутри класса
        """
        MAX_WORLD_SIZE = 400
        self.WorldSize = MAX_WORLD_SIZE // self.Scale[mode]

    def __bool__(self):
        """Проверка валидности введённых параметров

        :rtype: True/False
        :return: Возвращает информацию о том, верно ли были введены параметры
        """
        print("[LOG] Проверка параметров")
        if not 0 < self.TickUniverse < 1000:
            return False
        if not 0 < self.ChaosMoment < 1000:
            return False
        if not 0 < self.AmountOfFood < 1000:
            return False
        if not 0 < self.T_1 < 10:
            return False
        if not 0 < self.T_2 < 10:
            return False
        if not 0 < self.T_3 < 10:
            return False
        if not 20 < self.NumBots1 < 150:
            return False
        if not 20 < self.NumBots2 < 150:
            return False
        if not 20 < self.NumBots3 < 150:
            return False
        print("[LOG] OK")
        return True

    def print_in_log(self):
        """Функция для отладки

        :return: Возврашает в поток вывода всю информацию класса
        """
        print(f'TickOfUniverse = {self.TickUniverse}')
        print(f'ChaosMoment = {self.ChaosMoment}')
        print(f'AmountOfFood = {self.AmountOfFood}')
        print(f'T_1 = {self.T_1}')
        print(f'T_2 = {self.T_2}')
        print(f'T_3 = {self.T_3}')
        print(f'NumBots1 = {self.NumBots1}')
        print(f'NumBots2 = {self.NumBots2}')
        print(f'NumBots3 = {self.NumBots3}')
        print(f'WorldSize = {self.WorldSize}')
        print('\n')


def InfoParameters(win):
    """ Информация о параметрах меню настроек

    :param win: Окно tkinter
    :type win: <class 'tkinter.Tk'>
    :return: None
    """
    print(type(win))
    window = tkinter.Toplevel(win)
    window.title('Информация')
    MsgTik = "Тик вселенной - как быстро происходит действия в игровом мире."
    tkinter.Label(window, text =MsgTik).grid(row=0, column=0, sticky='W',
                                        padx=10, pady=10)
    MsgMeal = "Количество еды - общее количество еды в соответствующем биоме."
    tkinter.Label(window, text=MsgMeal).grid(row=1, column=0, sticky='W',
                                        padx=10, pady=10)

    MsgChaos = "Момент хаоса - момент времени в который боты смогут покинуть свой биом."
    tkinter.Label(window, text=MsgChaos).grid(row=2, column=0, sticky='W',
                                             padx=10, pady=10)

    MsgGen = "Период генерации еды - как часто в каждом из биомов генерируется еда."
    tkinter.Label(window, text=MsgGen).grid(row=3, column=0, sticky='W',
                                             padx=10, pady=10)

    МsgStart = "Начальное количество ботов - сколько ботов находится в начальный момент " \
                                                            "в каждом из биомов."
    tkinter.Label(window, text=МsgStart).grid(row=4, column=0, sticky='W',
                                             padx=10, pady=10)

    MsgScreen = "Размер поля - общий размер игрового поля."
    tkinter.Label(window, text=MsgScreen).grid(row=5, column=0, sticky='W',
                                             padx=10, pady=10)

    EndButton = tkinter.Button(window, text="Ясно", width=4)
    EndButton.grid(row=6, sticky='WE',padx=10, pady=10)
    EndButton.bind('<Button>', lambda event: window.destroy())



def CloseWindow(win):
    """Закрытие указанного окна

    :param win: Окно tkinter
    :type win: <class 'tkinter.Tk'>
    :rtype: None
    :return: Закрывает указанное существующее окно
    """
    global COUNT
    COUNT = 0
    win.destroy()


def CloseAllWindow():
    """ Закрытие всех существующих окон

    :rtype: None
    :return: Закрывает все окна
    """
    global WINDOWS
    for i in WINDOWS:
        CloseWindow(i)


def GenField(win, _text, borders, interval=(1,999)):
    """ Вспомогательная функция, создает окно с параметрами, scrollbox и кнопку random

    :param win: Окно tkinter
    :type win: <class 'tkinter.Tk'>
    :param _text: Текст сообщения
    :type _text: str
    :param borders: Кортеж данных, характеризующий (raw,column) для grid
    :type borders: tuple
    :param interval: Интервал чисел в котором кнопка random генерирует числа
    :type interval: tuple
    :rtype: None
    :return: Добавляет в окно win дополнительное поле
    """
    line,col = borders
    tkinter.Label(win, text=_text).grid(row=line, column=col, sticky='W',
                                         padx=10, pady=10)
    winParam = tkinter.Spinbox(win, width=7, from_=interval[0], to=interval[1])
    winParam.grid(row=line, column=col+1, padx=10, pady=10)
    randButton = tkinter.Button(win, text="Рандом", width=5)
    randButton.grid(row=line, column=col+2, sticky='W',
                                         padx=10, pady=10)
    randButton.bind('<Button>', lambda event: RandValue(winParam, interval[0], interval[1]))

    return winParam

def RandValue(vidget, _from, to):
    """ Задаёт реакцию на нажатие кнопки random

    :param vidget: виджет
    :param _from: начало интервала для генерации случайного числа
    :type _from: int
    :param to: конец интервала для генерации случайных чисел
    :rtype to: int
    :return: Меняет значение в поле виджета на случайное сгенерированное число из интервала
    """
    print(type(vidget))
    vidget.delete(0, tkinter.END)
    vidget.insert(0, randint(_from, to))


def OldVariables(allvid) -> None:
    """ При открытие окна показывает сохраненные параметры при предыдущей генерации

    :param allvid: Словарь значений всех переменных класса
    :type allvid: dict
    :rtype: None
    :return: Возвращает старые параметры генерации
    """

    for vidget in allvid:
        vidget.delete(0, tkinter.END)
        vidget.insert(0, allvid[vidget])


def ParamWindow(parameters):
    """ Создание окна с параметрами вселенной и сохранение параметров

    :param parameters: параметры вселенной
    :return: Обновленные параметры вселенной
    """

    def SaveParameters(parameters):
        """ Сохранение параметров вселенной

        :param parameters: параметры вселенной
        :return: Сохраняет параметры
        """
        parameters.update(tick.get(),
                          chaos.get(),
                          food.get(),
                          biom1.get(),
                          biom2.get(),
                          biom3.get(),
                          numBots1.get(),
                          numBots2.get(),
                          numBots3.get())
        if not parameters:
            messagebox.showerror("Ошибка", "Неверное значение параметров")

    def FullRandom(*args, **kwargs):
        """ Делает параметры класса случайными величинами

        :return: Задаёт все параметрами случайными в допустимых интервалах
        """
        RandValue(tick, 1, 999)
        RandValue(chaos, 1, 99)
        RandValue(food, 1, 999)

        RandValue(biom1, 1, 9)
        RandValue(biom2, 1, 9)
        RandValue(biom3, 1, 9)

        RandValue(numBots1, 21, 149)
        RandValue(numBots2, 21, 149)
        RandValue(numBots3, 21, 149)

        SaveParameters(parameters)

    def MakeWindowResizable(window, columns, lines):
        """ Добавляет окну возможность растягиваться

        :param win: Окно tkinter
        :type win: <class 'tkinter.Tk'>
        :param columns: Количество grid-колонок в окне
        :param lines: Количество grid-линий в окне
        :return: Делает окно растягиваемым
        """
        for i in range(columns):
            window.grid_columnconfigure(i, weight=1)
        for i in range(lines):
            window.grid_rowconfigure(i, weight=1)




    global COUNT, WINDOWS
    COUNT += 1
    if COUNT > 1:
        COUNT -= 1
        return

    win = tkinter.Tk()
    MakeWindowResizable(win, 7, 10)
    WINDOWS.append(win)

    win.title('Окно параметров')
    win.protocol("WM_DELETE_WINDOW", lambda: CloseWindow(win))

    VidgAccord = dict()

    tick = GenField(win, "Tик вселенной:", (0,0))
    VidgAccord.update({tick:parameters.TickUniverse})

    chaos = GenField(win, "Момент хаоса:", (0,4))
    VidgAccord.update({chaos: parameters.ChaosMoment})

    food = GenField(win, "Кол-во еды:", (1,0))
    VidgAccord.update({food: parameters.AmountOfFood})


    tkinter.Label(win, text="Период генерации еды в каждом из биомов:").grid(row=2,
                                                           sticky='WE',
                                                           padx=10,
                                                           pady=10,
                                                           columnspan=7)

    biom1 = GenField(win, "Биом 1:", (3,0), (1,9))
    VidgAccord.update({biom1: parameters.T_1})

    biom2 = GenField(win, "Биом 2:", (3,4), (1,9))
    VidgAccord.update({biom2:parameters.T_2})

    biom3 = GenField(win, "Биом 3:", (4,0),(1,9))
    VidgAccord.update({biom3: parameters.T_3})



    tkinter.Label(win, text="Начальное кол-во ботов:").grid(row=5,
                                                           sticky='WE',
                                                           padx=10,
                                                           pady=10,
                                                           columnspan=7)

    numBots1 = GenField(win, "Биом 1:", (6,0),(21,149))
    VidgAccord.update({numBots1: parameters.NumBots1})

    numBots2 = GenField(win, "Биом 2:", (6,4),(21,149))
    VidgAccord.update({numBots2: parameters.NumBots2})

    numBots3 = GenField(win, "Биом 3:", (7,0),(21,149))
    VidgAccord.update({numBots3: parameters.NumBots3})

    tkinter.Label(win, text="Выберите размер поля:").grid(row=8,
                                                           sticky='WE',
                                                           padx=30,
                                                           pady=30,
                                                           columnspan=7)

    buttonLittle = tkinter.Button(win, text="Маленький", height=1, width=10)
    buttonLittle.grid(row=9, column=1)
    buttonLittle.bind('<Button>',
                      lambda event: parameters.set_world_size("little"))

    buttonLittle = tkinter.Button(win, text="Средний", height=1, width=10)
    buttonLittle.grid(row=9, column=3)
    buttonLittle.bind('<Button>',
                      lambda event: parameters.set_world_size("medium"))

    buttonLittle = tkinter.Button(win, text="Большой", height=1, width=10)
    buttonLittle.grid(row=9, column=5)
    buttonLittle.bind('<Button>',
                      lambda event: parameters.set_world_size("large"))

    buttonSave = tkinter.Button(win, text="Сохранить", height=1, width=10, background="#555",foreground="#ccc")
    buttonSave.grid(row=10, column=3,padx=30, pady=30)
    buttonSave.bind('<Button>', lambda event: SaveParameters(parameters))

    buttonRandAll = tkinter.Button(win, text="На удачу!", height=1, width=10, background="#555",foreground="#ccc")
    buttonRandAll.grid(row=10, column=1, padx=30, pady=30)
    buttonRandAll.bind('<Button>', FullRandom)

    buttonInfo = tkinter.Button(win, text="Информация", height=1, width=10, background="#555",foreground="#ccc")
    buttonInfo.grid(row=10, column=5, padx=30, pady=30)
    buttonInfo.bind('<Button>', lambda event: InfoParameters(win))

    OldVariables(VidgAccord)


def StartReact(wPar):
    """ Реакция на нажатие кнопки StartGame

    :param wPar: Проверка валидности параметров
    :type wPar: bool
    :return: Закрывает окно и начинает игру или возвращает сообщение о ошибке
    """
    if (wPar):
        CloseAllWindow()
    else:
        messagebox.showerror("Ошибка", "Имеются ошибки в параметрах")


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
    startBtn.bind('<Button>', lambda event: StartReact(wPar))

    paramBtn = tkinter.Button(mainWindow,
                              text='Задать параметры вселенной',
                              font='Arial 24',
                              bd=5, width=25,
                              bg="#FFA500",
                              activebackground="#FFA500")

    paramBtn.grid(row=3, column=2, padx=20, pady=20)
    paramBtn.bind('<Button>', lambda event: ParamWindow(wPar))

    mainWindow.mainloop()
