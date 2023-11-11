from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

diamond_x = 200
diamond_y = 600
diamond_speed = 0.1
catcher_x = 200
score = 0
game_over = False
game_paused = False
Zone = -1
color=random.random()

def FindZone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    global Zone
    
    if abs(dx) >= abs(dy):
        if dx > 0 and dy >= 0:
            Zone = 0
        elif dx < 0 and dy >= 0:
            Zone = 3
        elif dx < 0 and dy < 0:
            Zone = 4
        elif dx > 0 and dy < 0:
            Zone = 7
    else:
        if dx > 0 and dy >= 0:
            Zone = 1
        elif dx < 0 and dy >= 0:
            Zone = 2
        elif dx < 0 and dy < 0:
            Zone = 5
        elif dx > 0 and dy < 0:
            Zone = 6
    
    return Zone

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(0, 420, 0, 650)

def plot(x, y):
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def ZoneZeroConversion(Zone, x, y):
    if Zone == 0:
        return x, y
    elif Zone == 1:
        return y, x
    elif Zone == 2:
        return -y, x
    elif Zone == 3:
        return -x, y
    elif Zone == 4:
        return -x, -y
    elif Zone == 5:
        return -y, -x
    elif Zone == 6:
        return -y, x
    elif Zone == 7:
        return x, -y

def zero_to_original_zone(Zone, x, y):
    if Zone == 0:
        return x, y
    if Zone == 1:
        return y, x
    if Zone == 2:
        return -y, -x
    if Zone == 3:
        return -x, y
    if Zone == 4:
        return -x, -y
    if Zone == 5:
        return -y, -x
    if Zone == 6:
        return y, -x
    if Zone == 7:
        return x, -y

def MidpointLine(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx
    incNE = 2 * (dy - dx)
    incE = 2 * dy
    incSE = 2 * (dy + dx)
    x, y = x1, y1
    Zone = FindZone(x1, y1, x2, y2)

    while x < x2:
        if d <= 0:
            d += incE
            x += 1
        else:
            d += incNE
            x += 1
            y += 1

        x0, y0 = ZoneZeroConversion(Zone, x, y)
        x01, y01 = zero_to_original_zone(Zone, x0, y0)
        plot(x01, y01)



        

def DrawDiamond(x, y):
    glColor3f(0.0,0.0,0.0)
    MidpointLine(x, y+10, x+10, y+10)
    glColor3f(0.0,0.0,0.0)
    MidpointLine(x+10, y+10, x+10, y-10)
    glColor3f(0.0,0.0,0.0)
    MidpointLine(x+10, y-10, x, y-10)
    glColor3f(0.0,0.0,0.0)
    MidpointLine(x, y-10, x, y+10)
    glColor3f(color,color,color)
    MidpointLine(x, y, x+5, y+10)
    glColor3f(color,color,color)
    MidpointLine(x+5, y+10, x+10, y)
    glColor3f(color,color,color)
    MidpointLine(x+10, y, x+5, y-10)
    glColor3f(color,color,color)
    MidpointLine(x+5, y-10, x, y)

def DrawCatcher(x, y):
    glColor3f(1.0, 1.0, 1.0)  
    MidpointLine(x, y, x+60, y)
    MidpointLine(x+10, y-10, x+50, y-10)
    MidpointLine(x, y,x+10, y-10)
    MidpointLine(x+60, y,  x+50, y-10)

def DrawButtons():
    
    glColor3f(0.0, 0.0, 1.0)  
    MidpointLine(20, 620, 50, 620)
    MidpointLine(20, 620, 35, 640)
    MidpointLine(20, 620, 35, 600)
    glColor3f(0.0, 0.0, 0.0)  #arrow
    MidpointLine(20, 600, 35, 600)
    MidpointLine(35,600 , 35,640 )
    MidpointLine(35,640 ,20 ,640 )
    MidpointLine(20,640 ,20 ,600 )

    glColor3f(0.0, 1.0, 0.0) 
    MidpointLine(205, 640, 205, 600)
    MidpointLine(215, 640, 215, 600)
    glColor3f(0.0, 0.0, 0.0)  #pause
    MidpointLine(205, 640, 215, 640)
    MidpointLine(205, 600, 215, 600)
    
    glColor3f(1.0, 0.0, 0.0) 
    MidpointLine(360, 640, 400, 600)
    MidpointLine(360, 600, 400, 640)
    glColor3f(0.0, 0.0, 0.0)  #cross
    MidpointLine(360, 640, 400, 640)
    MidpointLine(400, 640, 400, 600)
    MidpointLine(400, 600, 360, 600)
    MidpointLine(360, 600, 360, 640)


def mouseListener(button, state, x, y):
    global score, game_over, game_paused, diamond_y, diamond_speed,color

    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if 0 <= y <= 40 and 20 <= x <= 50:  # arrow clicked
            print("Starting Over...")
            score = 0
            diamond_y = 600
            diamond_speed = 1
            game_over = False
            game_paused = False
            diamond_x = random.randint(10, 390)  

        elif 205 <= x <= 215 and 0 <= y <= 40:  # Pause clicked
            game_paused = not game_paused

        elif 360 <= x <= 400 and 0 <= y <= 40:  # cross clicked
            color=0.0  
            print(f"Goodbye! Final score: {score}")
            glutLeaveMainLoop()
    

def KeyboardFunc(key, x, y):
    global catcher_x
    if key == b'\x1b':  # exit
        glutLeaveMainLoop()
    elif key==GLUT_KEY_LEFT and catcher_x > 10:  #left
        catcher_x -= 10
    elif key==GLUT_KEY_RIGHT and catcher_x < 350:  #right
        catcher_x += 10
    else:
        catcher_x=catcher_x

def UpdateGame():
    global diamond_x, diamond_y, score, game_over, diamond_speed,color

    if not game_over and not game_paused:
        diamond_y -= diamond_speed

        if diamond_y <= 0:
            game_over = True
            color=0.0
            print(f"Game Over. Score: {score}")

        if CheckCollision(diamond_x, diamond_y, catcher_x, 10):
            score += 1
            diamond_y = 600
            diamond_speed += 0.05
            diamond_x = random.randint(10, 410) 
            color=random.random()
            print(f"Score: {score}")

        glutPostRedisplay()

def CheckCollision(diamond_x, diamond_y, catcher_x, catcher_y):
    return abs(diamond_x - catcher_x) < 50 and abs(diamond_y - catcher_y) < 10


def Display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)

    DrawDiamond(diamond_x, diamond_y)
    DrawCatcher(catcher_x,10)
    DrawButtons()

    glFlush()

def main():
    global diamond_x, diamond_y, diamond_speed, catcher_x, score, game_over, game_paused

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(420, 650)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b'Catch the Diamonds!')

    init()
    glutDisplayFunc(Display)
    glutSpecialFunc(KeyboardFunc)
    glutMouseFunc(mouseListener)
    glutIdleFunc(UpdateGame)

    glutMainLoop()

if __name__ == "__main__":
    main()