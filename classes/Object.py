from .Vector2D import Vector2D


class Object:
    def __init__(self, position: Vector2D, width=0, height=0) -> None:
        self.position = position
        self.width = width
        self.height = height

    @property
    def center(self) -> str:
        return Vector2D(self.position.x + self.width / 2, self.position.y + self.height / 2)

    @center.setter
    def center(self, newCenter: Vector2D):
        self.position.x = newCenter.x - self.width / 2
        self.position.y = newCenter.y - self.height / 2
