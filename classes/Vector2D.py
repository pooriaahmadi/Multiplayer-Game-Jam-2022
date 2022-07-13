class Vector2D:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __add__(self, value):
        self.x += value.x
        self.y += value.y
        return self

    def __repr__(self) -> str:
        return f"X: {self.x}, Y: {self.y}"
