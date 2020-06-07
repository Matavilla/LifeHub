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
        self.Life = 255
        self.set_color()
        # amount of ticks for one move
        self.TimeSpeed = 5 - (self.Dna.get("speed") // 52)

    def set_color(self):
        self.Color = self.Biom_bot_color[self.Dna.Biom]

    def get_dir_and_action(self):
        """ 0..31 - move
            32..63 - attack
            64..95 - check
            96..127 - rotate
            128..255 - jump

        """
        curr_command = self.Ai.Gens[self.Pointer_of_ai]
        dx, dy, action = 0, 0, None
        max_num_of_actions = 10
        while 96 <= curr_command <= 255 and max_num_of_actions:
            if 96 <= curr_command <= 127:
                action = "rotate"
                self.Curr_direction = (curr_command + 
                                       self.Curr_direction -
                                       1) % 8
                self.Pointer_of_ai = (self.Pointer_of_ai + 1) % 64
            else:
                self.Pointer_of_ai = (self.Pointer_of_ai + curr_command) % 64
            curr_command = self.Ai.Gens[self.Pointer_of_ai]
            max_num_of_actions -= 1

        if 0 <= curr_command <= 31:
            action = "move"
        elif 32 <= curr_command <= 63:
            action = "attack"
        elif 64 <= curr_command <= 95:
            action = "check"
        else:
            action = None
        dx, dy = self.Bias_dir[(curr_command + self.Curr_direction - 1) % 8]
        return dx, dy, action

    def print_info(self):
        print("Curr_direction = " + str(self.Curr_direction))
        print("Pointer_of_ai  = " + str(self.Pointer_of_ai))
        print("Life  = " + str(self.Life))
        self.Dna.print_info()
        self.Ai.print_info()
        print("\n\n")


class AI(GenAlgo):
    """ Bot artificial intelligence

    """
    def __init__(self):
        self.Gens = array.array('B')
        self.set_ai()
       
    def set_ai(self):
        for i in range(64):
            self.Gens.append(random.randint(0, 255))

    def print_info(self):
        print("Gens AI:")
        for i in self.Gens:
            print(i, end=" ")
        print('\n')
