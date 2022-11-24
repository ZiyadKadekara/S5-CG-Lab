from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

def init2D(r,g,b):

    glClearColor(r, g, b, 0.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0.0, 200.0, 0.0, 200.0)

def display():

  glClear(GL_COLOR_BUFFER_BIT)
  glColor3f(0.0, 1.0, 0.0) #color of the line
  glBegin(GL_LINES) #for line
  glVertex2i(100, 100) #inital point vertex
  glVertex2i(50, 50) #final point vertex
  glEnd()
  glFlush()

def main():

  glutInit(sys.argv) #initialize GLUT
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
  glutInitWindowSize(500, 500)
  glutInitWindowPosition(0,0)
  glutCreateWindow("line")
  init2D(0.0, 0.0, 0.0)
  glutDisplayFunc(display)
  glutMainLoop()

main()