from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
#from Rendering2D import *
from snake_apple import *
import random


width = 1000
height = 750

FPS = 10.0

apples = []
snake = Snake()

def add_apple():
	apple = Apple()
	apples.append(apple)


def buttons(key, x, y):
	if(key == GLUT_KEY_UP):
		snake.change_direction(0, 16)
	elif(key == GLUT_KEY_DOWN):
		snake.change_direction(0, -16)
	elif(key == GLUT_KEY_LEFT):
		snake.change_direction(-16, 0)
	elif(key == GLUT_KEY_RIGHT):
		snake.change_direction(16, 0)

	#glutPostRedisplay()


def update(value):
	global FPS
	glutPostRedisplay()
	glutTimerFunc(int(1000/FPS), update, int(0))

def showScreen():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()
	iterate()

	if(random.randint(0, 1000) % 40  == 0 and len(apples) < 20):
		add_apple()




	snake.move_forward()
	snake.wrap_edges()
	snake.check_collision()

	for a in apples:
		eaten = snake.check_eaten(a)
		if(eaten == True):
			index = apples.index(a)
			snake.add(a.pos.x, a.pos.y)
			apples.pop(index)
		a.show()

	snake.show()




	glutSwapBuffers()

def iterate():
	glViewport(0, 0, width, height)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()

def main():
	glutInit()
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
	glutInitWindowSize(width, height)
	glutInitWindowPosition(0, 0)
	wind = glutCreateWindow("2D Rendering Engine | Ryan's OpenGL Practice")
	glutDisplayFunc(showScreen)
	glutSpecialFunc(buttons)
	#glutIdleFunc(showScreen)
	glutTimerFunc(int(0), update, int(0))
	glutMainLoop()


main()


