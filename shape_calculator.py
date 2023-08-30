class Rectangle:
    def __init__(self, _width, _height):
        self.width = _width
        self.height= _height
    
    def __str__(self):
        the_string=""
        if(self.width==self.height):
            the_string+="Square"
        else:
            the_string+="Rectangle"
        the_string+="(width="+str(self.width)+", height="+str(self.height)+")"

        return the_string

    def set_width(self, _width):
        self.width=_width
    def set_height(self, _height):
        self.height=_height
    def get_area(self):
        return self.height*self.width
    def get_perimeter(self):
        return (2*(self.width+self.height))
    def get_diagonal(self):
        return ((self.width**2 + self.height **2)**0.5)
    def get_picture(self):
        the_string=""
        if(self.height>50 or self.width>50):
            return "Too big for picture."
        for i in range(self.height):
            for j in range(self.width):
                the_string+="*"
            the_string+="\n"
        return the_string 
    def get_amount_inside(self, _shape):
        return self.get_area()//_shape.get_area()



class Square(Rectangle):
    def __init__(self, _side):
        Rectangle.__init__(self, _side, _side)
        
    def __str__(self):
        the_string="Square"
        the_string+="(side="+str(self.width)+")"

        return the_string
    def set_side(self, _side):
        self.height=_side
        self.width=_side 

    def set_width(self, _side):
        self.height=_side
        self.width=_side 
    def set_height(self, _side):
        self.height=_side
        self.width=_side 



# rectangle = Rectangle(4,4)

# print(rectangle.get_perimeter())
# print(rectangle.get_diagonal())
# print(rectangle.get_picture())
# print(rectangle)

# square = Square(3)
# print(square.set_side(2))
# print(square.get_perimeter())
# print(square.get_diagonal())
# print(square.get_picture())
# print(square)

# print(rectangle.get_amount_inside(square))
