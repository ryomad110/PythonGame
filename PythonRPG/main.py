from graphics import *
import Player
import Enemy
from random import *

message: Text
win: GraphWin
Qmessage1: Text
Qmessage2: Text
Qmessage3: Text
Qmessage4: Text
atk: Text
agi: Text
hp: Text
money: Text
defence: Text

qPoint: int
distance = 100
img = Image(Point(600, 240), "black.gif")
dice = Image(Point(800, 360), "black.gif")
garlic = 0
cross = 0
flash = 0
water = 0


def makeWin():
    global win
    win = GraphWin("Python RPG", 1200, 720)
    win.setBackground(color_rgb(0, 0, 0))


def gameOver():
    delQ()
    delImg()
    updateTextMessage("力尽きてしまった…")
    wait()
    updateTextMessage("Game Over")
    wait()
    updateTextMessage("次は必ず上手くいくはず！")
    wait()
    win.close()
    exit(0)


def makeTextBox():
    global message
    textBox = Rectangle(Point(5, 540), Point(845, 715))
    textBox.setOutline(color_rgb(255, 255, 255))
    textBox.draw(win)
    message = Text(Point(450, 570), "Test")
    message.setOutline(color_rgb(255, 255, 255))
    message.draw(win)


def makeDBox():
    global dist
    dBox = Rectangle(Point(5, 5), Point(180, 120))
    dBox.setOutline(color_rgb(255, 255, 255))
    dBox.draw(win)
    dMessage1 = Text(Point(90, 15), "残り")
    dMessage1.setOutline(color_rgb(255, 255, 255))
    dMessage1.draw(win)
    dMessage2 = Text(Point(90, 105), "km")
    dMessage2.setOutline(color_rgb(255, 255, 255))
    dMessage2.draw(win)
    dist = Text(Point(90, 55), distance)
    dist.setOutline(color_rgb(255, 255, 255))
    dist.draw(win)


def makeSBox():
    global atk, agi, hp, money, defence
    sBox = Rectangle(Point(1020, 5), Point(1195, 115))
    sBox.setOutline(color_rgb(255, 255, 255))
    sBox.draw(win)
    hp = Text(Point(1100, 25), "HP: %d/%d" % (p1.now_hp, p1.max_hp))
    hp.setOutline(color_rgb(255, 255, 255))
    hp.draw(win)
    atk = Text(Point(1100, 45), "ATK: %d + %d(%s)" % (p1.attack, p1.weapon_attack, p1.weapon_name))
    atk.setOutline(color_rgb(255, 255, 255))
    atk.draw(win)
    agi = Text(Point(1100, 65), "AGI: %d" % p1.agility)
    agi.setOutline(color_rgb(255, 255, 255))
    agi.draw(win)
    money = Text(Point(1100, 85), "%d Py" % p1.money)
    money.setOutline(color_rgb(255, 255, 255))
    money.draw(win)
    defence = Text(Point(1100, 105), "DEF: %d(%s)" % (p1.defence, p1.armor_name))
    defence.setOutline(color_rgb(255, 255, 255))
    defence.draw(win)


def makeQBox():
    global qMessage1, qMessage2, qMessage3, qMessage4
    qBox = Rectangle(Point(855, 540), Point(1195, 715))
    qBox.setOutline(color_rgb(255, 255, 255))
    qBox.draw(win)
    qMessage1 = Text(Point(1025, 570), "")
    qMessage1.setOutline(color_rgb(255, 255, 255))
    qMessage1.draw(win)
    qMessage2 = Text(Point(1025, 610), "")
    qMessage2.setOutline(color_rgb(255, 255, 255))
    qMessage2.draw(win)
    qMessage3 = Text(Point(1025, 650), "")
    qMessage3.setOutline(color_rgb(255, 255, 255))
    qMessage3.draw(win)
    qMessage4 = Text(Point(1025, 690), "")
    qMessage4.setOutline(color_rgb(255, 255, 255))
    qMessage4.draw(win)


