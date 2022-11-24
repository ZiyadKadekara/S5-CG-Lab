from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

def init():

  glClearColor(0, 0, 0, 0)
  glMatrixMode(GL_PROJECTION)

def display():

  glClear(GL_COLOR_BUFFER_BIT)
  glColor3f(0.5, 0.6, 0.5) #color of lines of the rectangle
  glBegin(GL_LINE_LOOP) #creating rectanlge using loop of lines
  glVertex2f(-0.1, 0.1) #vertex 1
  glVertex2f(0.8, 0.1)  #vertex 2
  glVertex2f(0.8, -0.4) #vertex 3
  glVertex2f(-0.1, -0.4) #vertex 4
  glEnd()
  glFlush()

def main():

  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
  glutInitWindowSize(400, 400)
  glutInitWindowPosition(100, 100)
  glutCreateWindow("Rectangle on black background")
  init()
  glutDisplayFunc(display)
  glutMainLoop()

main()
