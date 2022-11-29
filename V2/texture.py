import pygame
from OpenGL.GL import *


class Texture:

    def __init__(self, path, scale=1):
        self.textId = 0
        self.path = path
        self.scale = scale

        image = pygame.image.load(self.path).convert_alpha()
        if image:
            image_width, image_height = image.get_rect().size
            img_data = pygame.image.tostring(image, 'RGBA')
            self.texture = glGenTextures(1)
            glBindTexture(GL_TEXTURE_2D, self.texture)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA8, image_width,
                         image_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)

            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
            glBindTexture(GL_TEXTURE_2D, 0)
            glGenerateMipmap(GL_TEXTURE_2D)
        else:
            print("Falha ao carregar a imagem")

    def Bind(self):
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self.texture)

    def UnBind(self):
        glBindTexture(GL_TEXTURE_2D, 0)

    def destroy(self):
        glDeleteTextures(1, self.texture)


if __name__ == "__main__":
    import main
    main.main()
