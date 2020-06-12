from src.map import Map, MapCell


class Test_Map:
    def test_generate(self):
        mp = Map(10)
        mp.generate()
        assert mp.Size == 10
        for line in mp.Field:
            for el in line:
                assert type(el) == MapCell
                assert el.Biom in range(1, 4)
                assert el.Bot_ref is None
                assert el.Food_ref is None
