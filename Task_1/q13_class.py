# Q13-Implementing classes

from abc import ABC,abstractmethod 
class Shape(ABC):
    def __init__(self,c):
        self.color = c
    def get_color(self):
        return self.color
    @abstractmethod
    def get_area(self) -> float:
        pass
class Square(Shape):
    def __init__(self, c, side):
        super().__init__(c)
        self.side = side
    def get_area(self):
        return self.side*self.side

# just testing the code using print to see if it works
s=Square("Red",5)
print(s.get_color())
print(s.get_area())
