from OpenGL.GL import *
from OpenGL.GLU import *
from texture import Texture


class Bola:
    def __init__(self, texture: Texture, position):
        glPushMatrix()
        glTranslatef(*position)

        glColor3f(1, 1, 1)
        gluSphere(gluNewQuadric(), 0.7, 50, 20)
        glPopMatrix()


if __name__ == "__main__":
    import main
    main.main()
