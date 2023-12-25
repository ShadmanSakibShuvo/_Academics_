from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class GrowingCircle:
    def __init__(self,center,radius,speed):
        self.center,self.radius,self.speed=center,radius,speed

    def draw(self):
        glColor3f(1.0,0.0,0.0)
        self.midpointCircle()

    def grow(self):
        self.radius+=self.speed

    def plot(self,x,y):
        glPointSize(5)
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glEnd()

    def isInDisplay(self,x_min,x_max,y_min,y_max):
        return (self.center[0]-self.radius>=x_min and self.center[0]+self.radius<=x_max
                and self.center[1]-self.radius>=y_min and self.center[1]+self.radius<=y_max)

    def midpointCircle(self):
        x,y,r=self.center[0],self.center[1],int(self.radius)
        p,x,y=1-r,0,r
        while x<=y:
            x+=1
            if p<=0:
                p=p+2*x+1
            else:
                y-=1
                p=p+2*x-2*y+1
            self.plotCircle(x,y)
            self.plotCircle(x,-y)
            self.plotCircle(-x,y)
            self.plotCircle(-x,-y)
            self.plotCircle(y,x)
            self.plotCircle(-y,x)
            self.plotCircle(y,-x)
            self.plotCircle(-y,-x)

    def plotCircle(self,x,y):
        zone=Findzone(self.center[0],self.center[1],x,y)
        original_zone=zone
        x0,y0=zone_zero_conversion(zone,x,y)
        x01,y01=zero_to_original_zone(original_zone,x0,y0)
        self.plot(x01+self.center[0],y01+self.center[1])
        if x!=y:
            self.plot(y01+self.center[0],x01+self.center[1])

def Findzone(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1

    if abs(dx)>abs(dy):
        if dx>=0 and dy>=0:
            return 0
        elif dx<0 and dy>=0:
            return 3
        elif dx<0 and dy<0:
            return 4
        else:
            return 7
    else:
        if dx>=0 and dy>=0:
            return 1
        elif dx<0 and dy>=0:
            return 2
        elif dx<0 and dy<0:
            return 5
        else:
            return 6

def zone_zero_conversion(zone,x,y):
    if zone==0:
        return x,y
    elif zone==1:
        return y,x
    elif zone==2:
        return -y,x
    elif zone==3:
        return -x,y
    elif zone == 4:
        return -x,-y
    elif zone == 5:
        return -y,-x
    elif zone == 6:
        return y,-x
    else:
        return x,-y  

def zero_to_original_zone(zone,x,y):
    if zone==0:
        return x,y
    elif zone==1:
        return y,x
    elif zone==2:
        return -y,x
    elif zone==3:
        return -x,y
    elif zone==4:
        return -x,-y
    elif zone==5:
        return -y,-x
    elif zone==6:
        return y,-x
    else:
        return x,-y

def init():
    glClearColor(0.0,0.0,0.0,0.0)
    gluOrtho2D(0,600,0,600)

growing_circles,pause,speed=[],False,0.5

def create_circle(x,y):
    growing_circles.append(GrowingCircle((x,y),0,speed))

def draw_growing_circles():
    for circle in growing_circles:
        circle.draw()

def update_growing_circles():
    global speed
    if not pause:
        for circle in growing_circles:
            circle.speed=speed
            circle.grow()
        growing_circles[:]=[circle for circle in growing_circles if circle.isInDisplay(0,599,0,599)]
        glutPostRedisplay()

def Display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    draw_growing_circles()
    glutSwapBuffers()

def keyboardFunc(key,x,y):
    global pause,speed
    if key==GLUT_KEY_UP:
        pause=not pause
    elif key==GLUT_KEY_LEFT:
        speed+=0.05
    elif key==GLUT_KEY_RIGHT and speed>0:
        speed-=0.05

def mouseListener(button,state,x,y):
    if button==GLUT_LEFT_BUTTON and state==GLUT_DOWN:
        create_circle(x,599-y)
        glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600,600)
    glutInitWindowPosition(0,0)
    glutCreateWindow(b'Growing Circles')

    init()
    glutDisplayFunc(Display)
    glutIdleFunc(update_growing_circles)
    glutMouseFunc(mouseListener)
    glutSpecialFunc(keyboardFunc)

    glutMainLoop()

if __name__ == "__main__":
    main()