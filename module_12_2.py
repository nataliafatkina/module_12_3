import unittest as ut
from unittest import skipIf

from Module_12.runner_and_tournament import Runner, Tournament


class TournamentTest(ut.TestCase):

    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Усэйн',10)
        self.runner2 = Runner('Андрей',9)
        self.runner3 = Runner('Ник',3)

    @classmethod
    def tearDownClass(cls):
        if cls.all_results != {}:
            for i in range(3):
                print(cls.all_results[i])

    @ut.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge1(self):
        self.tournament = Tournament(90, self.runner1, self.runner3)
        self.all_results[0] = {k: v.name for k, v in self.tournament.start().items()}
        self.assertTrue(self.all_results[0][1], 'Ник')

    @ut.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge2(self):
        self.tournament = Tournament(90, self.runner2, self.runner3)
        self.all_results[1] = {k: v.name for k, v in self.tournament.start().items()}
        self.assertTrue(self.all_results[1][1], 'Ник')

    @ut.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge3(self):
        self.tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        self.all_results[2] = {k: v.name for k, v in self.tournament.start().items()}
        self.assertTrue(self.all_results[2][2], 'Ник')

