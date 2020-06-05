import random
import src.dna as dna

class Bot:
    Biom_bot_color = {1 : (25, 23, 163), 2 : (176, 163, 42), 3 : (173, 50, 58)}

    def __init__(self, biom):
        self.Dna = dna.Dna(biom)
        self.set_color()
        self.TimeSpeed = 11 - self.Dna.get("speed") # amount of ticks for one move

    def set_color(self):
        self.Color = self.Biom_bot_color[self.Dna.Biom]

        








