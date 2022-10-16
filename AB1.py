import pygame
import math
import copy
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

cameraAngle = 90
bX, bY, bZ = 3400, 350, 5250

verticiesSuperior = (
    (3900,   0,   0),
    (3900, 400, 100),
    (2900, 400, 100),
    (2900,   0,   0),
    (3900,   0, 200),
    (3900, 400, 200),
    (2900,   0, 200),
    (2900, 400, 200),
)

verticiesInferior = (
    (3900,   0, 10500),  # 1
    (3900, 400, 10400),  # 2
    (2900, 400, 10400),  # 3
    (2900,   0, 10500),  # 4
    (3900,   0, 10300),  # 5
    (3900, 400, 10300),  # 6
    (2900,   0, 10300),  # 7
    (2900, 400, 10300),  # 8
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)


def Line(iX, iZ, fX, fZ, color=[1, 1, 1], log=False):
    glBegin(GL_LINES)
    glColor(color)

    dX = abs(fX - iX)
    dZ = abs(fZ - iZ)
    if (dX == 0 or dZ == 0):
        glVertex3f(iX, 0, iZ)
        glVertex3f(fX, 0, fZ)
    else:
        points = bresenhamLinePoints(iX, iZ, fX, fZ, dX, dZ)

        for i in range(dX):
            if log:
                print("(", points[i][0], ",", points[i][1], ")")
            glVertex3f(points[i][0], 0, points[i][1])
            glVertex3f(points[i+1][0], 0, points[i+1][1])

        if log:
            print("(", points[-1][0], ",", points[-1][1], ")")

    glEnd()
    if log:
        print()


def Bola():
    glPushMatrix()
    glColor3f(1, 1, 1)
    glTranslatef(bX, bY, bZ)
    gluSphere(gluNewQuadric(), 140, 100, 30)
    glPopMatrix()


def TraveSuperior():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticiesSuperior[vertex])
    glEnd()


def TraveInferior():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticiesInferior[vertex])
    glEnd()


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


def Circle(cX, cZ, r, nOct, octIni, color=[1, 1, 1], log=False):
    x = 0
    z = r
    d = 3 - (2*r)

    activeOctants = [(octIni+i) % 8 for i in range(nOct)]
    octantPoints = {i: list() for i in activeOctants}

    octantPoints = addOctantPoints(cX, cZ, x, z, octantPoints, activeOctants)
    while (x <= z):
        if (d > 0):
            z -= 1
            d = d + (4 * x) - (4 * z) + 10
        else:
            d = d + (4 * x) + 6
        x += 1
        octantPoints = addOctantPoints(
            cX, cZ, x, z, octantPoints, activeOctants)

    for octant in activeOctants:
        points = octantPoints[octant]

        glBegin(GL_LINES)
        glColor(color)
        for p in range(len(points)-1):
            glVertex3f(points[p][0], 0, points[p][1])
            glVertex3f(points[p+1][0], 0, points[p+1][1])
        glEnd()


def addOctantPoints(cX, cZ, x, z, octantPoints, activeOctants):
    if 0 in activeOctants:
        octantPoints[0].append([cX+x, cZ-z])  # 0
    if 1 in activeOctants:
        octantPoints[1].append([cX+z, cZ-x])  # 1
    if 2 in activeOctants:
        octantPoints[2].append([cX+z, cZ+x])  # 2
    if 3 in activeOctants:
        octantPoints[3].append([cX+x, cZ+z])  # 3
    if 4 in activeOctants:
        octantPoints[4].append([cX-x, cZ+z])  # 4
    if 5 in activeOctants:
        octantPoints[5].append([cX-z, cZ+x])  # 5
    if 6 in activeOctants:
        octantPoints[6].append([cX-z, cZ-x])  # 6
    if 7 in activeOctants:
        octantPoints[7].append([cX-x, cZ-z])  # 7
    return octantPoints


