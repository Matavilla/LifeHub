from src.food import Food


class Test_Food:
    def test_set_color(self):
        f1, f2, f3 = Food(1), Food(2), Food(3)
        f1.Food_value, f1.Toxic_value = 100, 100
        f2.Food_value, f2.Toxic_value = 120, 30
        f3.Food_value, f3.Toxic_value = 30, 200
        f1.set_color(), f2.set_color(), f3.set_color()
        assert f1.Color == (30, 200, 30)
        assert f2.Color == (30, 240, 30)
        assert f3.Color == (30, 60, 30)
