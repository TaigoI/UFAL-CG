from OpenGL.GL import glRotatef, glTranslatef
import pygame

translate = 5
rotate = 2


def handler(keys):
    if keys[pygame.K_i]:
        glRotatef(rotate, +1, +0, +0)
    if keys[pygame.K_k]:
        glRotatef(rotate, -1, +0, +0)
    if keys[pygame.K_j]:
        glRotatef(rotate, +0, +1, +0)
    if keys[pygame.K_l]:
        glRotatef(rotate, +0, -1, +0)
    if keys[pygame.K_u]:
        glRotatef(rotate, +0, +0, +1)
    if keys[pygame.K_o]:
        glRotatef(rotate, +0, +0, -1)

    if keys[pygame.K_d]:
        glTranslatef(-1*translate, +0, +0)
    if keys[pygame.K_a]:
        glTranslatef(+1*translate, +0, +0)
    if keys[pygame.K_q]:
        glTranslatef(+0, -1*translate, +0)
    if keys[pygame.K_e]:
        glTranslatef(+0, +1*translate, +0)
    if keys[pygame.K_s]:
        glTranslatef(+0, +0, -1*translate)
    if keys[pygame.K_w]:
        glTranslatef(+0, +0, +1*translate)


if __name__ == "__main__":
    import main
    main.main()
