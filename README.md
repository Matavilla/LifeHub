# LifeHub

Описание игры:

Есть 3 биома (холодный, умеренный, теплый) и 3 вида организмов (клеток).
Изначально генерируется карта в виде клеточной структуры, на которой генерируется рандомное
количество организмов. Место генерации организма зависит от его вида и принадлежности вида к 
определенному биому (например на севере более агрессивные). 

Каждому виду организма и биому соответствует определенный цвет. 
Холодный биом находится на севере карты, умеренный - середина, теплый - юг. 

Перед началом игры, пользователь должен задать начальные параметры вселенной и организмов(ботов).
Если какой-то параметр не задан, то он выбирается случайным образом в допустимом диапазоне
(допустимый диапазон определяется пользователем для каждого биома отдельно).
Подробное описание параметров ниже.

Изначально организмы каждого вида не могут выходить за пределы своего биома, но в параметрах 
вселенной можно задать момент времени, в который им разрешено покидать свой биом.
Организмы могут взаимодействовать между собой (скрещивание, атака).
Одними из самых важных параметров организмов являются здоровье и энергия, которые они пополняют (теряют)
в зависимости от взаимодействия с едой (ядом) или другими организмами. Также энергия уменьшается
при движении организма.

Главная цель организма – выжить и размножиться. Для этого ему нужно собрать как можно больше энергии.

Размножение организмов происходит в зависимости от типа размножения. 
1. Деление - в определенный момент времени организм может разделиться на 2 части, если ему хватает энергии
   для этого. Параметры новых организмов определяются исходя из генетического алгоритма.
2. Классическое размножение - при встрече двух организмов одного вида, и при достаточном кол-ве энергии
   у обоих организмов, появляется новый организм, параметры которого также определяются генетическим 
   алгоритмом.


Описание параметров:

	Параметры вселенной: 

	1. Тик вселенной (за это время совершается одно действие).
	2. Количество еды и яда, и период генерации для каждого биома (место генерации в биоме - рандомное).
	3. Температура окружающей среды для каждого биома.
	4. Момент времени, в который организмы могут покинуть свой биом.


	Параметры ботов:

	1. Скорость - сколько клеток может пройти за 1 тик.
	2. Дальность видимости (чувствительность).
	3. Затраты энергии на 1 действие (атака, скрещивание, движение).
	4. Энергия (от 0 до 100). 
	   Если энергия меньше нуля, то отнимается 1 ед. здоровья и энергия восстанавливается до 100. 
	   Если энергия больше чем 100, то прибавляется 1 ед. здоровья и энергия также = 100.
	5. Здоровье ( >= 0). Если здорове = 0, то смерть организма.
	6. Приспособленность к климату - уменьшает отрицательное влияние биома на организм.
	7. Размер (влияет на потребление энергии за 1 тик, а также на атаку и защиту).
	8. Стойкость к урону (влияет на потребление энергии за 1 тик) - в процентном соотношении 
	   понижает атаку др. бота.
	9. Атака другого бота - наносит урон здоровью другого бота (если он его убил, то прибавка 
	   к здоровью и энергии).
	10. Агрессивность (от -1 до 1) - влияет на желание убегать/атаковать другого бота.
	11. Способ размножения при встрече 2 ботов одного вида (деление или классическое).
	12. Чувствительность к еде/яду - влияет на распознавание еды/яда.




Требования:


1. Разработать симулятор эволюции, в котором будет 3 вида биомов (холодный, умеренный, теплый)
   и 3 вида организмов (клеток).

2. Добавить несколько объектов для взаимодействия клеток с ними (еда, яд).

3. Должна быть возможность изменения условий обитания организмов.

4. Добавить различные виды взаимодействий между организмами (скрещивание, атака).

5. Реализовать генетический алгоритм для скрещивания и мутаций.

6. Разработать искусственный интеллект бота.


![Примерная схема проекта](https://github.com/Matavilla/LifeHub/blob/master/Схема%20проекта.bmp)


Инструкции:


Сборка колеса: 

> ninja wheel 

  или просто:

> ninja

(Колесо установится в папку dist текущего каталога. Колесо устанавливается 
через pip3 install <файл с колесом>)


Локали:

После установки пакета, для запуска на английской локали использовать:

> LANG=en_US.UTF-8 python3 -m LifeHub

Для запуска на польской локали:

> LANG=pl_PL.UTF-8 python3 -m LifeHub


Проверить все тесты:

> ninja test

(имеются тесты как для pytest, так и для doctest. В случае doctest проверяется
только 1 модуль LifeHub/src/Handler.py. Тесты для pytest лежат в папке tests)

Для отдельного запуска тестов pytest и doctest:

> ninja pytest

> ninja doctest


Проверить код стайл через flake8: 

> ninja codestyle


Сборка документации:

> ninja builddoc

(Исходники документации лежат в папке docs. Собранная документация будет
лежать в папке docs/_build. Соответственно саму документацию можно посмотреть
файле docs/_build/html/index.html)


Очистка генерата:

> ninja distclean


Игру также можно запустить с помощью скрипта в текущей директории:

> python3 run.py


