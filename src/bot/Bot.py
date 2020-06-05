import random
import src.dna as dna

class Bot:
    Biom_bot_bound = {1 : (0, 20), 2 : (20, 40), 3 : (40, 60)}

    def __init__(self, biom):
        self.Bot_value = random.randint(*self.Biom_bot_bound[biom])
        self.set_color()
        self.WasChecked = False
        self.Dna = dna.Dna(biom)
        self.TimeSpeed = 11 - self.Dna.get("speed") # amount of ticks for one move

    def set_color(self):
        self.Color = ((self.Bot_value * 3) % 256, (self.Bot_value * 4) % 256, 100)

        








