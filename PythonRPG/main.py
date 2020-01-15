from graphics import *
import PythonRPG.Player
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

qPoint: int
distance = 100
img = Image(Point(600, 240), "black.gif")
dice = Image(Point(800, 360), "black.gif")


def makeWin():
    global win
    win = GraphWin("Python RPG", 1200, 720)
    win.setBackground(color_rgb(0, 0, 0))


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
    global atk, agi, hp, money
    sBox = Rectangle(Point(1020, 5), Point(1195, 100))
    sBox.setOutline(color_rgb(255, 255, 255))
    sBox.draw(win)
    hp = Text(Point(1100, 25), "HP: %d/%d" % (p1.now_hp, p1.max_hp))
    hp.setOutline(color_rgb(255, 255, 255))
    hp.draw(win)
    atk = Text(Point(1100, 45), "ATK: %d" % p1.attack)
    atk.setOutline(color_rgb(255, 255, 255))
    atk.draw(win)
    agi = Text(Point(1100, 65), "AGI: %d" % p1.agility)
    agi.setOutline(color_rgb(255, 255, 255))
    agi.draw(win)
    money = Text(Point(1100, 85), "%d Py" % p1.money)
    money.setOutline(color_rgb(255, 255, 255))
    money.draw(win)


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
    atk.setText("ATK: %d" % p1.attack)
    agi.setText("AGI: %d" % p1.agility)
    money.setText("%d Py" % p1.money)
    hp.draw(win)
    atk.draw(win)
    agi.draw(win)
    money.draw(win)


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
        updateTextMessage("ダイスを振りましょう")
        wait()
        diceResult = rollDice()
        updateTextMessage("%dが出ました" % diceResult)
        updateDistance(diceResult)
        event()


def treasure(d):
    pass


def battle(d):
    pass


def otherEvents(d):
    pass


def shop():
    pass


def event():
    randomEvent = randint(1, 100)
    if randomEvent <= 40:  # 戦闘
        battle(distance)
    if 40 < randomEvent <= 70:  # トレジャー
        treasure(distance)
    if 70 < randomEvent <= 90:  # その他のイベント
        otherEvents(distance)
    else:  # ショップ
        shop()


def boss():
    pass


if __name__ == '__main__':
    p1 = PythonRPG.Player.Player()
    makeGUI()
    updateImg("ozisan.gif")
    diceResult = 0
    updateTextMessage("プレイヤーの初期ステータスを決めて下さい")
    select1 = question(["決定", "振り直す"])
    while select1 != 0:
        if select1 == 1:
            p1.resetStat()
            updateStats()
            select1 = question(["決定", "振り直す"])
    delQ()
    updateTextMessage("冒険の始まりです")
    wait()
    toBoss()
    boss()
    wait()
    win.close()
