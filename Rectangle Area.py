class Rectangle:

    def __init__(self,width,length,):
        self.width = width
        self.length = length
    
    def area(self):
        return self.width * self.length
    
rectangle1 = Rectangle(int(input("Enter the width: ")),int(input("Enter the length: ")))

print("Area of the rectangle with width {} and length {} is {}".format(rectangle1.width,rectangle1.length,rectangle1.area()))



