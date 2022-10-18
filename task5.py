class Rectangle:
    def __init__(self, length , width):
        self.length = length
        self.width = width
        
    def Perimeter(self):
        return 2*(self.length + self.width)
    
    def Area(self):
        return self.length*self.width   
    
    def display(self):
        print("The length  is: ", self.length)
        print("The width is: ", self.width)
        print("The perimeter is: ", self.Perimeter())
        print("The area is: ", self.Area())

class Parallelepipede(Rectangle):
    def __init__(self, length, width , height):
        Rectangle.__init__(self, length, width)
        self.height=height    
    def volume(self):
        return self.length*self.width*self.height
        
obj1 = Rectangle(7 , 5)
obj1.display()
mypipede = Parallelepipede(7 , 5 , 2)
print("the volume  is: " , mypipede.volume())