
from object import Object
from texture import Texture


class Arquibancadas:
    lDelta = 2
    wDelta = 0.90
    hDelta = 1.0
    nRows = 20

    def __init__(self, texture):
        self.Norte(texture)
        self.Sul(texture)
        self.Leste(texture)
        self.Oeste(texture)

    def Sul(self, texture):
        posX = 0
        posZ = 110 + (self.wDelta*5)
        length = 68

        for row in range(0, self.nRows):
            w = self.wDelta
            h = self.hDelta * (row+1)
            l = length+(self.lDelta*row)

            rowX = posX - (self.lDelta*row/2)
            rowZ = posZ + (self.wDelta*row)

            if (row == self.nRows-1):
                Object(texture, size=(l, h, w),
                       position=(rowX, 0, rowZ))
            else:
                Object(texture, size=(self.lDelta, h, w),
                       position=(rowX, 0, rowZ))
                Object(texture, size=(self.lDelta, h, w),
                       position=(l+rowX-w, 0, rowZ))
                Object(texture, size=(l, self.hDelta, w),
                       position=(rowX, row*self.hDelta, rowZ))

    def Norte(self, texture):
        posX = 0
        posZ = (self.wDelta*-6)
        length = 68

        for row in range(0, self.nRows):
            w = self.wDelta
            h = self.hDelta * (row+1)
            l = length+(self.lDelta*row)

            rowX = posX - (self.lDelta*row/2)
            rowZ = posZ - (self.wDelta*row)

            if (row == self.nRows-1):
                Object(texture, size=(l, h, w),
                       position=(rowX, 0, rowZ))
            else:
                Object(texture, size=(self.lDelta, h, w),
                       position=(rowX, 0, rowZ))
                Object(texture, size=(self.lDelta, h, w),
                       position=(l+rowX-w, 0, rowZ))
                Object(texture, size=(l, self.hDelta, w),
                       position=(rowX, row*self.hDelta, rowZ))

    def Oeste(self, texture):
        posX = (self.wDelta*-6)
        posZ = 0
        length = 110

        for row in range(0, self.nRows):
            w = self.wDelta
            h = self.hDelta * (row+1)
            l = length+(self.lDelta*row)

            rowX = posX - (self.lDelta*row/2)
            rowZ = posZ - (self.wDelta*row)

            if (row == self.nRows-1):
                Object(texture, size=(w, h, l),
                       position=(rowX, 0, rowZ))
            else:
                Object(texture, size=(w, h, self.lDelta),
                       position=(rowX, 0, rowZ))
                Object(texture, size=(w, h, self.lDelta),
                       position=(rowX, 0, l+rowZ-w))
                Object(texture, size=(w, self.hDelta, l),
                       position=(rowX, row*self.hDelta, rowZ))

    def Leste(self, texture):
        posX = 68 + (self.wDelta*5)
        posZ = 0
        length = 110

        for row in range(0, self.nRows):
            w = self.wDelta
            h = self.hDelta * (row+1)
            l = length+(self.lDelta*row)

            rowX = posX + (self.lDelta*row/2)
            rowZ = posZ - (self.wDelta*row)

            if (row == self.nRows-1):
                Object(texture, size=(w, h, l),
                       position=(rowX, 0, rowZ))
            else:
                Object(texture, size=(w, h, self.lDelta),
                       position=(rowX, 0, rowZ))
                Object(texture, size=(w, h, self.lDelta),
                       position=(rowX, 0, l+rowZ-w))
                Object(texture, size=(w, self.hDelta, l),
                       position=(rowX, row*self.hDelta, rowZ))


if __name__ == "__main__":
    import main
    main.main()
