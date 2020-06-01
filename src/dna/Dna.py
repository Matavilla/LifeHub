from src.dna.Algo import GenAlgo


class Dna(GenAlgo):
    value_names = [""] #names - speed...


    def __init__(self):
        self.gens = array.array('H')
        seld.index = dict()
#need to init value - may be use random + bounds
        for i in value_names:
            self.set_value(i, random.randint(0, 65535))
        

    def set_value(self, name, value):
        self.gens.append(value)
        self.index[name] = len(self.dna) - 1

    def get(self, name):
        return self.gens[self.index[name]]
    

