from abc import ABC, abstractmethod


class Shape(ABC):
    
    def __init__(self, name) -> None:
        self.name = name

    @abstractmethod
    def area(self):
        pass
    
        
class Rectangle(Shape):
    
    def __init__(self, name, r_len, r_width) -> None:
        super().__init__(name)
        self.r_len = r_len
        self.r_width = r_width
        
    def area(self):
        return self.r_width * self.r_len
        
    def prem(self):
        return self.r_width * 2 + self.r_len * 2
        
class Rectangular_Cube(Rectangle):
        
        def __init__(self, name, r_len, r_width) -> None:
            super().__init__(name, r_len, r_width)
        
        def surface_area(self):
            # Use method area from the parent class Rectangle to calculate the surface area of a rectangular Cube
            pass
        
class Circle(Shape):
    
    def __init__(self, name, radius) -> None:
        super().__init__(name)
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius * self.radius

class Triangle(Shape):
    
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width
        
    def area(self):
        pass
    
class Line(Shape):
    
    def __init__(self, name, radius) -> None:
        super().__init__(name)
        self.radius = radius
        
    def area(self):   
        print("Line has no area!")    


# This is not a method! It does not belong to a class. It's a global function
# Function enlarge takes a shape object as input
def enlarge(my_shape):
    my_shape.prem()
    print("You want to enlarge: " + my_shape.name)


if __name__ == "__main__":
    
    # s = Shape("Some Shape")
    r = Rectangle("Rectangle", 10, 20)
    c = Circle("Circle", 5)

    # s.area()
    print(r.area())
    print(c.area())

    enlarge(r)
    # enlarge(c)