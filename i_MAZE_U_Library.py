from graphics import *

win = GraphWin("i MAZE U",800,500)

def drawText(coorX, coorY, text, size, color, style):
    text = Text(Point(coorX, coorY), text)
    text.setSize(size)
    text.setTextColor(color)
    text.setStyle(style)
    text.draw(win)

def drawRectangle(coorX1, coorY1, coorX2, coorY2, fill, outline):
    pt1 = Point(coorX1, coorY1)
    pt2 = Point(coorX2, coorY2)

    rec = Rectangle(pt1, pt2)
    rec.setFill(fill)
    rec.setOutline(outline)
    rec.draw(win)

def drawImage(coorX, coorY, image):
    img = Image(Point(coorX, coorY), image)
    img.draw(win)
