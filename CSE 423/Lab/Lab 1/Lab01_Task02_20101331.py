from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

W_Width,W_Height=500,500

points=[]
speed=1
frozen=False

class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.color=(random.random(),random.random(),random.random())
        self.blinking=False

def convert_coordinate(x,y):
    global W_Width,W_Height
    a=x-(W_Width/2)
    b=(W_Height/2)-y 
    return a,b

def draw_points():
    glPointSize(5)
    glBegin(GL_POINTS)
    for p in points:
        if p.blinking:
            glColor3f(0,0,0)
        else:
            glColor3f(*p.color)
        glVertex2f(p.x,p.y)
    glEnd()

def blink_points(value):
    for p in points:
        p.blinking=not p.blinking
    glutTimerFunc(1000,blink_points,0)
    glutPostRedisplay()

def keyboardListener(key,x,y):
    global frozen
    if key==b' ' and frozen==False:
        frozen = True
    else:
        frozen = False

def specialKeyListener(key,x,y):
    global speed,frozen
    if key==GLUT_KEY_UP:
        speed+=1
    elif key==GLUT_KEY_DOWN:
        speed-=1

def mouseListener(button,state,x,y):
    global points,frozen
    if button==GLUT_RIGHT_BUTTON:
        c_X,c_Y=convert_coordinate(x,y)
        new_point=point(c_X,c_Y)
        points.append(new_point)

        new_direction=point(random.choice([-1, 1]),random.choice([-1, 1]))
        new_point.x+=new_direction.x
        new_point.y+=new_direction.y

    if button==GLUT_LEFT_BUTTON:
        blink_points(0)

    glutPostRedisplay()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0,0,0,0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,0,200, 0,0,0, 0,1,0)
    glMatrixMode(GL_MODELVIEW)
    draw_points()

    glutSwapBuffers()

def animate(value):
    global frozen
    if frozen!=True:
        for p in points:
            p.x+=random.choice([-1, 1])*speed
            p.y+=random.choice([-1, 1])*speed

    glutTimerFunc(100, animate, 0)
    glutPostRedisplay()

def init():
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(104, 1, 1, 1000.0)

glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)

wind = glutCreateWindow(b"Building the Amazing Box")
init()

glutDisplayFunc(display)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)
glutTimerFunc(100, animate, 0)

glutMainLoop()
