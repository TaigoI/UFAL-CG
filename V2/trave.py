
from object import Object


class Traves:
    def __init__(self, texture):
        Object(texture, (8, 3, 1.5), (30, 0.1, -1.5), 3, (1.0, 0.5, 0.5))
        Object(texture, (8, 3, 1.5), (30, 0.1, 110), 3, (0.5, 0.5, 1.0))


if __name__ == "__main__":
    import main
    main.main()
