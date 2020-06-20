# LifeHub (python 3.7+)
___

## Оглавление
<a name="6"></a> 
1. [Описание программы](#1)
2. [Описание вселенной игры](#2)
3. [Описание параметров](#3)
4. [Схемы проекта](#4)
5. [Описание установки](#5)
___

## Описание программы
<a name="1"></a> 
Данная программа является симулятором эволюции живых организмов (см.подробное описание вселенной). Пользователь может регулировать параметры вселенной для получения различных вариантов эволюции существ. Каждое существо имеет два вида генотипов - генотип команд для ИИ существа и генотип параметров существа. Для скрещивания используются классические варианты кроссовера и мутаций.

Стрелки вверх и вниз соответсвенно позволяют увеличивать или уменьшать время тика внутри pygame.

[Оглавление](#6)
____

## Описание вселенной игры
<a name="2"></a> 
В игре представлено три биома(холодный, умеренный, теплый), в каждом из которых существует свой вид существ(имееют синий, белый, фиолетовый цвет). Каждому виду и биому соответствует свой определенный цвет. Холодный биом находится на севере карты, умеренный - по середине карты, а теплый - на юге карты.
Все виды существ отличаются друг от друга, и это отличие прявляется в различных свойствах видов(например, различный уровень агрессии у существ). Так же в каждом биоме существует свой вид еды для существ, которая может быть и ядовитой. Главная цель существа – выжить и размножиться. Для этого ему нужно собрать как можно больше "жизней".

[Оглавление](#6)
____

## Описание параметров
<a name="3"></a> 
### Параметры вселенной: 

1. Тик вселенной (за это время совершается одно действие).
2. Начальное количество еды и период генерации для каждого биома (место генерации в биоме - случайное).
3. Максимальное число существ для каждого биома.
4. Число периодов отбора для создания начальной популяции для кажого вида существ.

### Параметры существ:
1. Скорость - сколько тиков занимает одно действие существа.
2. Здоровье. Если здорове меньше нуля, то существо умирает.
3. Приспособленность к климату - уменьшает отрицательное влияние биома на существо.
4. Броня - определяет стойкость существа к атаке от другого существа.
5. Атака - наносит урон здоровью другого существа.
6. Агрессивность - влияет на желание атаковать другое свущество.
7. Чувствительность к еде/яду - влияет на распознавание еды/яда.

[Оглавление](#6)
____

## Схемы проекта
<a name="4"></a> 

Схема GUI:
![Примерная схема GUI проекта](https://github.com/Matavilla/LifeHub/blob/master/Схема%20GUI.bmp)

Схема архитектуры программы:
![Примерная архитектура проекта](https://github.com/Matavilla/LifeHub/blob/master/Схема%20проекта.bmp)

[Оглавление](#6)
____

## Описание установки
<a name="5"></a> 
### Сборка колеса
```
ninja wheel 
```
или просто:
```
ninja
```
 Колесо установится в папку dist текущего каталога. Колесо устанавливается через pip3 install <файл с колесом> .

### Выбор локализации
После установки пакета, для запуска на английской локализации можно использовать:
```
LANG=en_US.UTF-8 python3 -m LifeHub
```
Для запуска на польской локализации:
```
LANG=pl_PL.UTF-8 python3 -m LifeHub
```

### Запуск тестов, сборки документации и проверки CodeStyle
Проверить все тесты:
```
ninja test
```
Имеются тесты как для pytest, так и для doctest. В случае doctest проверяется только 1 модуль LifeHub/src/Handler.py. Тесты для pytest лежат в папке tests.

Для отдельного запуска тестов pytest и doctest:
```
ninja pytest

ninja doctest
```

Проверить код стайл через flake8: 
```
ninja codestyle
```

Сборка документации:
```
ninja builddoc
```
Исходники документации лежат в папке docs. Собранная документация будет лежать в папке docs/_build. Саму документацию можно посмотреть в  docs/_build/html/index.html.

Очистка генерата:
```
ninja distclean
```
**Требуется python версии не ниже 3.7. На остальных версиях работа не гарантируется.**

Игру также можно запустить с помощью скрипта в текущей директории:
```
python3 run.py
```
Или с перенаправлением вывода логов:
```
./run
```
[Оглавление](#6)
____
