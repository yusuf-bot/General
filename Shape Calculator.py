import math
class Shape_calc:
    class Rectangle:
        length=0
        height=0
        def __init__(self, h, l):
            self.length=int(l)
            self.height=int(h)

        def set_height(self,h):
            self.height=int(h)


        def set_length(self,l):
            self.length=int(l)


        def get_area(self):
            area=self.length*self.height
            return (f'The area is: {area}')


        def get_diagonal(self):
            dig=(self.length*self.length)+(self.height*self.height)
            dign=math.sqrt(dig)
            return (f'The length of the diagonal is: {dign}')


        def get_perimeter(self):
            peri=2*(self.height+self.length)
            return (f"The perimeter is: {peri}")


        # noinspection PyTypeChecker
        def get_picture(self):
            for x in range(0, self.height):
                for y in range(0, int(self.length)):
                    print ('*',end='')
                print ('')
            return (' ')

    class Square(Rectangle):
        length = 0
        height = 0

        def __init__(self,s):
            self.length = int(s)
            self.height = int(s)

        def set_side(self, s):
            self.height = int(s)
            self.length = int(s)

rect = Shape_calc.Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect.get_picture())

sq = Shape_calc.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq.get_picture())