# hi


class Piece(object):

    def __init__(self, position, color):
        self.position = position
        self.color = color

    def getPosition(self):
        return self.position

    def getColor(self):
        return self.color

    def setPosition(self, newPosition):
        self.position = newPosition

    def setColor(self, newColor):
        self.color = newColor




class King(Piece):
    def __init__(self, position, color):
        super().__init__(position, color)

class Queen(Piece):
    def __init__(self, position, color):
        super().__init__(position, color)


class Bishop(Piece):
    def __init__(self, position, color):
        super().__init__(position, color)


class Knight(Piece):
    def __init__(self, position, color):
        super().__init__(position, color)


class Rook(Piece):
    def __init__(self, position, color):
        super().__init__(position, color)

class Pawn(Piece):
    def __init__(self, position, color):
        super().__init__(position, color)
