from OpenGL.GL import *
from object import Object

# Fonte: adaptado do RogueBasin
# http://www.roguebasin.com/index.php/Bresenham%27s_Line_Algorithm#Python
def Line(iX, iZ, fX, fZ, color=[1, 1, 1], log=False):
    glBegin(GL_LINES)
    #glLineWidth(7)
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
            glVertex3f(points[i][0], 0.15, points[i][1])
            glVertex3f(points[i+1][0], 0.15, points[i+1][1])

        if log:
            print("(", points[-1][0], ",", points[-1][1], ")")

    glEnd()
    if log:
        print()


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


# Fonte: adaptado da versão Java do JavaTPoint
# https://www.javatpoint.com/computer-graphics-bresenhams-circle-algorithm
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
        #glLineWidth(7)
        glColor(color)
        for p in range(len(points)-1):
            glVertex3f(points[p][0], 0.15, points[p][1])
            glVertex3f(points[p+1][0], 0.15, points[p+1][1])
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


def linhasCampo():
    # Limite Maior
    Line(0, 0, 0, 110)
    Line(0, 110, 68, 110)
    Line(68, 110, 68, 0)
    Line(68, 0, 0, 0)
    # Meio Campo
    Line(0, 55, 68, 55)
    Circle(34, 55, 9, 8, 0)

    # Grande Área Superior
    Circle(34, 17, 6, 4, 2)
    Line(14, 0, 14, 17)
    Line(54, 0, 54, 17)
    Line(14, 17, 54, 17)

    # Pequena Área Superior
    Line(25, 0, 25, 6)
    Line(43, 0, 43, 6)
    Line(25, 6, 43, 6)

    # Grande Área Inferior
    Circle(34, 93, 6, 4, 6)
    Line(14, 110, 14, 93)
    Line(54, 110, 54, 93)
    Line(14, 93, 54, 93)

    # Pequena Área Inferior
    Line(25, 110, 25, 104)
    Line(43, 110, 43, 104)
    Line(25, 104, 43, 104)
    # Line(3000,12,32,0)
    # Line(3900,12,32,4444)

    # Escanteios
    Circle(0, 0, 3, 2, 2)
    Circle(0, 110, 3, 2, 0)
    Circle(68, 0, 3, 2, 4)
    Circle(68, 110, 3, 2, 6)

class Campo:
    def __init__(self, texture):
        Object(texture, (68, 0.1, 110))
        glDisable(GL_DEPTH_TEST)
        linhasCampo()
        glEnable(GL_DEPTH_TEST)


if __name__ == "__main__":
    import main
    main.main()