def setQ(qMessage: list):
    global qPoint
    if (len(qMessage) > 4):
        raise ValueError
    if (len(qMessage) == 4):
        qMessage1.setText(qMessage[0])
        qMessage2.setText(qMessage[1])
        qMessage3.setText(qMessage[2])
        qMessage4.setText(qMessage[3])
    if (len(qMessage) == 3):
        qMessage1.setText(qMessage[0])
        qMessage2.setText(qMessage[1])
        qMessage3.setText(qMessage[2])
    if (len(qMessage) == 2):
        qMessage1.setText(qMessage[0])
        qMessage2.setText(qMessage[1])
    if (len(qMessage) == 1):
        qMessage1.setText(qMessage[0])
    qPoint = 0


def delQ():
    qMessage1.setText("")
    qMessage2.setText("")
    qMessage3.setText("")
    qMessage4.setText("")


def selectQ(key, length):
    global qPoint
    if key == "Up":
        if qPoint == 0:
            qPoint = length - 1
        else:
            qPoint -= 1
    if key == "Down":
        if qPoint == length - 1:
            qPoint = 0
        else:
            qPoint += 1


def question(qMessage: list):
    delQ()
    setQ(qMessage)
    global qPoint
    key = ""
    while key != "Return":
        qMessage1.setOutline(color_rgb(255, 255, 255))
        qMessage2.setOutline(color_rgb(255, 255, 255))
        qMessage3.setOutline(color_rgb(255, 255, 255))
        qMessage4.setOutline(color_rgb(255, 255, 255))

        if qPoint == 0:
            qMessage1.setOutline(color_rgb(218, 165, 32))
        if qPoint == 1:
            qMessage2.setOutline(color_rgb(218, 165, 32))
        if qPoint == 2:
            qMessage3.setOutline(color_rgb(218, 165, 32))
        if qPoint == 3:
            qMessage4.setOutline(color_rgb(218, 165, 32))
        key = win.getKey()
        if key == "Down" or key == "Up":
            selectQ(key, len(qMessage))
        if key == "Return":
            delQ()
            return qPoint


def updateTextMessage(text):
    global message
    message.setText(text)


def updateStats():
    hp.undraw()
    atk.undraw()
    agi.undraw()
    money.undraw()
    hp.setText("HP: %d/%d" % (p1.now_hp, p1.max_hp))
    atk.setText("ATK: %d + %d(%s)" % (p1.attack, p1.weapon_attack, p1.weapon_name))
    agi.setText("AGI: %d" % p1.agility)
    money.setText("%d Py" % p1.money)
    defence.setText("DEF: %d(%s)" % (p1.defence, p1.armor_name))
    hp.draw(win)
    atk.draw(win)
    agi.draw(win)
    money.draw(win)
    if p1.chkGameover() == 1:
        gameOver()


def updateDistance(mass):
    global dist
    global distance
    dist.undraw()
    distance = distance - mass
    if distance < 0:
        distance = 0
    dist = Text(Point(90, 55), distance)
    dist.setOutline(color_rgb(255, 255, 255))
    dist.draw(win)


def updateImg(fileName):
    global img
    img.undraw()
    img = Image(Point(600, 240), fileName)
    img.draw(win)


def delImg():
    global img
    img.undraw()


def wait():
    key = ""
    while key != "Return":
        key = win.getKey()


def makeGUI():
    makeWin()
    makeTextBox()
    makeQBox()
    makeDBox()
    makeSBox()


def rollDice():
    global dice
    result = randint(1, 6)
    dice.undraw()
    if result == 1:
        dice = Image(Point(1100, 480), "d1.gif")
    if result == 2:
        dice = Image(Point(1100, 480), "d2.gif")
    if result == 3:
        dice = Image(Point(1100, 480), "d3.gif")
    if result == 4:
        dice = Image(Point(1100, 480), "d4.gif")
    if result == 5:
        dice = Image(Point(1100, 480), "d5.gif")
    if result == 6:
        dice = Image(Point(1100, 480), "d6.gif")
    dice.draw(win)
    return result


def toBoss():
    while distance != 0:
        updateStats()
        updateTextMessage("ダイスを振りましょう")
        wait()
        diceResult = rollDice()
        updateTextMessage("%dが出ました" % diceResult)
        updateDistance(diceResult)
        wait()
        dice.undraw()
        event()


