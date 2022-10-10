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
    else:
        points = bresenhamLinePoints(iX, iZ, fX, fZ, dX, dZ)
            
        for i in range(dX):
            if log: print("(",points[i][0],",",points[i][1],")")
            glVertex3f(points[i][0], 0, points[i][1])
            glVertex3f(points[i+1][0], 0, points[i+1][1])
        
        if log: print("(",points[-1][0],",",points[-1][1],")")
    
    glEnd()
    if log: print()

def bresenhamLinePoints(iX, iZ, fX, fZ, dX, dZ):
    dX = fX - iX
    dZ = fZ - iZ

    # Determine how steep the line is
    is_steep = abs(dZ) > abs(dX)

    # Rotate line
    if is_steep:
        iX, iZ = iZ, iX
        fX, fZ = fZ, fX

    # Swap start and end points if necessary and store swap state
    swapped = False
    if iX > fX:
        iX, fX = fX, iX
        iZ, fZ = fZ, iZ
        swapped = True

    # Recalculate differentials
    dX = fX - iX
    dZ = fZ - iZ

    # Calculate error
    error = int(dX / 2.0)
    ystep = 1 if iZ < fZ else -1

    # Iterate over bounding box generating points between start and end
    y = iZ
    points = []
    for x in range(iX, fX + 1):
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
        error -= abs(dZ)
        if error < 0:
            y += ystep
            error += dX

    # Reverse the list if the coordinates were swapped
    if swapped:
        points.reverse()
    return points

def Campo():
    #Limite Maior
    Line(0,0,0,105)
    Line(0,105,68,105)
    Line(68,105,68,0)
    Line(68,0,0,0)

    #Meio Campo
    Line(0,52.5,68,52.5)
    
    #Grande Área Superior
    Line(14,0,14,17)
    Line(54,0,54,17)
    Line(14,17,54,17)

    #Pequena Área Superior
    Line(25,0,25,6)
    Line(43,0,43,6)
    Line(25,6,43,6)

    #Grande Área Inferior
    Line(14,105,14,88)
    Line(54,105,54,88)
    Line(14,88,54,88)

    #Pequena Área Inferior
    Line(25,105,25,99)
    Line(43,105,43,99)
    Line(25,99,43,99)

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.01, 200.0)

    glTranslatef(-35, 53, -150)
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
        glLineWidth(3)
        Campo()

        pygame.display.flip()
        pygame.time.wait(10)

main()