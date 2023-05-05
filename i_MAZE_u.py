from i_MAZE_U_Library import *

def finalScreen():
    drawImage(400, 250, "end_screen.png")
    win.getMouse()
    win.close()

def levelThree():
    pt1 = Point(520,395)
    pt2 = Point(520,445)
    pt3 = Point(48,445)
    pt4 = Point(48,327)
    pt5 = Point(450,327)
    pt6 = Point(450,290)
    pt7 = Point(48,290)
    pt8 = Point(48,182)
    pt9 = Point(385,182)
    pt10 = Point(385,138)
    pt11 = Point(357,138)
    pt12 = Point(357,95)
    pt13 = Point(388,95)
    pt14 = Point(388,74)
    pt15 = Point(400,74)
    pt16 = Point(400,108)
    pt17 = Point(372,108)
    pt18 = Point(372,124)
    pt19 = Point(400,124)
    pt20 = Point(400,195)
    pt21 = Point(377,195)
    pt22 = Point(377,205)
    pt23 = Point(70,205)
    pt24 = Point(70,250)
    pt25 = Point(480,250)
    pt26 = Point(480,365)
    pt27 = Point(97,365)
    pt28 = Point(97,395)

    level3 = Polygon(pt1,pt2,pt3,pt4,pt5,pt6,pt7,pt8,pt9,pt10,pt11,pt12,pt13,pt14,pt15,pt16,pt17,pt18,pt19,pt20,pt21,pt22,pt23,pt24,pt25,pt26,pt27,pt28)
    # level3.draw(win)

    drawImage(400, 250, "Level_3.png")

    
    box = Rectangle(Point(498,418),Point(502,422))
    box.setFill('red')
    box.draw(win)

    goal = Rectangle(Point(381,48),Point(407,74))
    # goal.setFill('red')
    # goal.draw(win)

    while True:
        keyValue = win.checkKey()
        point = box.getCenter()
        xVal = point.getX()
        yVal = point.getY()
        if keyValue == "Right":
            dx = 5
            dy = 0
            box.move(dx,dy)
                    
        elif keyValue == "Left":
            dx = 5
            dy = 0
            box.move(-dx,dy)
                    
        elif keyValue == "Up":
            dx = 0
            dy = 5
            box.move(dx,-dy)
                    
        elif keyValue == "Down":
            dx = 0
            dy = 5
            box.move(dx,dy)

        # Right Vertical L1   
        elif (xVal > 94 and yVal > 362) and (xVal > 94 and yVal < 398):
            box.undraw()
            box = Rectangle(Point(498,418),Point(502,422))
            box.setFill('red')
            box.draw(win)

        # Right Vertical L2   
        elif (xVal > 517 and yVal > 398) and (xVal > 517 and yVal < 442):
            box.undraw()
            box = Rectangle(Point(498,418),Point(502,422))
            box.setFill('red')
            box.draw(win)

        # Down Horizontal L3   
        elif (xVal > 51 and yVal > 442) and (xVal < 517 and yVal > 442):
            box.undraw()
            box = Rectangle(Point(498,418),Point(502,422))
            box.setFill('red')
            box.draw(win)

        # Left Vertical L4
        elif (xVal < 51 and yVal > 331) and (xVal < 51 and yVal < 442):
            box.undraw()
            box = Rectangle(Point(498,418),Point(502,422))
            box.setFill('red')
            box.draw(win)

        # Left Vertical L5
        elif (xVal < 453 and yVal > 287) and (xVal < 453 and yVal < 331):
            box.undraw()
            box = Rectangle(Point(498,418),Point(502,422))
            box.setFill('red')
            box.draw(win)

        # Right Vertical L6   
        elif (xVal > 477 and yVal > 253) and (xVal > 477 and yVal < 362):
            box.undraw()
            box = Rectangle(Point(498,418),Point(502,422))
            box.setFill('red')
            box.draw(win)

        # Right Vertical L7   
        elif (xVal > 67 and yVal > 202) and (xVal > 67 and yVal < 253):
            box.undraw()
            box = Rectangle(Point(498,418),Point(502,422))
            box.setFill('red')
            box.draw(win)

        # Left Vertical L8
        elif (xVal < 51 and yVal > 186) and (xVal < 51 and yVal < 453):
            box.undraw()
            box = Rectangle(Point(498,418),Point(502,422))
            box.setFill('red')
            box.draw(win)

        # Left Vertical L9
        elif (xVal < 389 and yVal > 134) and (xVal < 389 and yVal < 185):
            box.undraw()
            box = Rectangle(Point(498,418),Point(502,422))
            box.setFill('red')
            box.draw(win)

        # Right Vertical L10   
        elif (xVal > 374 and yVal > 191) and (xVal > 374 and yVal < 202):
            box.undraw()
            box = Rectangle(Point(498,418),Point(502,422))
            box.setFill('red')
            box.draw(win)

        # Right Vertical L11   
        elif (xVal > 397 and yVal > 124) and (xVal > 397 and yVal < 193):
            box.undraw()
            box = Rectangle(Point(498,418),Point(502,422))
            box.setFill('red')
            box.draw(win)

        # Right Vertical L12   
        elif (xVal > 369 and yVal > 106) and (xVal > 369 and yVal < 126):
            box.undraw()
            box = Rectangle(Point(498,418),Point(502,422))
            box.setFill('red')
            box.draw(win)

        # Left Vertical L13
        elif (xVal < 359 and yVal > 95) and (xVal < 359 and yVal < 138):
            box.undraw()
            box = Rectangle(Point(498,418),Point(502,422))
            box.setFill('red')
            box.draw(win)

        # Left Vertical L14
        elif (xVal < 390 and yVal > 74) and (xVal < 390 and yVal < 97):
            box.undraw()
            box = Rectangle(Point(498,418),Point(502,422))
            box.setFill('red')
            box.draw(win)

        # Right Vertical L15   
        elif (xVal > 397 and yVal > 74) and (xVal > 397 and yVal < 108):
            box.undraw()
            box = Rectangle(Point(498,418),Point(502,422))
            box.setFill('red')
            box.draw(win)

        # Up Horizontal Goal
        elif (xVal > 388 and yVal < 75) and (xVal < 400 and yVal < 75):
            box.undraw()
            level3.undraw()
            goal.undraw()
            finalScreen()

