from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys

def display() :
    glClearColor(0.5,0.1,0.5,0.2)
    #1111 for white screen,0000 for black screen
    glClear(GL_COLOR_BUFFER_BIT)
    glFlush()

def init() :
     glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
     glutInitWindowSize(500,500)
     glutInitWindowPosition(0,0)
     glutCreateWindow("Color_window")

def main():
    glutInit(sys.argv)   
    init()
    glutDisplayFunc(display)
    glutMainLoop()

main()  

