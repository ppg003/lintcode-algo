class Shape:
    def draw(self):
        raise NotImplementedError('This method should have implemented.')


class Triangle(Shape):
    def draw(self):
        print("  /\\\n /  \\\n/____\\")


class Rectangle(Shape):
    def draw(self):
        print(" ----\n|    |\n ----")


class Square(Shape):
    def draw(self):
        print(" ----\n|    |\n|    |\n ----")


class ShapeFactory:
    def getShape(self, shapeType):
        """
        :param shapeType: {string} shapeType a string
        :return: {Shape} Get object of type Shape
        """
        if shapeType == "Square":
            return Square()
        elif shapeType == "Triangle":
            return Triangle()
        elif shapeType == "Rectangle":
            return Rectangle()
        else:
            return None


a = ShapeFactory()
a.getShape("Square")
