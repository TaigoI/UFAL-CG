import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )


def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def Line(iX, iZ, fX, fZ, color=[1,1,1], log=False):
    glBegin(GL_LINES)
    glColor(color)
    
    dX = abs(fX - iX)
    dZ = abs(fZ - iZ)
    if(dX == 0 or dZ == 0):
        glVertex3f(iX, 0, iZ)
        glVertex3f(fX, 0, fZ)
        glEnd()
        return

    m_new = 2 * dZ
    slope_error_new = m_new - dX
    z = iZ
    for x in range(iX, fX+1):
        if log: print("(", x, ",", z, ")")
        glVertex3f(x, 0, z)
        if(x != iX and x != fX):
            glVertex3f(x, 0, z)
        slope_error_new = slope_error_new + m_new
        if (slope_error_new >= 0):
            z = z+1
            slope_error_new = slope_error_new - 2 * dX
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.01, 50.0)

    glTranslatef(0, -2, -7)
    glRotatef(90, 1, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
        mX, mY, mZ = 0, 0, 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            mX += 0.1
        if keys[pygame.K_d]:
            mX -= 0.1
        if keys[pygame.K_e]:
            mY -= 0.1
        if keys[pygame.K_q]:
            mY += 0.1   
        if keys[pygame.K_w]:
            mZ -= 0.1
        if keys[pygame.K_s]:
            mZ += 0.1
        glTranslatef(mX, mY, mZ)

        if keys[pygame.K_RIGHT]:
            glRotatef(1, 0, -1, 0)
        if keys[pygame.K_LEFT]:
            glRotatef(1, 0, 1, 0)
        if keys[pygame.K_UP]:
            glRotatef(1, 1, 0, 0)
        if keys[pygame.K_DOWN]:
            glRotatef(1, -1, 0, 0)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Line(0,0,2,0, [1,0,0]) #X (vermelho)
        Line(0,0,0,2, [0,1,0]) #Z (verde)

        Line(0,0,0,1)
        Line(0,1,1,1)
        Line(1,1,1,0)
        Line(1,0,0,0)

        Line(0,0,1,1, [1,1,0])
        Line(1,0,0,1, [0,1,0], log=True)
        pygame.display.flip()
        pygame.time.wait(10)

main()