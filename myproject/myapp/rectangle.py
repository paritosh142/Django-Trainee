class Rectangle:
    def __init__(self , length : int , width : int):
        self.length = length
        self.width = width
    
    def __iter__(self):
        yield {'length' : self.length , 'width' : self.width}


if __name__ == '__main__':
    rectangle = Rectangle(10 , 20)
    for dimension in rectangle:
        print(dimension)