def getWeaponName(Type):
    if Type == 1:
        return "サバイバルナイフ"
    if Type == 2:
        return "バール"
    if Type == 3:
        return "金属バット"
    if Type == 4:
        return "ナタ"
    if Type == 5:
        return "日本刀"
    if Type == 6:
        return "どうのつるぎ"
    if Type == 7:
        return "ひのきのぼう"
    if Type == 8:
        return "こんぼう"
    if Type == 9:
        return "スレッジハンマー"
    if Type == 10:
        return "レイピア"
    if Type == 11:
        return "拳銃"
    if Type == 12:
        return "歯ブラシ"
    if Type == 13:
        return "ショットガン"
    if Type == 14:
        return "アサルトライフル"
    if Type == 20:
        return "伝説の剣"


def getArmorName(Type):
    if Type == 1:
        return "バイク用プロテクター"
    if Type == 2:
        return "甲冑"
    if Type == 3:
        return "防弾ジャケット"
    if Type == 4:
        return "着ぐるみ"
    if Type == 5:
        return "チェインメイル"
    if Type == 6:
        return "プレートアーマー"
    if Type == 20:
        return "単位"


def treasure(d):
    weaponOrArmor = randint(1, 2)
    updateImg("daiza.gif")
    if weaponOrArmor == 1:
        weaponType = randint(1, 100)
        if weaponType <= 5:
            weaponId = 20
        else:
            weaponId = randint(1, 14)
        updateTextMessage("台座の上に%sが置かれている…" % getWeaponName(weaponId))

        wait()
        updateTextMessage("取りますか？")
        select = question(["はい", "いいえ"])
        if select == 0:
            delQ()
            wanaCheck = randint(1, 100)
            if 1 <= wanaCheck < 20:
                updateTextMessage("台座が爆発して%sもろとも粉々になった！" % getWeaponName(weaponId))
                updateImg("explode.gif")
                wait()
                updateTextMessage(p1.damage(randint(1, 30)))
                updateStats()
                wait()
            if 20 <= wanaCheck < 40:
                updateTextMessage("%sを手に入れた" % getWeaponName(weaponId))
                p1.weapon(weaponId)
                updateStats()
                wait()
            if 40 <= wanaCheck < 70:
                updateTextMessage("台座へ近づくと%sは消えてしまった" % getWeaponName(weaponId))
                wait()
            if 70 <= wanaCheck:
                updateTextMessage("台座へ近づくと矢が飛んできた！")
                wait()
                updateTextMessage(p1.damage(randint(5, 10)))
                updateStats()
                wait()
                updateTextMessage("%sを手に入れた" % getWeaponName(weaponId))
                p1.weapon(weaponId)
                updateStats()
                wait()
        if select == 1:
            delQ()
            updateTextMessage("罠かもしれない。やめておこう")
        delImg()
    if weaponOrArmor == 2:
        armorType = randint(1, 100)
        if armorType <= 5:
            armorId = 20
        else:
            armorId = randint(1, 7)
        updateTextMessage("台座の上に%sが置かれている…" % getArmorName(armorId))

        wait()
        updateTextMessage("取りますか？")
        select = question(["はい", "いいえ"])
        if select == 0:
            delQ()
            wanaCheck = randint(1, 100)
            if 1 <= wanaCheck < 20:
                updateTextMessage("台座が爆発して%sもろとも粉々になった！" % getArmorName(armorId))
                updateImg("explode.gif")
                wait()
                updateTextMessage(p1.damage(randint(1, 30)))
                updateStats()
                wait()
            if 20 <= wanaCheck < 40:
                updateTextMessage("%sを手に入れた" % getArmorName(armorId))
                p1.armor(armorId)
                updateStats()
                wait()
            if 40 <= wanaCheck < 70:
                updateTextMessage("台座へ近づくと%sは消えてしまった" % getArmorName(armorId))
                wait()
            if 70 <= wanaCheck:
                updateTextMessage("台座へ近づくと矢が飛んできた！")
                wait()
                updateTextMessage(p1.damage(randint(5, 10)))
                updateStats()
                wait()
                updateTextMessage("%sを手に入れた" % getArmorName(armorId))
                p1.armor(armorId)
                updateStats()
                wait()
        if select == 1:
            delQ()
            updateTextMessage("罠かもしれない。やめておこう")
        delImg()


def td():
    return randint(1, 6) + randint(1, 6)


