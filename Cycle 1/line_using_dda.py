from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-300, 300, -300, 300)
def plotLine(x1, y1, x2, y2): #function to plot line
    deltaX = x2 - x1
    deltaY = y2 - y1
    steps = 0
    if (abs(deltaX) > abs(deltaY)):  #
         steps = abs(deltaX)         # checking to choose which value as steps
    else:                            #
        steps = abs(deltaY)          #
    Xincrement = deltaX / steps
    Yincrement = deltaY / steps
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(10.0)
    glBegin(GL_POINTS)
    for step in range(1, steps + 1):
        glVertex2f(round(x1), round(y1)) #
        x1 = x1 + Xincrement             # looping to print points one by one
        y1 = y1 + Yincrement             #
    glEnd()
    glFlush()

def main():
     print ("Enter following coordinates for a line :")
     x1 = int(input("Enter x1: "))
     y1 = int(input("Enter y1: "))
     x2 = int(input("Enter x2: "))
     y2 = int(input("Enter y2: "))
     glutInit(sys.argv)
     glutInitDisplayMode(GLUT_RGB)
     glutInitWindowSize(500, 500)
     glutInitWindowPosition(0, 0)
     glutCreateWindow("Plot Line using DDA")
     glutDisplayFunc(lambda: plotLine(x1, y1, x2, y2)) #calling the line drawing function
     glutIdleFunc(lambda: plotLine(x1, y1, x2, y2))
     init()
     glutMainLoop()
main()