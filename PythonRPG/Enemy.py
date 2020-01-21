from random import *


class Enemy:
    def __init__(self, d):
        self.img = "enemy.gif"
        if d <= 20:
            self.Lvl = 5
            self.name = "ドラゴン"
            self.img = "Dragon.gif"
        if 20 < d <= 40:
            self.Lvl = 4
            self.name = "ライオン"
            self.img = "lion.gif"
        if 40 < d <= 60:
            self.Lvl = 3
            self.name = "鹿"
            self.img = "sika.gif"
        if 60 < d <= 80:
            self.Lvl = 2
            self.name = "コウモリ"
            self.img = "koumori.gif"
        if 80 < d:
            self.Lvl = 1
            self.name = "カラス"
            self.img = "karasu.gif"
        self.attack = 1
        self.hp = 5
        self.defence = 0
        self.agility = 5
        for i in range(self.Lvl):
            self.levelUp()

    def levelUp(self):
        self.hp = self.hp + randint(1, 6) + randint(1, 6)
        self.attack = self.attack + randint(1, 5)
        self.agility = self.agility + randint(1, 2)
        self.defence = self.defence + randint(1, 3)

    def damage(self, amount):
        self.hp = self.hp - amount
        if self.hp < 0:
            self.hp = 0
        return "%sに%dのダメージを与えた！" % (self.name, amount)


    def isDie(self):
        if self.hp == 0:
            return 1
        else:
            return 0


class Vampire:
    def __init__(self):
        self.hp = 150
        self.attack = 40
        self.agi = 15
        self.defence = 20
        self.name = "吸血鬼"

    def flash(self):
        self.hp = 75

    def cross(self):
        self.defence = 0

    def garlic(self):
        self.agi = 1

    def water(self):
        self.attack = 10

    def isDie(self):
        if self.hp == 0:
            return 1
        else:
            return 0