def enemyAttack(mo, pl):
    dodge = 0
    updateTextMessage("%sの攻撃！" % mo.name)
    if randint(1, 100) < pl.agility:
        updateTextMessage("攻撃を回避した！")
        wait()
        return
    else:
        damageAmount = mo.attack + td() - pl.defence - randint(1, 3)
        updateTextMessage(pl.damage(damageAmount))
        wait()
        updateStats()


def playerAttack(pl, mo):
    dodge = 0
    updateTextMessage("あなたの攻撃！")
    if randint(1, 100) < mo.agility:
        updateTextMessage("%sは攻撃を回避した！" % mo.name)
        wait()
        return
    else:
        damageAmount = pl.attack + pl.weapon_attack + randint(1, 6) - mo.defence - randint(1, 3)
        updateTextMessage(mo.damage(damageAmount))
        wait()
        updateStats()


def battle(d):
    over = 0
    isWin = 0

    m = Enemy.Enemy(d)
    updateImg(m.img)
    fa = 0
    if p1.agility + td() > m.agility + td():
        fa = 1  # First Attack
    updateTextMessage("%sが現れた！" % m.name)
    wait()
    if fa == 0:
        updateTextMessage("先手を打たれた！")
        wait()
        updateTextMessage("%sの攻撃！" % m.name)
        enemyAttack(m, p1)
    while over != 1:
        updateTextMessage("行動を選択")
        select = question(["攻撃", "逃げる"])
        if select == 0:
            delQ()
            playerAttack(p1, m)
            if m.isDie() == 1:
                isWin = 1
                over = 1
        if select == 1:
            delQ()
            escapeWin = 0
            if p1.agility + td() >= m.agility + td():
                escapeWin = 1
            updateTextMessage("あなたは逃げだした！")
            wait()
            if escapeWin == 1:
                updateTextMessage("なんとか撒いたようだ")
                delImg()
                wait()
                over = 1
            if escapeWin == 0:
                updateTextMessage("追い付かれた！")
                wait()
        if over == 0:
            updateTextMessage("%sの攻撃！" % m.name)
            wait()
            enemyAttack(m, p1)
        if isWin == 1:
            updateTextMessage("%sを倒した！" % m.name)
            delImg()
            wait()
            if p1.now_hp <= 10:
                p1.levelUpAll()
                updateTextMessage("命懸けの戦いで全ステータスアップ！")
            if p1.now_hp > 10:
                p1.levelUpOne()
                updateTextMessage("ステータスアップ！")
            wait()
            winMoney = 0
            for i in range(m.Lvl):
                winMoney = winMoney + randint(2, 5)
            updateTextMessage("%dPyを手に入れた" % winMoney)
            p1.money = p1.money + winMoney
            wait()


def warpDoor():
    global distance
    updateImg("door.gif")
    updateTextMessage("どこへ出るか分からないワープ扉だ")
    wait()
    updateTextMessage("入りますか？")
    select = question(["はい", "いいえ"])
    if select == 0:
        delQ()
        warpd = randint(1, 100)
        distance = warpd
        updateDistance(0)
        updateTextMessage("%dkm地点へワープしました" % warpd)
        delImg()
        wait()
    if select == 1:
        delQ()
        updateTextMessage("やめておこう")
        delImg()
        wait()


def izumi():
    updateImg("izumi.gif")
    updateTextMessage("綺麗な泉がある")
    wait()
    updateTextMessage("喉が渇いた")
    select = question(["一口飲む", "飲まない"])
    if select == 0:
        izumiType = randint(1, 100)
        if izumiType <= 10:
            updateTextMessage("全ステータスが上がった")
            p1.levelUpAll()
            updateStats()
            wait()
        if 10 < izumiType <= 40:
            updateTextMessage(p1.heal(randint(5, 20)))
            wait()
        if 40 < izumiType <= 60:
            updateTextMessage("ステータスがどれか1つ上がった")
            p1.levelUpOne()
            wait()
        if 60 < izumiType <= 80:
            updateTextMessage("変な味だった")
            wait()
            updateTextMessage("特に何も起こらなかった")
            wait()
        if 80 < izumiType <= 90:
            updateTextMessage("HPが全回復した")
            p1.now_hp = p1.max_hp
            updateStats()
            wait()
        if 90 < izumiType <= 97:
            updateTextMessage("猛毒だ！")
            wait()
            updateTextMessage(p1.damage(randint(5, 30)))
            wait()
        if 97 < izumiType <= 100:
            updateTextMessage("伝説の泉だった")
            wait()
            updateTextMessage("HPが全回復した")
            p1.now_hp = p1.max_hp
            updateStats()
            wait()
            for i in range(3):
                p1.levelUpAll()
            updateTextMessage("全てのステータスが大きく上がった")
            updateStats()
            wait()
        delImg()

