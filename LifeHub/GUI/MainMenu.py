# -*- coding: utf-8 -*-

"""
Данный модуль отвечает за вывод стартового меню на экран, а также за ввод
всех необходимых параметров вселенной.
"""

import tkinter
from tkinter import messagebox
from random import randint

COUNT = 0
WINDOWS = list()


class WorldParameters:
    """ Класс, содержащий параметры вселенной.
    """
    def __init__(self):

        self.update()
        self.set_world_size('little')

    def update(self, tick=0, chaos=0, food=0,
               t_1=0, t_2=0, t_3=0, numB1=0, numB2=0, numB3=0):
        """
        :param tick: Число действий в 1 секунду (тик вселенной).
        :type tick: int
        :param chaos: Число периодов отбора.
        :type chaos: int
        :param food: Количество еды.
        :type food: int
        :param t_1: Период генерации еды в первом биоме.
        :type t_1: int
        :param t_2: Период генерации еды во втором биоме.
        :type t_2: int
        :param t_3: Период генерации еды в третьем биоме.
        :type t_3: int
        :param numB1: Число ботов в первом биоме.
        :type numB1: int
        :param numB2: Число ботов во втором биоме.
        :type numB2: int
        :param numB3: Число ботов в третьем биоме.
        :type numB3: int
        """
        self.TickUniverse = int(tick)
        self.ChaosMoment = int(chaos)
        self.AmountOfFood = int(food)

        self.T_1 = int(t_1)
        self.T_2 = int(t_2)
        self.T_3 = int(t_3)

        self.NumBots1 = int(numB1)
        self.NumBots2 = int(numB2)
        self.NumBots3 = int(numB3)

    def set_world_size(self, mode):
        """ Функция, которая устанавливает размер игрового поля.

        :param mode: Размер поля.
        """
        scale = {'little': 4, 'medium': 2, 'large': 1}
        MAX_WORLD_SIZE = 400
        self.WorldSize = MAX_WORLD_SIZE // scale[mode]

    def __bool__(self):
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
    """Функция создания окна с информацией по параметрам вселенной.

    :param win: Окно tkinter.
    :type win: <class 'tkinter.Tk'>
    """
    
    window = tkinter.Toplevel(win)
    
    for i in range(6):
        window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(0, weight=1)

    window.title(_("Информация"))
    
    MsgTik = _("Тик вселенной - число действий в 1 секунду.")
    tkinter.Label(window, text=MsgTik).grid(row=0, column=0, sticky='W',
                                            padx=10, pady=10)
    MsgMeal = _("Количество еды - начальное количество еды в каждом биоме.")
    tkinter.Label(window, text=MsgMeal).grid(row=1, column=0, sticky='W',
                                             padx=10, pady=10)

    MsgChaos = _("Число периодов отбора - количество периодов отбора.")
    tkinter.Label(window, text=MsgChaos).grid(row=2, column=0, sticky='W',
                                              padx=10, pady=10)

    MsgGen = _("Период генерации еды - время генерации еды в биомах.")
    tkinter.Label(window, text=MsgGen).grid(row=3, column=0, sticky='W',
                                            padx=10, pady=10)

    МsgStart = _("Начальное количество ботов - начальное число ботов.")
    tkinter.Label(window, text=МsgStart).grid(row=4, column=0, sticky='W',
                                              padx=10, pady=10)

    MsgScreen = _("Размер поля - размер игрового поля.")
    tkinter.Label(window, text=MsgScreen).grid(row=5, column=0, sticky='W',
                                               padx=10, pady=10)

    EndButton = tkinter.Button(window, text=_("Закрыть"), width=4)
    EndButton.grid(row=6, sticky='WE', padx=10, pady=10)
    EndButton.bind('<Button>', lambda event: window.destroy())


def CloseWindow(win, single):
    global COUNT
    global WINDOWS
    COUNT = 0
    
    if single:
        WINDOWS.remove(win)
    
    win.destroy()


