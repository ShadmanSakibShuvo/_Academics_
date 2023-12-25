from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

dx,dy,ds,cx,score,over,pause,zone,color1,color2,color3=200,585,0.2,200,0,False,False,-1,random.random(),random.random(),random.random()

def init():
    glClearColor(0.0,0.0,0.0,0.0)
    gluOrtho2D(0,420,0,650)

def plot(x, y):
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def MidpointLine(x1,y1,x2,y2,width=2):
    dx=abs(x2-x1)
    dy=abs(y2-y1)
    if x1<x2:
        sx=1
    else:
        sx=-1
    if y1<y2:
        sy=1
    else:
        sy=-1
    err=dx-dy
    while True:
        glPointSize(width)
        glBegin(GL_POINTS)
        glVertex2f(x1, y1)
        glEnd()
        if x1==x2 and y1==y2:
            break
        e2=2*err
        if e2>-dy:
            err=err-dy
            x1=x1+sx
        if x1==x2 and y1==y2:
            glBegin(GL_POINTS)
            glVertex2f(x1, y1)
            glEnd()
            break
        if e2<dx:
            err=err+dx
            y1=y1+sy

# def Findzone(x1, y1, x2, y2):   #not used in this version of midpoint line ; but can be used manually
#     dx,dy=x2-x1,y2-y1
#     global zone
    
#     if abs(dx) >= abs(dy):
#         if dx > 0 and dy >= 0:
#             zone = 0
#         elif dx < 0 and dy >= 0:
#             zone = 3
#         elif dx < 0 and dy < 0:
#             zone = 4
#         elif dx > 0 and dy < 0:
#             zone = 7
#     else:
#         if dx > 0 and dy >= 0:
#             zone = 1
#         elif dx < 0 and dy >= 0:
#             zone = 2
#         elif dx < 0 and dy < 0:
#             zone = 5
#         elif dx > 0 and dy < 0:
#             zone = 6
    
#     return zone

# def zone_zero_conversion(zone, x, y):
#     if zone == 0:
#         return x, y
#     elif zone == 1:
#         return y, x
#     elif zone == 2:
#         return -y, x
#     elif zone == 3:
#         return -x, y
#     elif zone == 4:
#         return -x, -y
#     elif zone == 5:
#         return -y, -x
#     elif zone == 6:
#         return -y, x
#     elif zone == 7:
#         return x, -y

# def zero_to_original_zone(zone, x, y):
#     if zone == 0:
#         return x, y
#     if zone == 1:
#         return y, x
#     if zone == 2:
#         return -y, -x
#     if zone == 3:
#         return -x, y
#     if zone == 4:
#         return -x, -y
#     if zone == 5:
#         return -y, -x
#     if zone == 6:
#         return y, -x
#     if zone == 7:
#         return x, -y

def plot(x,y):
    glVertex2f(x,y)


def DrawDiamond(x,y):
    glColor3f(0.0,0.0,0.0)
    MidpointLine(x,y+10,x+10,y+10)
    glColor3f(0.0,0.0,0.0)
    MidpointLine(x+10,y+10,x+10,y-10)
    glColor3f(0.0,0.0,0.0)
    MidpointLine(x+10,y-10,x,y-10)
    glColor3f(0.0,0.0,0.0)
    MidpointLine(x,y-10,x,y+10)

    glColor3f(color1,color2,color3)
    MidpointLine(x,y,x+5,y+10)
    glColor3f(color1,color2,color3)
    MidpointLine(x+5,y+10,x+10,y)
    glColor3f(color1,color2,color3)
    MidpointLine(x+10,y,x+5,y-10)
    glColor3f(color1,color2,color3)
    MidpointLine(x+5,y-10,x,y)

def DrawCatcher(x, y):
    glColor3f(1.0,1.0,1.0)  
    MidpointLine(x,y,x+60,y)
    MidpointLine(x+10,y-10,x+50,y-10)
    MidpointLine(x,y,x+10,y-10)
    MidpointLine(x+60,y,x+50,y-10)

def DrawButtons():
    glColor3f(0.0,0.0,1.0)  
    MidpointLine(20,620,50,620)   
    MidpointLine(20,620,35,640)
    MidpointLine(20,620,35,600)

    glColor3f(0.0,1.0,0.0) 
    MidpointLine(205,640,205,600)
    MidpointLine(215,640,215,600)

    glColor3f(1.0,0.0,0.0) 
    MidpointLine(360,640,400,600)
    MidpointLine(360,600,400,640)



def mouseListener(button,state,x,y):
    global score,over,pause,dx,dy,ds,color1,color2,color3

    if button==GLUT_LEFT_BUTTON and state==GLUT_DOWN:
        if 0<=y<=40 and 20<=x<=50:                # arrow clicked
            print("Starting Over...")
            score=0
            dy=585
            ds=1
            over=False
            pause=False
            dx=random.randint(10,360)  

        elif 205<=x<=215 and 0<=y<=40:              # Pause clicked
            pause=not pause

        elif 360<=x<=400 and 0<=y<=40:              # cross clicked
            color1,color2,color3=0.0,0.0,0.0  
            print(f"Goodbye! Final score: {score}")
            glutLeaveMainLoop()
    

def KeyboardFunc(key,x,y):
    global cx
    if key==b'\x1b':                                  # exit
        glutLeaveMainLoop()
    elif key==GLUT_KEY_LEFT and cx>10:                 #left
        cx-=15
    elif key==GLUT_KEY_RIGHT and cx<350:              #right
        cx+=15

def UpdateGame():
    global dx,dy,score,over,ds,color1,color2,color3

    if not over and not pause:
        dy-=ds

        if dy<0:
            over=True
            color1,color2,color3=0.0,0.0,0.0
            print(f"Game Over. Score: {score}")

        if hasCollided(dx,dy,cx+30,20):
            score+=1
            dy=585
            ds+=0.05
            dx=random.randint(10,350) 
            colorGenerate=random.random()
            if colorGenerate<=0.4:
                color1=colorGenerate+1
            else:
                color1=colorGenerate
            colorGenerate=random.random()
            if colorGenerate<=0.4:
                color2=colorGenerate+1
            else:
                color2=colorGenerate
            colorGenerate=random.random()
            if colorGenerate<=0.4:
                color3=colorGenerate+1
            else:
                color3=colorGenerate
            print(f"Score: {score}")

        glutPostRedisplay()

def hasCollided(dx,dy,cx,cy):
    return abs(dx-cx)<30 and abs(dy-cy)<30


def Display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,1.0,1.0)

    DrawDiamond(dx,dy)
    DrawCatcher(cx,10)
    DrawButtons()

    glFlush()

def main():
    global dx,dy,ds,cx,score,over,pause

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(420,650)
    glutInitWindowPosition(0,0)
    glutCreateWindow(b'Catch the Diamonds!')

    init()
    glutDisplayFunc(Display)
    glutSpecialFunc(KeyboardFunc)
    glutMouseFunc(mouseListener)
    glutIdleFunc(UpdateGame)

    glutMainLoop()

if __name__ == "__main__":
    main()