def megami():
    updateTextMessage("天から声が聞こえる・・・")
    wait()
    updateTextMessage("「あなたに祝福を与えましょう」")
    wait()
    for i in range(3):
        p1.levelUpAll()
    updateStats()
    updateTextMessage("全てのステータスが大きく上がった")
    wait()


def otherEvents(d):
    eventType = randint(1, 100)
    if eventType <= 5:
        warpDoor()
    if 5 < eventType <= 30:
        izumi()
    if 30 < eventType <= 35:
        megami()
    if 35 < eventType <= 100:
        updateTextMessage("特に何もなかった")
        wait()


def intro():
    updateTextMessage("イントロをスキップしますか？")
    select = question(["はい", "いいえ"])
    if select == 0:
        delQ()
        return
    if select == 1:
        delQ()
        updateTextMessage("最近、山奥に住む吸血鬼がたびたび町で悪事を働いているようです")
        wait()
        updateTextMessage("被害者が増えた末、遂に懸賞金が掛けられました")
        wait()
        updateTextMessage("あなたは懸賞金目当てで討伐へと出発することにしました")
        wait()


def shop():
    updateImg("Shop.gif")
    updateTextMessage("何かの店だ")
    wait()
    shopType = randint(2, 3)
    if shopType == 1 or shopType == 2:
        updateTextMessage("武器屋のようだ")
        shoppingEnd = 1
        wait()
        weapon1 = randint(1, 14)
        weapon2 = randint(1, 14)
        weapon3 = randint(1, 14)
        while shoppingEnd != 0:
            updateTextMessage("品揃えは…")
            select = question([getWeaponName(weapon1), getWeaponName(weapon2), getWeaponName(weapon3), "何も買わない"])
            if select == 0:
                price = weapon1 * 4 + 5
                updateTextMessage("%sを%dPyで購入します" % (getWeaponName(weapon1), price))
                select = question(["はい", "いいえ"])
                if select == 0:
                    if price <= p1.money:
                        p1.weapon(weapon1)
                        p1.money = p1.money - price
                        delQ()
                        delImg()
                        shoppingEnd = 0
                    else:
                        delQ()
                        updateTextMessage("所持金が足りない")
                        wait()
                if select == 1:
                    select = 0
            if select == 1:
                price = weapon2 * 4 + 5
                updateTextMessage("%sを%dPyで購入します" % (getWeaponName(weapon2), price))
                select = question(["はい", "いいえ"])
                if select == 0:
                    if price <= p1.money:
                        p1.weapon(weapon2)
                        p1.money = p1.money - price
                        delQ()
                        delImg()
                        shoppingEnd = 0
                    else:
                        delQ()
                        updateTextMessage("所持金が足りない")
                        wait()
                if select == 1:
                    select = 0
            if select == 2:
                price = weapon3 * 4 + 5
                updateTextMessage("%sを%dPyで購入します" % (getWeaponName(weapon3), price))
                select = question(["はい", "いいえ"])
                if select == 0:
                    if price <= p1.money:
                        p1.weapon(weapon3)
                        p1.money = p1.money - price
                        delQ()
                        delImg()
                        shoppingEnd = 0
                    else:
                        delQ()
                        updateTextMessage("所持金が足りない")
                        wait()
                if select == 1:
                    select = 0
            if select == 3:
                updateTextMessage("何も買わずに店を出ます")
                select = question(["はい", "いいえ"])
                if select == 0:
                    delQ()
                    delImg()
                    shoppingEnd = 0
                if select == 1:
                    delQ()

    if shopType == 3:
        updateTextMessage("宿屋のようだ")
        price = (p1.max_hp - p1.now_hp) / 2
        wait()
        if p1.now_hp == p1.max_hp:
            updateTextMessage("元気なので泊まっていかなくてもいいだろう")
            wait()
            delImg()
            return
        updateTextMessage("泊まっていきますか(宿泊費%dPy" % price)
        select = question(["はい", "いいえ"])
        if select == 0:
            if price <= p1.money:
                p1.now_hp = p1.max_hp
                p1.money = p1.money - price
                delQ()
                delImg()
                updateTextMessage("1泊したことでHPが全て回復した")
                wait()
                return
            else:
                updateTextMessage("所持金が足りない")
                delQ()
                wait()
                delImg()
                return
        if select == 1:
            delQ()
            return


