import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from arquibancada import Arquibancadas
from campo import Campo
from texture import Texture
from object import Object
from bola import Bola
from trave import Traves
import motion


ballSpeed = 1.5


def updateGame(keys, ballPosition, pRed, pBlue):
    bX, bY, bZ = ballPosition

    if keys[pygame.K_UP]:
        bZ = max(bZ - ballSpeed, -1.5)
    if keys[pygame.K_DOWN]:
        bZ = min(bZ + ballSpeed, 111.5)
    if keys[pygame.K_LEFT]:
        bX = max(bX - ballSpeed, -1.5)
    if keys[pygame.K_RIGHT]:
        bX = min(bX + ballSpeed, 69.5)

    if (bX >= 30 and bX <= 38):
        if (bZ >= -1.5 and bZ <= 0):
            pBlue += 1
            bX, bZ = 34, 52.5
        elif (bZ >= 110 and bZ <= 111.5):
            pRed += 1
            bX, bZ = 34, 52.5
    return ((bX, bY, bZ), pRed, pBlue)


def main():
    global surfaces

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(70, (display[0]/display[1]), 0.1, 500)

    glMatrixMode(GL_MODELVIEW)

    glLight(GL_LIGHT0, GL_POSITION,  (5, 5, 5, 1))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0, 0, 0, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))

    glEnable(GL_TEXTURE_2D)
    glEnable(GL_DEPTH_TEST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_COMBINE)

    textDeserto = Texture("assets/areia.jpg", 100)
    textCeu = Texture("assets/ceu.jpg", 0.01)

    textArq = Texture("assets/concreto.jpg", 0.2)
    textCampo = Texture("assets/campo.png", 0.05)
    textBola = Texture("assets/bola.jpg", 0.5)
    textRede = Texture("assets/rede.jpg", 0.5)

    ballPosition = (34, 1, 60)
    pRed = 0
    pBlue = 0

    glTranslatef(-43, 55, -160)
    glRotatef(90, 1, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        motion.handler(keys)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # glDisable(GL_DEPTH_TEST)
        Object(textDeserto, (600, 1, 400), (-300, -1, -200), 0.1)
        Object(textCeu, (600, 300, 0.1), (-300, -1, -200), 0.1)
        Object(textCeu, (600, 300, 0.1), (-300, -1, 200), 0.1)
        Object(textCeu, (0.1, 300, 400), (-300, -1, -200), 0.1)
        Object(textCeu, (0.1, 300, 400), (300, -1, -200), 0.1)
        Object(textCeu, (600, 1, 400), (-300, 300, -200), 0.1)
        # glEnable(GL_DEPTH_TEST)

        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

        Campo(textCampo)
        Arquibancadas(textArq)
        Traves(textRede)

        ballPosition, pRed, pBlue = updateGame(
            keys, ballPosition, pRed, pBlue)
        Bola(textBola, ballPosition)

        glDisable(GL_LIGHT0)
        glDisable(GL_LIGHTING)
        glDisable(GL_COLOR_MATERIAL)

        pygame.display.flip()


if __name__ == "__main__":
    main()
