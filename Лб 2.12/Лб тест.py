class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def set_coord(self, x, y):
        if type(x) in (int, float) and type(y) in (int, float):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Координаты точки должны быть числами')
    def get_coord(self):
        return self.__x, self.__y
pt = Point(4.56, 2.34)    # обращение к классу
print(pt.get_coord())    # вывод: (4.56, 2.34)
pt.set_coord(9, '9')    # обращение к методу
print(pt.get_coord())    # вывод ValueError:
