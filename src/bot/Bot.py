import random
import array
import src.dna as dna
from src.dna.Algo import GenAlgo


class Bot:
    Biom_bot_color = {1 : (25, 23, 163), 
                      2 : (176, 163, 42), 
                      3 : (173, 50, 58)}

    Bias_dir = [(-1, -1), (0, -1), (1, -1), (1, 0), 
                (1, 1),   (0, 1),  (-1, 1), (-1, 0)]

    def __init__(self, biom):
        self.Dna = dna.Dna(biom)
        self.Ai = AI()
        self.Curr_direction = 1
        self.Pointer_of_ai = 0
        self.Life = 300
        self.set_color()
        # amount of ticks for one move
        self.TimeSpeed = 6 - self.Dna.get("speed")

    def set_color(self):
        self.Color = self.Biom_bot_color[self.Dna.Biom]

    def get_dir_and_action(self):
        """ 0..7 - move
            8..15 - attack
            16..23 - check
            24..31 - rotate
            32..63 - jump

        """
        curr_command = self.Ai.Gens[self.Pointer_of_ai]
        dx, dy, action = 0, 0, None
        count = 10
        while 24 <= curr_command <= 63 and count:
            if 24 <= curr_command <= 31:
                action = "rotate"
                self.Curr_direction = (curr_command + 
                                       self.Curr_direction -
                                       1) % 8
                self.Pointer_of_ai = (self.Pointer_of_ai + 1) % 64
            else:
                self.Pointer_of_ai = (self.Pointer_of_ai + curr_command) % 64
            curr_command = self.Ai.Gens[self.Pointer_of_ai]
            count -= 1

        if 0 <= curr_command <= 7:
            action = "move"
        elif 8 <= curr_command <= 15:
            action = "attack"
        elif 16 <= curr_command <= 23:
            action = "check"
        else:
            action = None
        dx, dy = self.Bias_dir[(curr_command + self.Curr_direction - 1) % 8]
        return dx, dy, action


class AI(GenAlgo):
    """ Bot artificial intelligence

    """
    def __init__(self):
        self.Gens = array.array('B')
        self.set_ai()
       
    def set_ai(self):
        for i in range(64):
            self.Gens.append(random.randint(0, 63))

