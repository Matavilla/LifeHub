from src.dna.Algo import GenAlgo
import random
import array

class Dna(GenAlgo):
    Value_names = ["life", "speed", "sensity", 
                   "size", "agression", "armor"] #names - speed...

    def __init__(self, biom):
        self.Biom = biom
        self.Gens = array.array('H')
        self.Index = dict()
#need to init value - may be use random + bounds
        if biom == 1:
            self.set_value("life", random.randint(90, 100))
            self.set_value("speed", random.randint(1, 4))
            self.set_value("sensity", random.randint(5, 7))
            self.set_value("agression", random.randint(50, 60))
            self.set_value("armor", random.randint(50, 60))
        elif biom == 2:
            self.set_value("life", random.randint(80, 90))
            self.set_value("speed", random.randint(4, 8))
            self.set_value("sensity", random.randint(3, 5))
            self.set_value("agression", random.randint(25, 40))
            self.set_value("armor", random.randint(30, 40))
        elif biom == 3:
            self.set_value("life", random.randint(70, 80))
            self.set_value("speed", random.randint(8, 10))
            self.set_value("sensity", random.randint(1, 3))
            self.set_value("agression", random.randint(5, 10))
            self.set_value("armor", random.randint(10, 15))

    def set_value(self, name, value):
        self.Gens.append(value)
        self.Index[name] = len(self.Gens) - 1

    def get(self, name):
        return self.Gens[self.Index[name]]
    

