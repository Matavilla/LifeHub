import random
import array


class GenAlgo:
    def single_point_crossover(dna_1, dna_2):
        bytes_1, bytes_2 = dna_1.tobytes(), dna_2.tobytes()
        res_dna_1 = array.array(dna_1.typecode)
        res_dna_2 = array.array(dna_1.typecode)
        point = random.randint(1, len(bytes_1) - 1)

        res_dna_1.frombytes(bytes_1[:point] + bytes_2[point:])
        res_dna_2.frombytes(bytes_2[:point] + bytes_1[point:])

        return (res_dna_1, res_dna_2)

    def two_point_crossover(dna_1, dna_2):
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
        SIZE_CHAR = 256
        index = random.randint(0, len(dna) - 1)
        dna[index] = random.randint(0, SIZE_CHAR ** dna.itemsize - 1)

    def swap_mutation(self, dna):
        gen_1 = random.randint(0, len(dna) - 1)
        gen_2 = random.randint(0, len(dna) - 1)
        tmp = dna[gen_1]
        dna[gen_1] = dna[gen_2]
        dna[gen_2] = tmp

    def inversion_mutation(dna):
        gen = random.randint(0, len(dna) - 1)
        dna[gen] = abs(~dna[gen])  # why not

    def shuffle_mutation(dna):
        point_1 = random.randint(0, len(dna) // 2)
        point_2 = random.randint(point_1 + 1, len(dna))
        tmp = dna[point_1:point_2].tolist()
        random.shuffle(tmp)
        dna[point_1:point_2] = array.array(dna.typecode, tmp)[:]
