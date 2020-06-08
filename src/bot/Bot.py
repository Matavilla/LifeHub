import random
import array
import src.dna as dna


class Bot:
    Biom_bot_color = {1: (25, 23, 163),
                      2: (176, 163, 42),
                      3: (173, 50, 58)}

    Bias_dir = [(-1, -1), (0, -1), (1, -1), (1, 0),
                (1, 1), (0, 1), (-1, 1), (-1, 0)]

    def __init__(self, biom):
        self.Dna = dna.Dna(biom)
        self.Ai = AI()
        self.Curr_direction = random.randint(0, 7)
        self.Pointer_of_ai = 0
        self.Life = 300
        self.set_color()
        self.DeathTick = 0
        self.Age = 0  
        # amount of ticks for one move
        self.TimeSpeed = 5 - (self.Dna.get("speed") // 52)

    def set_color(self):
        self.Color = self.Biom_bot_color[self.Dna.Biom]

    def get_dir_and_action(self, x, y, map_):
        """ 0..39 - move
            40..79 - attack or catch
            80..119 - check
            120..159 - rotate
            160..255 - jump

        """
        curr_command = self.Ai.Gens[self.Pointer_of_ai]
        dx, dy, action = 0, 0, None
        max_num_of_actions = 10
        while 80 <= curr_command <= 255 and max_num_of_actions:
            num_bias_dir = (curr_command + self.Curr_direction - 1) % 8
            if curr_command < 120:
                # check command
                dx, dy = self.Bias_dir[num_bias_dir]
                if x + dx >= map_.Size or x + dx < 0:
                    dx = -dx
                if y + dy >= map_.Size or y + dy < 0:
                    dy = -dy
                if map_.Field[x + dx][y + dy].is_bot_here():
                    self.Pointer_of_ai = (self.Pointer_of_ai + 3) % 256
                elif map_.Field[x + dx][y + dy].is_food_here():
                    self.Pointer_of_ai = (self.Pointer_of_ai + 4) % 256
                else:
                    self.Pointer_of_ai = (self.Pointer_of_ai + 5) % 256
            if curr_command < 160:
                # rotate command
                self.Curr_direction = num_bias_dir
                self.Pointer_of_ai = (self.Pointer_of_ai + 1) % 256
            else:
                self.Pointer_of_ai = (self.Pointer_of_ai + curr_command) % 256
            curr_command = self.Ai.Gens[self.Pointer_of_ai]
            max_num_of_actions -= 1

        if 0 <= curr_command <= 39:
            action = "move"
        elif 40 <= curr_command <= 79:
            action = "attack"

        num_bias_dir = (curr_command + self.Curr_direction - 1) % 8
        dx, dy = self.Bias_dir[num_bias_dir]
        if x + dx >= map_.Size or x + dx < 0:
            dx = -dx
        if y + dy >= map_.Size or y + dy < 0:
            dy = -dy
        return dx, dy, action

    def print_info(self):
        print("Curr_direction = " + str(self.Curr_direction))
        print("Pointer_of_ai  = " + str(self.Pointer_of_ai))
        print("Life  = " + str(self.Life))
        self.Dna.print_info()
        # self.Ai.print_info()
        print("\n\n")

    def get_adaptation_value(self):
        return self.Age * 100 + self.DeathTick * 10 + self.Life;



class AI:
    """ Bot artificial intelligence

    """
    def __init__(self):
        self.Gens = array.array('B')
        self.set_ai()

    def set_ai(self):
        for i in range(256):
            self.Gens.append(random.randint(0, 255))

    def print_info(self):
        print("Gens AI:")
        for i in self.Gens:
            print(i, end=" ")
        print('\n')
