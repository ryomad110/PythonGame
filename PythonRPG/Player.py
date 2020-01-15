from random import *
from graphics import *


class Player:
    def __init__(self):
        self.max_hp = 20 + randint(1, 6) + randint(1, 6) + randint(1, 6)
        self.attack = 5 + randint(1, 6) + randint(1, 6)
        self.money = 10 + randint(1, 6) + randint(1, 6) + randint(1, 6)
        self.agility = 5 + randint(1, 6) + randint(1, 6)
        self.now_hp = self.max_hp
        self.weapon_attack = 0

    def resetStat(self):
        self.__init__()

    def levelUpOne(self):
        stat = randint(1, 3)
        if stat == 1:
            self.max_hp = self.max_hp + randint(1, 6) + randint(1, 6)

        if stat == 2:
            self.attack = self.attack + randint(1, 3)

        if stat == 3:
            self.agility = self.agility + randint(1, 3)

    def levelUpAll(self):
        self.max_hp = self.max_hp + randint(1, 6) + randint(1, 6)
        self.attack = self.attack + randint(1, 3)
        self.agility = self.agility + randint(1, 3)