def CloseAllWindow():
    """ Функция, закрывающая созданные окна.
    """
    global WINDOWS
    for i in WINDOWS:
        CloseWindow(i, False)

def GenField(win, _text, borders, interval=(1, 999)):
    """ Функция, создающая поле для ввода.

    :param win: Окно tkinter.
    :type win: <class 'tkinter.Tk'>
    :param _text: Текст сообщения.
    :type _text: str
    :param borders: Кортеж данных, характеризующий (raw, column) для grid.
    :type borders: tuple
    :param interval: Интервал генерации чисел.
    :type interval: tuple
    """
    line, col = borders
    tkinter.Label(win, text=_text).grid(row=line, column=col, sticky='W',
                                        padx=10, pady=10)
    winParam = tkinter.Spinbox(win, width=7, from_=interval[0], to=interval[1])
    winParam.grid(row=line, column=col+1, padx=10, pady=10)
    randButton = tkinter.Button(win, text=_("Случайное значение"), width=18)
    randButton.grid(row=line, column=col+2, sticky='W', padx=10, pady=10)
    randButton.bind('<Button>', lambda event: RandValue(winParam, interval[0],
                                                        interval[1]))

    return winParam


def RandValue(vidget, _from, to):
    """ Функция, меняющая значение в виджете на случайное
        сгенерированное число.

    :param vidget: Виджет.
    :param _from: Начало интервала для генерации случайного числа.
    :type _from: int
    :param to: Конец интервала для генерации случайного числа.
    """
    vidget.delete(0, tkinter.END)
    vidget.insert(0, randint(_from, to))


def OldVariables(allvid) -> None:
    """ Функция, которая задает начальные значения для каждого виджета.

    :param allvid: Словарь виджетов.
    :type allvid: dict
    """

    for vidget in allvid:
        vidget.delete(0, tkinter.END)
        vidget.insert(0, allvid[vidget])


