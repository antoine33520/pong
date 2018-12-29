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

    fenetre.after(10, gameTick)




v = 5

vx = random.choice([-v, v])
vy = random.randrange(-v, v)

x1 = 510
y1 = 320
x2 = 570
y2 = 370


largeur = 1080
longueur = 720
dla = largeur / 2
dlo = longueur / 2


fenetre = Tk()
fenetre.title("Pong")
canvas = Canvas(fenetre, width=largeur, height=longueur, bg="black")
canvas.pack()
Bouton_Quitter = Button(fenetre, text="Quitter", command=fenetre.quit)
Bouton_Quitter.pack()


ball = canvas.create_oval(x1, y1, x2, y2, fill="red", tag="ball")
line = canvas.create_line(dla, 0, 540, longueur, fill="white", dash=(20, 10), width=4)
haut = canvas.create_line(1081, 1, 0, 1, fill="red", width=4)
bas = canvas.create_line(1081, 720, 0, 720, fill="red", width=4)
droite = canvas.create_line(0, 1, 1, 720, fill="red", width=4)
gauche = canvas.create_line(1081, 720, 1081, 1, fill="red", width=4)


gameTick()
# rebond()

fenetre.mainloop()
