from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*


def init2D(r,g,b): #a function you can ignore if it find difficult at the beginning
      glClearColor(r,g,b,0.0)
      glMatrixMode(GL_PROJECTION)
      gluOrtho2D(0,300.0,0.0,300.0)

def display():
      glColor3f(1.0,1.0,1.0) #change color of the point
      glPointSize(10) #define size of the point
      glBegin(GL_POINTS)
      glVertex2i(100,100) #draw point at position 100 100
      glEnd()
      glFlush() #flushing

def main():

  glutInit(sys.argv) #initialize GLUT
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
  glutInitWindowSize(1920, 1080)
  glutInitWindowPosition(0,0)
  glutCreateWindow("Drawing a point")
  glutDisplayFunc(display)
  init2D(0.0, 0.0, 0.0) #change values to change background color
  glutMainLoop()  #routine

main()