def event():
    randomEvent = randint(1, 100)
    if randomEvent <= 40:  # 戦闘40%
        battle(distance)
        delImg()
    if 40 < randomEvent <= 50:  # トレジャー10%
        treasure(distance)
    if 50 < randomEvent <= 80:  # その他のイベント30%
        otherEvents(distance)
    if 80 < randomEvent:  # ショップ
        shop()


def boss():
    updateTextMessage("吸血鬼の根城へとたどり着いた")
    wait()
    updateImg("vamp.gif")
    updateTextMessage("「この私を1人で倒すつもりとは恐れ入った」")
    wait()
    updateTextMessage("「かかってくるがよい！」")
    wait()
    vamp = Enemy.Vampire()
    if garlic == 1:
        updateTextMessage("あなたはにんにくを投げつけた")
        wait()
        updateTextMessage("「ぐあああ！臭い！」")
        wait()
        updateTextMessage("吸血鬼の動きが鈍くなった")
        wait()
        vamp.garlic()
    if water == 1:
        updateTextMessage("あなたは聖水を身体に振りかけた！")
        wait()
        updateTextMessage("「そんな雨水で何ができる」")
        wait()
        vamp.water()
        updateTextMessage("吸血鬼の攻撃が通りにくくなった！")
        wait()
    if cross == 1:
        updateTextMessage("あなたは十字架を天に掲げた！")
        wait()
        updateTextMessage("ぐあああ！！！忌々しい！")
        wait()
        updateTextMessage("吸血鬼の防御力が下がった")
        vamp.cross()
        wait()
        updateTextMessage("十字架は役目を終えて砕け散った")
        wait()
    if flash == 1:
        updateTextMessage("あなたは吸血鬼に懐中電灯を照射した！")
        wait()
        updateTextMessage("「ぐあああ！！！身体が焼けるっ！！！」")
        vamp.flash()
        wait()
        updateTextMessage("懐中電灯の電池が切れてしまった")
        wait()
        updateTextMessage("が、吸血鬼に大きなダメージを与えた")
        wait()


def ending():
    updateTextMessage("あなたの活躍により、吸血鬼は封印されました。")
    wait()
    updateTextMessage("これで安心して眠れます。")
    wait()
    updateTextMessage("終")
    wait()
    updateTextMessage("制作・著作━━━━━3班")
    wait()
    updateTextMessage("ここまでプレイしていただきありがとうございました！")
    wait()
    updateTextMessage("短期間で急いで作ったゲームですが、楽しんで頂けたならば幸いです。")
    wait()


def goal():  # ボス未実装につきゴールとして処理
    delQ()
    delImg()
    updateTextMessage("ゴール地点へ到達しました。")
    wait()
    updateTextMessage("終")
    wait()
    updateTextMessage("制作・著作━━━━━3班")
    wait()
    updateTextMessage("ここまでプレイしていただきありがとうございました！")
    wait()
    updateTextMessage("短期間で作った拙い出来のゲームですが、楽しんで頂けたならば幸いです。")
    wait()


def defstats():
    updateTextMessage("プレイヤーの初期ステータスを決めて下さい")
    select1 = question(["決定", "振り直す"])
    while select1 != 0:
        if select1 == 1:
            p1.resetStat()
            updateStats()
            select1 = question(["決定", "振り直す"])
    delQ()
    delImg()
    updateTextMessage("旅の始まりです")
    wait()


if __name__ == '__main__':
    p1 = Player.Player()
    makeGUI()
    updateImg("enemy.gif")
    diceResult = 0
    # intro()   ボス未実装のためコメントアウト
    defstats()
    toBoss()
    # boss()    未実装
    goal()
    win.close()
