class Vector2D:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = float(x)
        self.y = float(y)
    def set(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)
def main():
    vec = Vector2D()
    vec.set(5,6)
    print(f"x: {vec.x}, y:{vec.y}")
if __name__ == "__main__":
    main() 