def Campo():
    # Limite Maior
    Line(0, 0, 0, 10500)
    Line(0, 10500, 6800, 10500)
    Line(6800, 10500, 6800, 0)
    Line(6800, 0, 0, 0)

    # Meio Campo
    Line(0, 5250, 6800, 5250)
    Circle(3400, 5250, 900, 8, 0)

    # Grande Área Superior
    TraveSuperior()
    Circle(3400, 1700, 600, 4, 2)
    Line(1400, 0, 1400, 1700)
    Line(5400, 0, 5400, 1700)
    Line(1400, 1700, 5400, 1700)

    # Pequena Área Superior
    Line(2500, 0, 2500, 600)
    Line(4300, 0, 4300, 600)
    Line(2500, 600, 4300, 600)

    # Grande Área Inferior
    TraveInferior()
    Circle(3400, 8800, 600, 4, 6)
    Line(1400, 10500, 1400, 8800)
    Line(5400, 10500, 5400, 8800)
    Line(1400, 8800, 5400, 8800)

    # Pequena Área Inferior
    Line(2500, 10500, 2500, 9900)
    Line(4300, 10500, 4300, 9900)
    Line(2500, 9900, 4300, 9900)
    # Line(3000,12,32,0)
    # Line(3900,12,32,4444)

    # Escanteios
    Circle(0, 0, 300, 2, 2)
    Circle(0, 10500, 300, 2, 0)
    Circle(6800, 0, 300, 2, 4)
    Circle(6800, 10500, 300, 2, 6)


def move(direction):
    global cameraAngle
    angle = copy.deepcopy(cameraAngle)
    distance = 150

    if (direction == "S"):
        angle += 180
    elif (direction == "L"):
        angle -= 90
    elif (direction == "O"):
        angle += 90

    angle = angle % 360
    xT = math.cos(math.radians(angle)) * distance
    zT = math.sin(math.radians(angle)) * distance
    glTranslatef(xT, 0, zT)


def moveBall(direction):
    global bX, bY, bZ, cameraAngle

    if (cameraAngle > 45 and cameraAngle <= 135):
        if (direction == "N"):
            bZ = between(bZ - 75, -200, 10700)
        elif (direction == "S"):
            bZ = between(bZ + 75, -200, 10700)
        elif (direction == "L"):
            bX = between(bX + 75, -200, 7000)
        elif (direction == "O"):
            bX = between(bX - 75, -200, 7000)
    elif (cameraAngle > 135 and cameraAngle <= 225):
        if (direction == "N"):
            bX = between(bX + 75, -200, 7000)
        elif (direction == "S"):
            bX = between(bX - 75, -200, 7000)
        elif (direction == "L"):
            bZ = between(bZ + 75, -200, 10700)
        elif (direction == "O"):
            bZ = between(bZ - 75, -200, 10700)
    elif (cameraAngle > 225 and cameraAngle <= 315):
        if (direction == "N"):
            bZ = between(bZ + 75, -200, 10700)
        elif (direction == "S"):
            bZ = between(bZ - 75, -200, 10700)
        elif (direction == "L"):
            bX = between(bX - 75, -200, 7000)
        elif (direction == "O"):
            bX = between(bX + 75, -200, 7000)
    elif (cameraAngle > 315 or cameraAngle <= 45):
        if (direction == "N"):
            bX = between(bX - 75, -200, 7000)
        elif (direction == "S"):
            bX = between(bX + 75, -200, 7000)
        elif (direction == "L"):
            bZ = between(bZ - 75, -200, 10700)
        elif (direction == "O"):
            bZ = between(bZ + 75, -200, 10700)


def yaw(rate):
    global cameraAngle
    cameraAngle += rate
    glRotatef(1,  0,  rate, 0)


def between(point, minP, maxP):
    if point > maxP:
        return maxP
    if point < minP:
        return minP
    return point


def handleInput(keys):
    global bX, bY, bZ

    if keys[pygame.K_i]:
        glRotatef(1,  1,  0,  0)
    if keys[pygame.K_k]:
        glRotatef(1, -1,  0,  0)
    if keys[pygame.K_j]:
        yaw(1)
    if keys[pygame.K_l]:
        yaw(-1)
    if keys[pygame.K_u]:
        glRotatef(1,  0,  0,  1)
    if keys[pygame.K_o]:
        glRotatef(1,  0,  0, -1)

    if keys[pygame.K_s]:
        move("S")
    if keys[pygame.K_w]:
        move("N")
    if keys[pygame.K_a]:
        move("O")
    if keys[pygame.K_d]:
        move("L")

    if keys[pygame.K_RIGHT]:
        moveBall("L")
    if keys[pygame.K_LEFT]:
        moveBall("O")
    if keys[pygame.K_UP]:
        moveBall("N")
    if keys[pygame.K_DOWN]:
        moveBall("S")


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(80, (display[0]/display[1]), 50, 25000)

    glTranslatef(-3400, 5250, -15000)
    glRotatef(90, 1, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        handleInput(keys)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLineWidth(1)

        Campo()
        Bola()

        pygame.display.flip()
        pygame.time.wait(10)


main()
