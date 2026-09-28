import turtle
import math
import random
from pygame import mixer
from tkinter import messagebox
import tkinter as tk



mixer.init()

mixer.music.load("./music/SunShine.mp3")

screen = turtle.Screen()

screen.bgcolor("black")
screen.title("Space Moment - Song")

pen = turtle.Turtle()

pen.speed(0)
pen.hideturtle()
pen.pensize(2)

colors = [
    "red",
    "blue",
    "purple",
    "cyan",
    "magenta",
    "orange",
    "white",
    "green",
    "yellow"
]

forms = random.randint(1,5)

def form(t, scale, deform):

    if forms == 1:

        raio = 2 + t * 3

        x = math.cos(t) * raio
        y = math.sin(t) * raio


    elif forms == 2:

        raio = 8 + 4 * math.sin(5 * t)

        x = math.cos(t) * raio
        y = math.sin(t) * raio


    elif forms == 3:

        raio = 15 + 7 * math.cos(5 * t)

        x = math.cos(t) * raio
        y = math.sin(t) * raio

    elif forms == 4:

        raio = 12 + 5 * math.sin(8 * t)

        x = math.cos(t) * raio
        y = math.sin(t) * raio


    elif forms == 5:

        x = 18 * math.cos(t)
        y = 8 * math.sin(t)


    x = x * scale * deform
    y = y * scale

    return x, y


def draw_pen():

    pen.clear()

    scale = random.uniform(0.8, 1.8)

    deform = random.uniform(0.7, 1.4)

    color = random.choice(colors)

    pen.color(color)

    pen.penup()

    for i in range(301):

        t = i / 20

        x, y = form(t, scale, deform)

        if i == 0:

            pen.goto(x, y)
            pen.pendown()

        else:

            pen.goto(x, y)

    pen.penup()

    screen.ontimer(draw_pen, 100)



def show_info():

    window = tk.Tk()

    window.withdraw()

    messagebox.showinfo(
        "MENU === CONTROL",

        "SPACE MOMENT\n\n"

        "CONTROLES DA MÚSICA\n\n"

        "I = Iniciar música\n"
        "P = Pausar música\n"
        "C = Continuar música\n"
        "S = Parar música\n\n"
    )

    window.destroy()


def start_music():

    mixer.music.play()


def pause_music():

    mixer.music.pause()


def continue_music():

    mixer.music.unpause()


def stop_music():

    mixer.music.stop()

screen.listen()

screen.onkey(start_music, "i")

screen.onkey(pause_music, "p")

screen.onkey(continue_music, "c")

screen.onkey(stop_music, "s")


show_info()

draw_pen()


screen.mainloop()