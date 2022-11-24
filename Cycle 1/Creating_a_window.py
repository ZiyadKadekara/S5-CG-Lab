from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys #provides functions to manipulate different parts of the Python runtime environment

def display() :
    glClearColor(0.5,0.1,0.5,0.2) #Add color to your window background
    #1111 for white screen,0000 for black screen
    glClear(GL_COLOR_BUFFER_BIT)
    glFlush()

def init() :
     glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
     glutInitWindowSize(500,500)      #size of your window
     glutInitWindowPosition(0,0)      #position of your window
     glutCreateWindow("Color_window") #name of your window

def main():
    glutInit(sys.argv)   
    init() #calling init() function
    glutDisplayFunc(display) #dispalying "display" function
    glutMainLoop()  #looping for viewing the window until you close

main()  

