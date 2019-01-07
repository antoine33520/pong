# /usr/bin/python3.7
# coding: utf-8
from tkinter import *
from tkinter import ttk
import random
import time

def jeu():
    global pos, vx, vy, sj1, sj2, game, fenetre
    game = 1

    def gameTick():
        global pos, vx, vy, sj1, sj2, game
        # fenetre.update()
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
            game = 0
            # fenetre.destroy()

        # Droite de la fenêtre
        elif posb[2] > 1080:
            sj2 += 1
            vx = 0
            vy = 0
            game = 0
            # fenetre.destroy()

        canvas.move(ball, vx, vy)
        # Raquette droite
        if ((posb[2] > posr1[0]) and (posb[0] < posr1[2]) and (posb[3] > posr1[1]) and (posb[3] < posr1[3])):
            vx = -v
            vy = random.randrange(-2, 2)
        # Raquette gauche
        if ((posb[2] > posr2[0]) and (posb[0] < posr2[2]) and (posb[3] > posr2[1]) and (posb[3] < posr2[3])):
            vx = v
            vy = random.randrange(-2, 2)

        if game == 0:
            print(sj1)
            print(sj2)
            fermer()

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

    # def score():
    #     global sj1,sj2
    #     tsj1=canvas.create_text(100,100, text=("Score Joueur Gauche", sj1),
    #     font=("Comic Sans", 50))
    #     tsj2=canvas.create_text(100,100, text=("Score Joueur Gauche", sj2),
    #     font=("Comic Sans", 50))

    def fermer():
        global fenetre
        fenetre.destroy()
        jeu()


    v = 2
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
    fenetre.title("PONG")
    canvas = Canvas(fenetre, width=largeur, height=hauteur, bg="black")
    canvas.pack()
    canvas.focus_force()
    Bouton_Quitter = Button(fenetre, text="Quitter", command=fenetre.destroy)
    Bouton_Quitter.pack()
    
    ball = canvas.create_oval(x1, y1, x2, y2, fill="red", tag="ball")

    line = canvas.create_line(dla, 0, 540, hauteur, fill="white", dash=(20, 10), width=4)

    # Joueur Droit
    r1 = canvas.create_rectangle(1050, 270, 1070, 450, fill="red")
    # Joueur Gauche
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
    canvas.bind_all("<Backspace>",espace)

    # def loop():
    #     if state == 'startup':
    #         Label(text="The Game is starting now!").grid(row=0,column=0)
    #     elif state == 'running':
    #         Label(text="The Game is running now!").grid(row=0,column=0)

    gameTick()
    fenetre.mainloop()

def launch():
    global win, game, sj1,sj2
    menup.destroy()
    sj1 = 0
    sj2 = 0
    jeu()

NORM_FONT = ("Verdana", 10)

def popupmsg():
    popup = Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text="lol", font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()
# Menu Principal
menup = Tk()
menup.title("PONG")
txtaction = Label(menup, text="Choisissez une action").grid(row=0, column=1)
bjouer = Button(menup, text="Jouer", command=launch).grid(row=1, column=0)
bquitter = Button(menup, text="Quitter", command=menup.destroy).grid(row=1, column=2)
txtou = Label(menup, text="ou").grid(row=1, column=1)
menup.mainloop()

