# /usr/bin/python3.7
# coding: utf-8
from tkinter import *
import random
import time

vx = 0
vy = 0


def gameTick():
    global pos, vx, vy
    canvas.move(ball, vx, vy)
    pos = canvas.coords(ball)
    if pos[0] <= 0:
        vx = v
        vy = 0
    elif pos[1] <= 0:
        vy = v
    elif pos[2] >= 1080:
        vx = -vx
        vy = 0
    elif pos[3] >= 720:
        vy = -v

    r1_pos = canvas.coords(r1)
    if pos[2] >= r1_pos[0] and pos[0] <= r1_pos[2]:
        if pos[3] >= r1_pos[1] and pos[3] <= r1_pos[3]:
            vy = 5
    r2_pos = canvas.coords(r2)
    if pos[2] >= r2_pos[0] and pos[0] <= r2_pos[2]:
        if pos[3] >= r2_pos[1] and pos[3] <= r2_pos[3]:
            vy = -5

    fenetre.after(10, gameTick)


# Joueur Droit
def haut_d(event):
    canvas.move(r1, 0, -10)


def bas_d(event):
    canvas.move(r1, 0, 10)


# Joueur Gauche
def haut_g(event):
    canvas.move(r2, 0, -10)


def bas_g(event):
    canvas.move(r2, 0, 10)


v = 5

vx = random.choice([-v, v])
vy = random.randrange(-v, v)

x1 = 510
y1 = 320
x2 = 570
y2 = 370


largeur = 1080
hauteur = 720
dla = largeur / 2
dlo = hauteur / 2


fenetre = Tk()
fenetre.title("Pong")
canvas = Canvas(fenetre, width=largeur, height=hauteur, bg="black")
canvas.pack()
Bouton_Quitter = Button(fenetre, text="Quitter", command=fenetre.quit)
Bouton_Quitter.pack()


ball = canvas.create_oval(x1, y1, x2, y2, fill="red", tag="ball")

line = canvas.create_line(dla, 0, 540, hauteur, fill="white", dash=(20, 10), width=4)

r1 = canvas.create_rectangle(1050, 270, 1070, 450, fill="red")
r2 = canvas.create_rectangle(10, 270, 30, 450, fill="red")

# haut = canvas.create_line(1081, 1, 0, 1, fill="red", width=4)
# bas = canvas.create_line(1081, 720, 0, 720, fill="red", width=4)
# droite = canvas.create_line(0, 1, 1, 720, fill="red", width=4)
# gauche = canvas.create_line(1081, 720, 1081, 1, fill="red", width=4)

canvas.bind_all("<Up>", haut_d)
canvas.bind_all("<Down>", bas_d)
canvas.bind_all("a", haut_g)
canvas.bind_all("q", bas_g)

gameTick()

fenetre.mainloop()
