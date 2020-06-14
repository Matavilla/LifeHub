"""
Данный модуль содержит класс, отвечающий за селекцию ботов.
"""

import random
import src.bot as bot
from src.ga.GenAlgo import GenAlgo


class Selection(GenAlgo):
    """ Класс, осуществляющий селекцию ботов.
    """
    def get_parent(bots):
        """ Функция выбора родителя - "колесо фортуны".

        :param bots: Популяция ботов.
        :return bot: Родитель.
        """
        v_1 = random.randint(0, 99) / 100
        sum_adaptation = 0
        for bot in bots: # noqa : F402
            sum_adaptation += bot.get_adaptation_value()

        for bot in bots:
            p = bot.get_adaptation_value() / sum_adaptation
            v_1 -= p
            if v_1 <= 0:
                return bot

    def check_diff(dna_1, dna_2):
        """ Функция, определяющая расстояние Хемминга 2 массивов.

        :param dna: Массивы битов.
        :return R: Расстояние Хемминга.
        """
        ans = 0
        for i in range(len(dna_1)):
            ans += dna_1[i] ^ dna_2[i]
        return ans

    def crossing(gens_1, gens_2):
        """ Функция скрещивания 2 генотипов.

        :param gens: Генотипы.
        :return gen: Генотип после скрещивания.
        """
        p_mut = 20
        dif = Selection.check_diff(gens_1, gens_2)
        if dif < (len(gens_1) * 8) // 2:
            p_mut = 40
        elif dif < (len(gens_1) * 8) // 3:
            p_mut = 60

        ans = Selection.crossover(gens_1, gens_2)

        Selection.mutation(ans, p_mut)

        return ans

    def get_child(bot_1, bot_2, biom):
        """ Функция создания бота-ребенка от 2 родителей.

        :param bot: Родители бота.
        :param biom: Биом ботов.
        :return child: Ребенок-бот.
        """
        child = bot.Bot(biom)
        child.Dna.Gens = Selection.crossing(bot_1.Dna.Gens, bot_2.Dna.Gens)
        child.Ai.Gens = Selection.crossing(bot_1.Ai.Gens, bot_2.Ai.Gens)

        return child