def ParamWindow(parameters):
    """ Функция, которая создает окно для ввода параметров вселенной.

    :param parameters: Параметры вселенной.
    """

    def SaveParameters(parameters):
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
            messagebox.showerror(_("Ошибка"),
                                 _("Неверное значение параметров"))

    def FullRandom(*args, **kwargs):
        """ Функция, которая задает случайные параметры вселенной.
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
        """ Функция, делающая разметку окна.

        :param win: Окно tkinter.
        :type win: <class 'tkinter.Tk'>
        :param columns: Количество grid-колонок в окне.
        :param lines: Количество grid-линий в окне.
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

    win.title(_("Окно параметров"))
    win.protocol("WM_DELETE_WINDOW", lambda: CloseWindow(win, True))

    VidgAccord = dict()

    tick = GenField(win, _("Tик вселенной:"), (0, 0))
    VidgAccord.update({tick: parameters.TickUniverse})

    chaos = GenField(win, _("Число периодов отбора:"), (0, 4))
    VidgAccord.update({chaos: parameters.ChaosMoment})

    food = GenField(win, _("Кол-во еды:"), (1, 0))
    VidgAccord.update({food: parameters.AmountOfFood})

    txt = _("Период генерации еды в каждом из биомов:")
    tkinter.Label(win, text=txt).grid(row=2, sticky='WE', padx=10,
                                      pady=10, columnspan=7)

    biom1 = GenField(win, _("Биом 1:"), (3, 0), (1, 9))
    VidgAccord.update({biom1: parameters.T_1})

    biom2 = GenField(win, _("Биом 2:"), (3, 4), (1, 9))
    VidgAccord.update({biom2: parameters.T_2})

    biom3 = GenField(win, _("Биом 3:"), (4, 0), (1, 9))
    VidgAccord.update({biom3: parameters.T_3})

    tkinter.Label(win, text=_("Начальное кол-во ботов:")).grid(row=5,
                                                               sticky='WE',
                                                               padx=10,
                                                               pady=10,
                                                               columnspan=7)

    numBots1 = GenField(win, _("Биом 1:"), (6, 0), (21, 149))
    VidgAccord.update({numBots1: parameters.NumBots1})

    numBots2 = GenField(win, _("Биом 2:"), (6, 4), (21, 149))
    VidgAccord.update({numBots2: parameters.NumBots2})

    numBots3 = GenField(win, _("Биом 3:"), (7, 0), (21, 149))
    VidgAccord.update({numBots3: parameters.NumBots3})

    tkinter.Label(win, text=_("Выберите размер поля:")).grid(row=8,
                                                             sticky='WE',
                                                             padx=30,
                                                             pady=30,
                                                             columnspan=7)

    buttonLittle = tkinter.Button(win, text=_("Маленький"), height=1, width=10)
    buttonLittle.grid(row=9, column=1)
    buttonLittle.bind('<Button>',
                      lambda event: parameters.set_world_size("little"))

    buttonLittle = tkinter.Button(win, text=_("Средний"), height=1, width=10)
    buttonLittle.grid(row=9, column=3)
    buttonLittle.bind('<Button>',
                      lambda event: parameters.set_world_size("medium"))

    buttonLittle = tkinter.Button(win, text=_("Большой"), height=1, width=10)
    buttonLittle.grid(row=9, column=5)
    buttonLittle.bind('<Button>',
                      lambda event: parameters.set_world_size("large"))

    buttonSave = tkinter.Button(win, text=_("Сохранить"), height=1, width=10,
                                background="#555", foreground="#ccc")
    buttonSave.grid(row=10, column=3, padx=30, pady=30)
    buttonSave.bind('<Button>', lambda event: SaveParameters(parameters))

    buttonRandAll = tkinter.Button(win,
                                   text=_("На удачу!"),
                                   height=1, width=10,
                                   background="#555", foreground="#ccc")

    buttonRandAll.grid(row=10, column=1, padx=30, pady=30)
    buttonRandAll.bind('<Button>', FullRandom)

    buttonInfo = tkinter.Button(win, text=_("Информация"), height=1, width=10,
                                background="#555", foreground="#ccc")
    buttonInfo.grid(row=10, column=5, padx=30, pady=30)
    buttonInfo.bind('<Button>', lambda event: InfoParameters(win))

    OldVariables(VidgAccord)


def StartReact(wPar, win):
    if (wPar):
        CloseAllWindow()
    else:
        messagebox.showerror(_("Ошибка"), _("Имеются ошибки в параметрах"))

#def CloseMain(win):
#    if messagebox.askokcancel("Quit", "Do you want to quit?"):
#        win.destroy()TypeError: <lambda>() missing 1 required positional argument: 'event'


def StartMenu(wPar):
    """ Функция, создающая стартовое окно.

    :param wPar: Параметры вселенной.
    """
    global WINDOWS
    mainWindow = tkinter.Tk()
    WINDOWS.append(mainWindow)

    mainWindow.configure(background=_('black'))
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
                              text=_('Начать симуляцию'),
                              font='Arial 24',
                              bd=5, width=25,
                              bg="#FFA500",
                              activebackground="#FFA500")

    startBtn.grid(row=2, column=2, padx=20, pady=20)
    startBtn.bind('<Button>', lambda event: StartReact(wPar, mainWindow))

    paramBtn = tkinter.Button(mainWindow,
                              text=_('Задать параметры вселенной'),
                              font='Arial 24',
                              bd=5, width=25,
                              bg="#FFA500",
                              activebackground="#FFA500")

    paramBtn.grid(row=3, column=2, padx=20, pady=20)
    paramBtn.bind('<Button>', lambda event: ParamWindow(wPar))
    #mainWindow.protocol("WM_DELETE_WINDOW", lambda: CloseMain(mainWindow))
    mainWindow.mainloop()
