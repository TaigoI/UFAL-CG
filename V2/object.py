from OpenGL.GL import *
from numpy import multiply

verticies = ((1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 0, 0),
             (1, 0, 1), (1, 1, 1), (0, 0, 1), (0, 1, 1))

surfaces = ((0, 1, 2, 3), (3, 2, 7, 6), (6, 7, 5, 4),
            (4, 5, 1, 0), (1, 5, 7, 2), (4, 0, 3, 6))

normals = ((0.1, 0.1, -1.0), (-1.0, 0.1, 0.1), (0.1, 0.1, 0.1),
           (0.1, 0.1, 0.1), (0.1, 1.0, 0.1), (0.1, -1.0, 0.1))

edges = ((0, 1), (0, 3), (0, 4), (2, 1), (2, 3), (2, 7),
         (6, 3), (6, 4), (6, 7), (5, 1), (5, 4), (5, 7))

textureMap = ((0.0, 0.0,), (1.0, 0.0,), (1.0, 1.0,), (0.0, 1.0))


class Object:
    def __init__(self, texture, size=(1, 1, 1), position=(0, 0, 0), line=0, color=(1, 1, 1)):
        glPushMatrix()
        glTranslatef(*position)

        texture.Bind()
        glBegin(GL_QUADS)
        for iS, surface in enumerate(surfaces):
            glNormal3fv(normals[iS])
            for iV, vertex in enumerate(surface):
                glColor3fv(color)
                tm = multiply(
                    textureMap[iV], (size[2]*texture.scale, size[0]*texture.scale))
                glTexCoord2fv(tm)
                glVertex3fv(multiply(verticies[vertex], size))
        glEnd()
        texture.UnBind()

        if line > 0:
            glLineWidth(line)
            glBegin(GL_LINES)
            for edge in edges:
                for vertex in edge:
                    glColor3fv(color)
                    glVertex3fv(multiply(verticies[vertex], size))
            glEnd()

        glPopMatrix()


if __name__ == "__main__":
    import main
    main.main()
