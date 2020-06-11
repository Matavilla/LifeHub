import array
from src.bot import Bot, AI
import src.map as mp

# add 3 bots for testing
b1, b2, b3 = Bot(1), Bot(2), Bot(3)

# bots programm
Gens1, Gens2, Gens3 = array.array('B'), array.array('B'), array.array('B')

# value and corresponding command:
# 0..39 - move
# 40..79 - attack or catch
# 80..119 - check
# 120..159 - rotate
# 160..255 - jump

for i in range(256):
    Gens1.append(i)
    Gens2.append(255 - i)
    Gens3.append(25)

b1.Ai.Gens, b2.Ai.Gens, b3.Ai.Gens = Gens1, Gens2, Gens3

# current direction of bots:
# 0 -> up + left
# 1 -> up
# 2 -> up + right
# ...
b1.Curr_direction, b2.Curr_direction, b3.Curr_direction = 1, 1, 1

# generate small map for testing 3 bots
tmp_map = mp.Map(9)
tmp_map.generate()
tmp_map.Field[0][0].Bot_ref = b1
tmp_map.Field[2][2].Bot_ref = b2
tmp_map.Field[0][1].Bot_ref = b3

class Test_AI:
    def test_set_ai(self):
        ai_ = AI()
        r = range(256)
        assert len(ai_.Gens) == 256
        for i in r:
            assert ai_.Gens[i] in r


class Test_Bot:
    def test_color(self):
        assert b1.color() == (0, 0, 255)
        assert b2.color() == (255, 255, 224)
        assert b3.color() == (255, 0, 255)

    def test_get_dir_and_action(self):
        dx1, dy1, action1 = b1.get_dir_and_action(0, 0, tmp_map)
        assert dx1 == 1
        assert dy1 == 1
        assert action1 == "move"

        b1.Pointer_of_ai = 85
        dx1, dy1, action1 = b1.get_dir_and_action(0, 0, tmp_map)
        assert dx1 == 1
        assert dy1 == 1
        assert action1 is None
        assert b1.Pointer_of_ai == 121
        assert b1.Curr_direction == 0

        b1.Pointer_of_ai = 46
        dx1, dy1, action1 = b1.get_dir_and_action(0, 0, tmp_map)
        assert dx1 == 0
        assert dy1 == 1
        assert action1 == "attack"

        dx2, dy2, action2 = b2.get_dir_and_action(2, 2, tmp_map)
        assert dx2 == -1
        assert dy2 == -1
        assert action2 == "move"
        assert b2.Pointer_of_ai == 255

        b2.Pointer_of_ai = 215
        dx2, dy2, action2 = b2.get_dir_and_action(2, 2, tmp_map)
        assert dx2 == -1
        assert dy2 == -1
        assert action2 == "attack"

        dx3, dy3, action3 = b3.get_dir_and_action(0, 1, tmp_map)
        assert dx3 == 0
        assert dy3 == -1
        assert action3 == "move"

    def test_get_adaptation_value(self):
        b1.DeathTick, b1.Life, b1.Age = 5, 300, 10
        assert b1.get_adaptation_value() == 10350


