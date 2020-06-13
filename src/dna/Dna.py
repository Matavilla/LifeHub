import random
import array


class Dna:
    """ Класс генотипа параметров ботов.
    """
    def __init__(self, biom=1):
        self.Biom = biom
        self.Gens = array.array('B')
        self.Index = dict()
        if biom == 1:
            self.set_value("speed", random.randint(0, 103))
            self.set_value("sensity", random.randint(25, 76))
            self.set_value("power", random.randint(120, 150))
            self.set_value("agression", random.randint(127, 153))
            self.set_value("armor", random.randint(127, 178))
            self.set_value("weather_resistance_1", 255)
            self.set_value("weather_resistance_2", 127)
            self.set_value("weather_resistance_3", 0)
            self.set_value("poison_vulnerability", random.randint(127, 178))
        elif biom == 2:
            self.set_value("speed", random.randint(52, 155))
            self.set_value("sensity", random.randint(127, 153))
            self.set_value("power", random.randint(50, 70))
            self.set_value("agression", random.randint(63, 102))
            self.set_value("armor", random.randint(63, 102))
            self.set_value("weather_resistance_1", 127)
            self.set_value("weather_resistance_2", 255)
            self.set_value("weather_resistance_3", 127)
            self.set_value("poison_vulnerability", random.randint(63, 102))
        elif biom == 3:
            self.set_value("speed", random.randint(104, 255))
            self.set_value("sensity", random.randint(200, 255))
            self.set_value("power", random.randint(30, 50))
            self.set_value("agression", random.randint(12, 25))
            self.set_value("armor", random.randint(12, 38))
            self.set_value("weather_resistance_1", 0)
            self.set_value("weather_resistance_2", 127)
            self.set_value("weather_resistance_3", 255)
            self.set_value("poison_vulnerability", random.randint(12, 38))

    def set_value(self, name, value):
        self.Gens.append(value)
        self.Index[name] = len(self.Gens) - 1

    def get(self, name):
        return self.Gens[self.Index[name]]

    def print_info(self):
        print("Biom = " + str(self.Biom))
        print("Gens Dna: ")
        print("\tspeed = " + str(self.get("speed")))
        print("\tsensity = " + str(self.get("sensity")))
        print("\tpower = " + str(self.get("power")))
        print("\tagression = " + str(self.get("agression")))
        print("\tarmor = " + str(self.get("armor")))
        s = "\tweather_resistance_1 = " + str(self.get("weather_resistance_1"))
        print(s)
        s = "\tweather_resistance_2 = " + str(self.get("weather_resistance_2"))
        print(s)
        s = "\tweather_resistance_3 = " + str(self.get("weather_resistance_3"))
        print(s)
        s = "\tpoison_vulnerability = " + str(self.get("poison_vulnerability"))
        print(s)
