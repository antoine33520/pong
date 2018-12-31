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
    posr1 = canvas.coords(r1)
    posr2 = canvas.coords(r2)

    # Bas de la fenêtre
    if posb[3] > 720:
        vy = -vy

    # Haut de la fenêtre
    elif posb[1] < 0:
        vy = -vy

    # Gauche de la fenêtre
    elif posb[0] < 0:
        vx = 0
        vy = 0

    # Droite de la fenêtre
    elif posb[2] > 1080:
        vx = 0
        vy = 0

    canvas.move(ball, vx, vy)
    # Raquette droite
    if (posb[2] > posr1[0]) and (posb[0] < posr1[2]):
        vx = -vx
    # Raquette gauche
    if (posb[2] > posr2[0]) and (posb[0] < posr2[2]):
        vx = -vx

    fenetre.after(10, gameTick)


# Joueur Droit
def haut_d(event):
    canvas.move(r1, 0, -50)


def bas_d(event):
    canvas.move(r1, 0, 50)


# Joueur Gauche
def haut_g(event):
    canvas.move(r2, 0, -50)


def bas_g(event):
    canvas.move(r2, 0, 50)


v = 4

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
canvas.bind_all("A", haut_g)
canvas.bind_all("Q", bas_g)

gameTick()

fenetre.mainloop()
