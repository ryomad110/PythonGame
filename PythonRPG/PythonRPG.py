from graphics import *
message: Text
win: GraphWin
Qmessage1: Text
Qmessage2: Text
Qmessage3: Text
Qmessage4: Text

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

def updateTextMessage(text):
    global message
    message.setText(text)

if __name__ == '__main__':
    makeWin()
    makeTextBox()
    makeQBox()

    setQ(["平山", "Python", "単位", "A評価"])

    win.getMouse()
    win.close()
