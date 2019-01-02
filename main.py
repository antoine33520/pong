# /usr/bin/python3.7
# coding: utf-8
from tkinter import *
import random
import time


def gameTick():
    global pos, vx, vy, sj1, sj2, win
    canvas.move(ball, vx, vy)

    posb = canvas.coords(ball)
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
        sj1 += 1
        vx = 0
        vy = 0

    # Droite de la fenêtre
    elif posb[2] > 1080:
        sj2 += 1
        vx = 0
        vy = 0

    canvas.move(ball, vx, vy)
    # Raquette droite
    if (
        (posb[2] > posr1[0])
        and (posb[0] < posr1[2])
        and (posb[3] > posr1[1])
        and (posb[3] < posr1[3])
    ):
        vx = -v
        vy = random.randrange(-2, 2)
    # Raquette gauche
    if (
        (posb[2] > posr2[0])
        and (posb[0] < posr2[2])
        and (posb[3] > posr2[1])
        and (posb[3] < posr2[3])
    ):
        vx = v
        vy = random.randrange(-2, 2)

    if sj1 != sj2:
        print(sj1)
        print(sj2)
        win = 1
        fenetre.quit()

    fenetre.after(10, gameTick)


# Joueur Droit
def haut_d(event):
    canvas.move(r1, 0, -80)


def bas_d(event):
    canvas.move(r1, 0, 80)


# Joueur Gauche
def haut_g(event):
    canvas.move(r2, 0, -80)


def bas_g(event):
    canvas.move(r2, 0, 80)


def quit():
    print("destroy")
    fenetre.destroy()


v = 2
vx = random.choice([-v, v])
vy = random.randrange(-v, v)

x1 = 510
y1 = 320
x2 = 570
y2 = 370

sj1 = 0
sj2 = 0

largeur = 1080
hauteur = 720
dla = largeur / 2
dlo = hauteur / 2

fenetre = Tk()
fenetre.title("Pong")
canvas = Canvas(fenetre, width=largeur, height=hauteur, bg="black")
canvas.pack()
Bouton_Quitter = Button(fenetre, text="Quitter", command=fenetre.destroy)
Bouton_Quitter.pack()

ball = canvas.create_oval(x1, y1, x2, y2, fill="red", tag="ball")

line = canvas.create_line(dla, 0, 540, hauteur, fill="white", dash=(20, 10), width=4)

# Joueur Droit
r1 = canvas.create_rectangle(1050, 270, 1070, 450, fill="red")
# Joueur Gauche
r2 = canvas.create_rectangle(10, 270, 30, 450, fill="red")

canvas.bind_all("<Up>", haut_d)
canvas.bind_all("<Down>", bas_d)
canvas.bind_all("a", haut_g)
canvas.bind_all("q", bas_g)
canvas.bind_all("A", haut_g)
canvas.bind_all("Q", bas_g)

gameTick()

fenetre.mainloop()
