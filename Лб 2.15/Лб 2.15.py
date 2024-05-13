import turtle
import random

# Функция для создания кнопки с заданными параметрами
def create_button(x, y, label):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    for _ in range(2):
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)

    turtle.penup()
    turtle.goto(x + 40, y + 15)
    turtle.write(label, font=("Arial", 12, "normal"))


# Функция для обработки нажатия на кнопку
def button_click(x, y):
    global buttons
    for button in buttons:
        if button["x"] < x < button["x"] + 100 and button["y"] < y < button["y"] + 50:
            button["value"] += 1
            for other_button in buttons:
                if other_button != button:
                    other_button["value"] -= 1
            draw_buttons()


# Функция для отрисовки кнопок
def draw_buttons():
    turtle.clear()
    for button in buttons:
        create_button(button["x"], button["y"], str(button["value"]))
    turtle.update()


# Инициализация экрана
turtle.tracer(False)

# Создание кнопок
buttons = [{"x": -150, "y": 0, "value": random.randint(0, 10)},
           {"x": -50, "y": 0, "value": random.randint(0, 10)},
           {"x": 50, "y": 0, "value": random.randint(0, 10)},
           {"x": 150, "y": 0, "value": random.randint(0, 10)}]

# Отрисовка кнопок
draw_buttons()

# Установка обработчика кликов мыши
turtle.onscreenclick(button_click)
turtle.hideturtle()
turtle.done()
