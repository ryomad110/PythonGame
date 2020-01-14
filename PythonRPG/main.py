from graphics import *
import PythonRPG.Player
message: Text
win: GraphWin
Qmessage1: Text
Qmessage2: Text
Qmessage3: Text
Qmessage4: Text
qPoint: int
distance = 100
img = Image(Point(600, 240), "black.gif")

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
    dMessage2 = Text(Point(90, 105), "マス")
    dMessage2.setOutline(color_rgb(255, 255, 255))
    dMessage2.draw(win)
    dist = Text(Point(90, 55), distance)
    dist.setOutline(color_rgb(255, 255, 255))
    dist.draw(win)
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
    if(len(qMessage) > 4):
        raise ValueError
    if(len(qMessage) == 4):
        qMessage1.setText(qMessage[0])
        qMessage2.setText(qMessage[1])
        qMessage3.setText(qMessage[2])
        qMessage4.setText(qMessage[3])
    if(len(qMessage) == 3):
        qMessage1.setText(qMessage[0])
        qMessage2.setText(qMessage[1])
        qMessage3.setText(qMessage[2])
    if(len(qMessage) == 2):
        qMessage1.setText(qMessage[0])
        qMessage2.setText(qMessage[1])
    if(len(qMessage) == 1):
        qMessage1.setText(qMessage[0])
    qPoint = 0
def delQ():
    qMessage1.setText("")
    qMessage2.setText("")
    qMessage3.setText("")
    qMessage4.setText("")
def selectQ(key):
    global qPoint
    if key == "Up":
        if qPoint == 0:
            qPoint = 3
        else:
            qPoint = qPoint - 1
    if key == "Down":
        if qPoint == 3:
            qPoint = 0
        else:
            qPoint = qPoint + 1

def question():
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
            selectQ(key)
        if key == "Return":
            return qPoint

def updateTextMessage(text):
    global message
    message.setText(text)

def updateDistance(mass):
    global dist
    global distance
    dist.setOutline(color_rgb(0, 0, 0))
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



if __name__ == '__main__':
    p1 = PythonRPG.Player.Player
    makeWin()
    makeTextBox()
    makeQBox()
    makeDBox()
    updateImg("ozisan.gif")
    updateTextMessage("プレイヤーの初期ステータスを決めて下さい")
    setQ(["決定", "振り直す"])
    select1 = question()
    if select1 == 1:
        updateDistance(66)
    delQ()
    wait()
    win.close()
