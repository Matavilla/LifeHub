import random
import array
from src.dna.Algo import GenAlgo

class Dna(GenAlgo):
    Value_names = ["speed", "sensity", "power", 
                   "agression", "armor", "weather_resistance",
                   "poison_vulnerability"] #names - speed...

    def __init__(self, biom):
        self.Biom = biom
        self.Gens = array.array('B')
        self.Index = dict()
#need to init value - may be use random + bounds
        if biom == 1:
            self.set_value("speed", random.randint(1, 2))
            self.set_value("sensity", 100)
            self.set_value("power", random.randint(50, 60))
            self.set_value("agression", random.randint(50, 60))
            self.set_value("armor", random.randint(50, 70))
            self.set_value("weather_resistance", random.randint(50, 70))
            self.set_value("poison_vulnerability", random.randint(50, 70))
        elif biom == 2:
            self.set_value("speed", random.randint(2, 3))
            self.set_value("sensity", random.randint(50, 60))
            self.set_value("power", random.randint(30, 40))
            self.set_value("agression", random.randint(25, 40))
            self.set_value("armor", random.randint(25, 40))
            self.set_value("weather_resistance", random.randint(25, 40))
            self.set_value("poison_vulnerability", random.randint(25, 40))
        elif biom == 3:
            self.set_value("speed", random.randint(4, 5))
            self.set_value("sensity", random.randint(10, 30))
            self.set_value("power", random.randint(20, 30))
            self.set_value("agression", random.randint(5, 10))
            self.set_value("armor", random.randint(5, 15))
            self.set_value("weather_resistance", random.randint(5, 15))
            self.set_value("poison_vulnerability", random.randint(5, 15))

    def set_value(self, name, value):
        self.Gens.append(value)
        self.Index[name] = len(self.Gens) - 1

    def get(self, name):
        return self.Gens[self.Index[name]]
    

