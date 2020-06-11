from src.dna import Dna


class Test_Dna:
    def test_set_value(self):
        dna1, dna2 = Dna(), Dna(2)
        dna1.set_value("test1", 0)
        dna2.set_value("test2", 1)
        assert dna1.get("test1") == 0
        assert dna2.get("test2") == 1

        dna1.set_value(0, 1)
        assert dna1.get(0) == 1

    def test_get(self):
        dna = Dna(1)
        assert dna.get("agression") in range(127, 154)
        assert dna.get("speed") in range(0, 104)
        assert dna.get("sensity") in range(25, 77)
        assert dna.get("power") in range(120, 151)
        assert dna.get("agression") in range(127, 154)
        assert dna.get("armor") in range(127, 179)
        assert dna.get("weather_resistance_1") == 255
        assert dna.get("weather_resistance_2") == 127
        assert dna.get("weather_resistance_3") == 0
        assert dna.get("poison_vulnerability") in range(127, 179)
