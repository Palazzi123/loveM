import time
import turtle
import threading

def draw_heart():
    turtle.bgcolor("black")
    turtle.pensize(3)
    turtle.speed(3)
    turtle.color("red")

    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(180)
    turtle.circle(-90, 200)
    turtle.left(40)
    turtle.circle(-90, 200)
    turtle.forward(180)
    turtle.end_fill()

    turtle.hideturtle()
    turtle.done()

    heart_thread = threading.Thread(target=draw_heart)
    heart_thread.start()

    message = [
        "Моя дорогая, любимая и не повторимая!",
        "С 8 марта тебя! Ты - самое прекрасное, что есть в моей жизни!",
        "Ты - мой свет, моя радость, моя весна!",
        "Пусть твои глаза всегда сияют счастьем, а сердце - любовью!",
        "Ты делаешь мой тусклый и серый мир лучше просто существованием в моей жизни!",
        "Я благодарен судьбе за тебя и хочу, чтобы ты всегда улыбалась!",
        "Прости за моё отсуствие рядом в столь прекрасный день, я бы хочешь хотел его провести рядом с тобой..",
        "С праздником тебя, мой цветочек! Я тебя очень сильно люблю и ценю!<3"
    ]

    for line in message:
        print(line)
        time.sleep(2)