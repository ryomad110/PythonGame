from random import *
from graphics import *


class Player:
    def __init__(self):
        self.max_hp = 20 + randint(1, 6) + randint(1, 6) + randint(1, 6)
        self.attack = 51111 + randint(1, 6) + randint(1, 6)
        self.money = 10 + randint(1, 6) + randint(1, 6) + randint(1, 6)
        self.agility = 5 + randint(1, 6) + randint(1, 6)
        self.now_hp = self.max_hp
        self.weapon_attack = 0
        self.defence = 0
        self.weapon_name = "素手"
        self.armor_name = "普段着"

    def setWeapon(self, wname, watk):
        self.weapon_name = wname
        self.weapon_attack = watk

    def weapon(self, Type):
        if Type == 1:
            self.setWeapon("サバイバルナイフ", 6)
        if Type == 2:
            self.setWeapon("バール", 9)
        if Type == 3:
            self.setWeapon("金属バット", 10)
        if Type == 4:
            self.setWeapon("ナタ", 12)
        if Type == 5:
            self.setWeapon("日本刀", 15)
        if Type == 6:
            self.setWeapon("どうのつるぎ", 15)
        if Type == 7:
            self.setWeapon("ひのきのぼう", 15)
        if Type == 8:
            self.setWeapon("こんぼう", 30)
        if Type == 9:
            self.setWeapon("スレッジハンマー", 17)
        if Type == 10:
            self.setWeapon("レイピア", 18)
        if Type == 11:
            self.setWeapon("拳銃", 20)
        if Type == 12:
            self.setWeapon("歯ブラシ", 23)
        if Type == 13:
            self.setWeapon("ショットガン", 28)
        if Type == 14:
            self.setWeapon("アサルトライフル", 40)
        if Type == 20:
            self.setWeapon("伝説の剣", 100000)

    def addArmor(self, aname, adef):
        self.armor_name = aname
        self.defence = adef

    def armor(self, Type):
        if Type == 1:
            self.addArmor("バイク用プロテクター", 4)
        if Type == 2:
            self.addArmor("甲冑", 7)
        if Type == 3:
            self.addArmor("防弾ジャケット", 9)
        if Type == 4:
            self.addArmor("着ぐるみ", 15)
        if Type == 5:
            self.addArmor("チェインメイル", 11)
        if Type == 6:
            self.addArmor("プレートアーマー", 17)
        if Type == 20:
            self.addArmor("単位", 17)

    def resetStat(self):
        self.__init__()

    def levelUpOne(self):
        stat = randint(1, 3)
        if stat == 1:
            self.max_hp = self.max_hp + randint(1, 6) + randint(1, 6)

        if stat == 2:
            self.attack = self.attack + randint(1, 5)

        if stat == 3:
            self.agility = self.agility + randint(1, 3)

    def levelUpAll(self):
        self.max_hp = self.max_hp + randint(1, 6) + randint(1, 6)
        self.attack = self.attack + randint(1, 5)
        self.agility = self.agility + randint(1, 3)

    def chkGameover(self):
        if self.now_hp <= 0:
            return 1
        else:
            return 0


    def damage(self, amount):
        self.now_hp = self.now_hp - amount
        if self.now_hp < 0:
            self.now_hp = 0
        return "%dのダメージを受けた！" % amount

    def heal(self, amount):
        self.now_hp = self.now_hp + amount
        if self.now_hp > self.max_hp:
            self.now_hp = self.max_hp
        return "HPが%d回復した！" % amount