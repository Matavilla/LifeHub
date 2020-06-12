from GUI import Field, StartGame # noqa : F401
from src.map import Map


class Test_Field:
    def test_create_grid(self) -> None:
        field = Field(100, 100, 10)
        mp = Map(10)
        mp.generate()
        field.create_grid(mp)
        for x in range(mp.Size):
            for y in range(mp.Size):
                assert field.Screen.get_at((x, y)) in [(102, 205, 170),
                                                       (152, 251, 152),
                                                       (255, 222, 173)]
