
# important note about 'self': self is the pointer to the object that methods use to access the object
class Rectangle:
    number_of_rectangles = 0 # this is NOT an instance variable. this is a class variable and belongs to the class
    
    # this constructor is being ignored being Python looks at the last constructor defined in the file
    def __init__(self):
        self.length = 0 # all variables using 'self' belong to the object, and are instance variables
        self.width = 0
        self.color  = ""
        
    # this is the constructor that is being used by python ! because as we said above, the last constructor defined in the file is aadopted to run by python
    def __init__(self, length: int, width: int, color: str):
        self.length = length
        self.width = width
        self.color = color
        Rectangle.number_of_rectangles += 1
        
    # the str method is part of the python language, and it is used to print the contents of an object
    # this string is a private method. this means that it should not be called from outside the class
    # python doesn't support private access, so it's a convention, i.e. the convention for private is: __functionName__
    def __str__(self):
        my_string = "Length: " + str(self.length) + ", width: " + str(self.width) + ", color: " + self.color
        return my_string
    
    def calc_area(self):
        return self.length * self.width

if __name__ == "__main__":
    print("Practice with classes and objects")
    
    r1 = Rectangle(10, 5, "Red") # a call to the constructor
    r2 = Rectangle(5, 2, "Green")
    
    # r1.length = 8
    # r2.length = 11
    # r2.width = 9
    
    print(r1) # this line call to the str method
    print(r2) # another call to the constructor
    
    print(r1.number_of_rectangles)
    print(r2.number_of_rectangles)
    print(Rectangle.number_of_rectangles)
    
    s = r1.__str__()
    print(s)
    
    print(r1.calc_area())