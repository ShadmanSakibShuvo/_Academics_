from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

rain_direction_angle=0.0
skin_color=0

def draw_filled_circle(x, y, radius):  #some sort of midpoint circle(collected)
    num_segments = 100                 #it could be done by just using a GL_point without making a ball point
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for i in range(num_segments+1):
        theta = 2.0 * math.pi * i / num_segments
        dx = radius * math.cos(theta)
        dy = radius * math.sin(theta)
        glVertex2f(x + dx, y + dy)
    glEnd()

def draw_line(x1, y1, x2, y2,width):
    glLineWidth(width)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

def draw_raindrop(x,y,length):
    glLineWidth(1)
    glBegin(GL_LINES)
    glVertex2f(x,y)
    glVertex2f(x,y-length)
    glEnd()

def draw_triangle(x1, y1, x2, y2, x3, y3):
    glLineWidth(7)
    glBegin(GL_TRIANGLES)  #or can be drawn using GL_LINES to make the triangle hollow
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glEnd()

def iterate():
    glViewport(0,0,1920,1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0,1920,0.0,1080,0.0,1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def specialKeyListener(key, x, y):
    global rain_direction_angle
    global skin_color

    if key == GLUT_KEY_LEFT:
        rain_direction_angle+=5 
    elif key == GLUT_KEY_RIGHT:
        rain_direction_angle-=5 
    elif key == b'n':
        skin_color=skin_color+0.2 
    elif key == b'd':
        skin_color=skin_color-0.2
    else:
        None

def showScreen():
    global rain_direction_angle
    global skin_color

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    glColor3f(1.0, 1.0, 1.0)
    c=0
    for i in range(0,620,20):
        for j in range(720,350,-20):
            if c%2==0:
                s=10
            else:
                s=5
            draw_raindrop(i,j,s)
            angle = rain_direction_angle * math.pi/180
            x_adjusted = i + (380 - j) * (angle)
            y_adjusted = j - (380 - j) * (angle)
            draw_raindrop(int(x_adjusted),int(y_adjusted),s)
            c+=1
    c+=1

    glClearColor(0, 0, 0 + skin_color, 1)

    glColor3f(0.0, 1.0, 0.0)
    draw_line(150, 150, 450, 150, 5)
    draw_line(450, 150, 450, 380, 5)
    draw_line(450, 380, 150, 380, 5)
    draw_line(150, 380, 150, 150, 5)

    glColor3f(0.0, 1.0, 0.0)
    draw_triangle(124, 385, 300, 490, 470, 385)

    glColor3f(0.0, 0.0, 1.0)
    draw_line(220, 150, 220, 250, 2)
    draw_line(280, 150, 280, 250, 2)
    draw_line(220, 250, 280, 250, 2)

    glColor3f(0.0, 0.0, 1.0)
    draw_line(355, 310, 375, 310, 2)
    draw_line(355, 310, 355, 330, 2)
    draw_line(355, 330, 375, 330, 2)
    draw_line(375, 310, 375, 330, 2)

    glColor3f(0.0, 0.0, 1.0)
    draw_line(355, 320, 375, 320, 1)
    draw_line(365, 310, 365, 330, 1)

    glColor3f(1.0, 0.0, 0.0)
    draw_filled_circle(270, 200, 2)

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(620,720)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Building a House in Rainfall")

glutDisplayFunc(showScreen)
glutSpecialFunc(specialKeyListener)

glutMainLoop()
