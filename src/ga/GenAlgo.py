import random
import array


class GenAlgo:
    """ Класс отвечающий за генетический алгоритм

    """
    def crossover(dna_1, dna_2):
        """ Скрещивание текущей днк и днк2.

        :param dna_2: днк того, с кем идёт скрещивание.
        :return: Результат работы генетического алгоритма по скрещиванию.
        """
        tmp = random.randint(0, 2)
        if tmp == 0:
            return random.choice(GenAlgo.single_point_crossover(dna_1, dna_2))
        elif tmp == 1:
            return random.choice(GenAlgo.two_point_crossover(dna_1, dna_2))
        elif tmp == 2:
            return random.choice(GenAlgo.uniform_crossover(dna_1, dna_2))

    def mutation(dna, p):
        """ Мутация текущей клетки днк

        :param p: ?
        :return: Результат работы генетического алгоритма по скрешиванию
        """
        tmp = random.randint(0, 3)
        if tmp == 0:
            for i in range(random.randint(1, len(dna))):
                if random.randint(0, 100) < p:
                    GenAlgo.random_mutation(dna)
        elif tmp == 1:
            for i in range(random.randint(1, len(dna))):
                if random.randint(0, 100) < p:
                    GenAlgo.swap_mutation(dna)
        elif tmp == 2:
            for i in range(random.randint(1, len(dna))):
                if random.randint(0, 100) < p:
                    GenAlgo.inversion_mutation(dna)
        elif tmp == 3:
            if random.randint(0, 100) < p:
                GenAlgo.shuffle_mutation(dna)

    def single_point_crossover(dna_1, dna_2):
        """ Halp

        :return:
        """
        bytes_1, bytes_2 = dna_1.tobytes(), dna_2.tobytes()
        res_dna_1 = array.array(dna_1.typecode)
        res_dna_2 = array.array(dna_1.typecode)
        point = random.randint(1, len(bytes_1) - 1)

        res_dna_1.frombytes(bytes_1[:point] + bytes_2[point:])
        res_dna_2.frombytes(bytes_2[:point] + bytes_1[point:])

        return (res_dna_1, res_dna_2)

    def two_point_crossover(dna_1, dna_2):
        """ Halp

        :return:
        """
        bytes_1, bytes_2 = dna_1.tobytes(), dna_2.tobytes()
        res_dna_1 = array.array(dna_1.typecode)
        res_dna_2 = array.array(dna_1.typecode)
        point_1 = random.randint(1, len(bytes_1) // 2)
        point_2 = random.randint(point_1 + 1, len(bytes_1) - 1)

        tmp = bytes_1[:point_1] + bytes_2[point_1:point_2] + bytes_1[point_2:]
        res_dna_1.frombytes(tmp)
        tmp = bytes_2[:point_1] + bytes_1[point_1:point_2] + bytes_2[point_2:]
        res_dna_2.frombytes(tmp)

        return (res_dna_1, res_dna_2)

    def uniform_crossover(dna_1, dna_2):
        """ Halp

        :return:
        """
        bytes_1, bytes_2 = dna_1.tobytes(), dna_2.tobytes()
        res_dna_1 = array.array(dna_1.typecode)
        res_dna_2 = array.array(dna_1.typecode)

        gen_1, gen_2 = bytes(), bytes()
        for i in range(len(bytes_1)):
            tmp = random.randint(0, 1)
            gen_1 += bytes_1[i:i + 1] if tmp else bytes_2[i:i + 1]

            tmp = random.randint(0, 1)
            gen_2 += bytes_1[i:i + 1] if tmp else bytes_2[i:i + 1]

        res_dna_1.frombytes(gen_1)
        res_dna_2.frombytes(gen_2)

        return (res_dna_1, res_dna_2)

    def random_mutation(dna):
        """ Halp

        :return:
        """
        SIZE_CHAR = 256
        index = random.randint(0, len(dna) - 1)
        dna[index] = random.randint(0, SIZE_CHAR ** dna.itemsize - 1)

    def swap_mutation(dna):
        """ Halp

        :return:
        """
        gen_1 = random.randint(0, len(dna) - 1)
        gen_2 = random.randint(0, len(dna) - 1)
        tmp = dna[gen_1]
        dna[gen_1] = dna[gen_2]
        dna[gen_2] = tmp

    def inversion_mutation(dna):
        """ Halp

        :return:
        """
        gen = random.randint(0, len(dna) - 1)
        dna[gen] = abs(~dna[gen]) % 256  # why not

    def shuffle_mutation(dna):
        """ Halp

        :return:
        """
        point_1 = random.randint(0, len(dna) // 2)
        point_2 = random.randint(point_1 + 1, len(dna))
        tmp = dna[point_1:point_2].tolist()
        random.shuffle(tmp)
        dna[point_1:point_2] = array.array(dna.typecode, tmp)[:]
