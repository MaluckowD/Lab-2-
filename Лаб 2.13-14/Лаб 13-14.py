import turtle
# Создание холста
window = turtle.Screen()
window.title("Звезда Давида")
window.bgcolor("white")


width = abs(int(input("Введите ширину пера: ")))
# Создание черепахи
star = turtle.Turtle()
star.speed(0)
star.color("dark blue")
star.width(width)

# Рисование шестиконечной звезды Давида
size = abs(float(input("Введите длину правильного треугольника: ")))
number_of_sides = 3
angle = 60
star.penup()
star.goto(-size/2,  size / 2)
star.pendown()

for i in range(number_of_sides):
    star.forward(size)
    star.right(2 * angle)


star.penup()
star.right(90)
star.forward(size*3**0.5/3)
star.left(90)


star.pendown()
for i in range(number_of_sides):
    star.forward(size)
    star.left(2 * angle)

star.hideturtle()
# Завершение программы
turtle.done()