def levelTwo():
    drawImage(400, 250, "Level_2.png")

    
    level2 = Polygon(Point(225,450),Point(325,450),Point(325,420),Point(488,420),Point(488,190),Point(125,190),Point(125,117),Point(288,117),Point(288,50),Point(263,50),Point(263,83),Point(75,83),Point(75,260),Point(413,260),Point(413,335),Point(225,335))
    # level2.draw(win)

    box = Rectangle(Point(270,415),Point(275,420))
    box.setFill('red')
    box.draw(win)

    goal = Rectangle(Point(263,50),Point(288,75))
    # goal.setFill('red')
    # goal.draw(win)

    while True:
        keyValue = win.checkKey()
        point = box.getCenter()
        xVal = point.getX()
        yVal = point.getY()
        if keyValue == "Right":
                dx = 8
                dy = 0
                box.move(dx,dy)
                
        elif keyValue == "Left":
                dx = 8
                dy = 0
                box.move(-dx,dy)
                
        elif keyValue == "Up":
                dx = 0
                dy = 8
                box.move(dx,-dy)
                
        elif keyValue == "Down":
                dx = 0
                dy = 8
                box.move(dx,dy)

        # Down Horizontal L1   
        elif (xVal > 225 and yVal > 445) and (xVal < 325 and yVal > 445):
            box.undraw()
            box = Rectangle(Point(270,415),Point(275,420))
            box.setFill('red')
            box.draw(win)

        # Right Vertical L2   
        elif (xVal > 325 and yVal > 415) and (xVal > 325 and yVal < 440):
            box.undraw()
            box = Rectangle(Point(270,415),Point(275,420))
            box.setFill('red')
            box.draw(win)

        # Left Vertical L3
        elif (xVal < 230 and yVal > 330) and (xVal < 230 and yVal < 440):
            box.undraw()
            box = Rectangle(Point(270,415),Point(275,420))
            box.setFill('red')
            box.draw(win)

        # Left Vertical L4
        elif (xVal < 420 and yVal > 250) and (xVal < 420 and yVal < 338):
            box.undraw()
            box = Rectangle(Point(270,415),Point(275,420))
            box.setFill('red')
            box.draw(win)

        # Right Vertical L5   
        elif (xVal > 483 and yVal > 194) and (xVal > 483 and yVal < 417):
            box.undraw()
            box = Rectangle(Point(270,415),Point(275,420))
            box.setFill('red')
            box.draw(win)

        # Right Vertical L6   
        elif (xVal > 122 and yVal > 110) and (xVal > 122 and yVal < 194):
            box.undraw()
            box = Rectangle(Point(270,415),Point(275,420))
            box.setFill('red')
            box.draw(win)

        # Up Horizontal L7
        elif (xVal > 79 and yVal < 85) and (xVal < 265 and yVal < 85):
            box.undraw()
            box = Rectangle(Point(270,415),Point(275,420))
            box.setFill('red')
            box.draw(win)

        # Left Vertical L8
        elif (xVal < 80 and yVal > 85) and (xVal < 80 and yVal < 255):
            box.undraw()
            box = Rectangle(Point(270,415),Point(275,420))
            box.setFill('red')
            box.draw(win)

        # Right Vertical L9   
        elif (xVal > 284 and yVal > 50) and (xVal > 284 and yVal < 110):
            box.undraw()
            box = Rectangle(Point(270,415),Point(275,420))
            box.setFill('red')
            box.draw(win)

        # Right Vertical L10   
        elif (xVal > 320 and yVal > 424) and (xVal > 320 and yVal < 445):
            box.undraw()
            box = Rectangle(Point(270,415),Point(275,420))
            box.setFill('red')
            box.draw(win)

        # Down Horizontal The Goal   
        elif (xVal > 263 and yVal < 77) and (xVal < 288 and yVal < 77):
            box.undraw()
            level2.undraw()
            goal.undraw()
            levelThree()

def mazeGame():
    #Level 1
    drawImage(400, 250, "Level_1.png")
    
    level1 = Polygon(Point(175,450),Point(375,450),Point(375,50),Point(75,50),Point(75,100),Point(175,100))
    # level1.draw(win)
    
    box = Rectangle(Point(270,415),Point(275,420))
    box.setFill('red')
    box.draw(win)

    goal = Rectangle(Point(75,50),Point(125,100))
    # goal.setFill('red')
    # goal.draw(win)

    while True:
        keyValue = win.checkKey()
        point = box.getCenter()
        xVal = point.getX()
        yVal = point.getY()
        if keyValue == "Right":
                dx = 8
                dy = 0
                box.move(dx,dy)
                
        elif keyValue == "Left":
                dx = 8
                dy = 0
                box.move(-dx,dy)
                
        elif keyValue == "Up":
                dx = 0
                dy = 8
                box.move(dx,-dy)
                
        elif keyValue == "Down":
                dx = 0
                dy = 8
                box.move(dx,dy)
        
        # Left Vertical
        elif (xVal < 180 and yVal > 100) and (xVal < 180 and yVal < 440):
            box.undraw()
            box = Rectangle(Point(270,415),Point(275,420))
            box.setFill('red')
            box.draw(win)

        # Right Vertical    
        elif (xVal > 365 and yVal > 50) and (xVal > 365 and yVal < 440):
            box.undraw()
            box = Rectangle(Point(270,415),Point(275,420))
            box.setFill('red')
            box.draw(win)

        # Down Horizontal    
        elif (xVal > 180 and yVal > 440) and (xVal < 365 and yVal > 440):
            box.undraw()
            box = Rectangle(Point(270,415),Point(275,420))
            box.setFill('red')
            box.draw(win)

        # Up Horizontal
        elif (xVal > 75 and yVal < 50) and (xVal < 365 and yVal < 50):
            box.undraw()
            box = Rectangle(Point(270,415),Point(275,420))
            box.setFill('red')
            box.draw(win)
            
        elif (xVal > 75 and yVal > 90) and (xVal < 175 and yVal > 90):
            box.undraw()
            box = Rectangle(Point(270,415),Point(275,420))
            box.setFill('red')
            box.draw(win)
            
        elif (xVal < 125 and yVal > 50) and (xVal < 125 and yVal < 100):
            box.undraw()
            level1.undraw()
            goal.undraw()
            levelTwo()

def howToPlay():
    drawImage(400, 250, "tutorial_bg.png")
    drawImage(400, 225, "GreenFrame.png")

    drawText(400, 70, "Objectives", 25, "black", "bold")
    drawText(400, 110, "The objective of the game is to navigate through the maze to reach the end point or goal", 15, "black", "normal")
    drawText(400, 160, "The game has three stages that must be completed in sequence. Completing each stage unlocks\nthe opportunity to find a each family member - the sister in the first stage, the mother in the second,\nand the father in the third. By completing all three stages, all family members can be found.", 15, "black", "normal")
    drawText(400, 210, "Be careful not to touch any edges of the maze, or you'll have to start over from the beginning.", 15, "black", "bold italic")
    drawText(400, 250, "Controls", 25, "black", "bold")
    drawText(400, 330, "Use the arrow keys on your keyboard to move your character around the maze.\n← = LEFT\n↑ = TOP\n→ = RIGHT\n↓ = DOWN\n", 15, "black", "normal")

    drawImage(50, 350, "left.png")
    drawImage(50, 275, "right.png")
    drawImage(750, 275, "up.png")
    drawImage(750, 350, "down.png")

     # BACK BUTTON
    drawRectangle(310, 430, 490, 470, "#FFE8D5", "#96452A")
    drawText(400, 450, "BACK", 24, "#96452A", "bold")

    while True:
        coords = win.getMouse()
        x = coords.getX()
        y = coords.getY()
        if (x >= 310 and y >= 430) and (x <= 490 and y <= 470):
            mainMenu()
        break

def mainMenu():
    drawImage(400, 250, "start_screen.png")

    # PLAY BUTTON
    drawRectangle(290, 330, 510, 370, "#F77900", "#F77900")
    drawText(400, 350, "PLAY GAME", 24, "#FFE8D5", "bold")

    # TUTORIAL BUTTON
    drawRectangle(310, 380, 490, 420, "#FFE8D5", "#96452A")
    drawText(400, 400, "TUTORIAL", 20, "#96452A", "bold")

    

    while True:
        coords = win.getMouse()
        x = coords.getX()
        y = coords.getY()
        if (x >= 290 and y >= 330) and (x <= 510 and y <= 370):
            mazeGame()
        elif (x >= 310 and y >= 380) and (x <= 490 and y <= 420):
            howToPlay()
        break

mainMenu()
