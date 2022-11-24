from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

def init(): #ignorable
 
  glClearColor(0, 0, 0, 0)
  glMatrixMode(GL_PROJECTION)
  

def display():
 
  glClear(GL_COLOR_BUFFER_BIT)
  glColor3f(0.5, 0.6, 0.5) #triangle color
  glBegin(GL_LINE_LOOP) 
  glVertex2f(-0.1, -0.4) #vertex 1 of triangle
  glVertex2f(-0.7, -0.4) #vertex 2 of triangle
  glVertex2f(-0.4, 0.0)  #vertex 3 of triangle
  glEnd()
  glFlush()

def main():

  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
  glutInitWindowSize(400, 400)
  glutInitWindowPosition(100, 100)
  glutCreateWindow("Triangle on black background")
  init()
  glutDisplayFunc(display)
  glutMainLoop()

main()
