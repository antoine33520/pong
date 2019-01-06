# /usr/bin/python3.7
# coding: utf-8
from tkinter import *
import random
import time


def jeu():
    global vx, vy, sj1, sj2, game, fenetre
    game = 1

    def gameTick():
        global vx, vy, sj1, sj2, game
        canvas.move(ball, vx, vy)

        posb = canvas.coords(ball)
        posr1 = canvas.coords(r1)
        posr2 = canvas.coords(r2)

        # Bas de la fenêtre
        if posb[3] > 720:
            vy = -vy - rd

        # Haut de la fenêtre
        elif posb[1] < 0:
            vy = -vy + rd

        # Gauche de la fenêtre
        elif posb[0] < 0:
            sj1 += 1
            vx = 0
            vy = 0
            game = 0

        # Droite de la fenêtre
        elif posb[2] > 1080:
            sj2 += 1
            vx = 0
            vy = 0
            game = 0

        canvas.move(ball, vx, vy)
        # Raquette droite
        if (
            (posb[2] > posr1[0])
            and (posb[0] < posr1[2])
            and (posb[3] > posr1[1])
            and (posb[3] < posr1[3])
        ):
            vx = -v
            vy = random.randrange(-3, 3)
        # Raquette gauche
        if (
            (posb[2] > posr2[0])
            and (posb[0] < posr2[2])
            and (posb[3] > posr2[1])
            and (posb[3] < posr2[3])
        ):
            vx = v
            vy = random.randrange(-3, 3)

        if game == 0:
            print(sj1)
            print(sj2)

            if sj1 == npg:
                fenetre.destroy()
                menu()
            elif sj2 == npg:
                fenetre.destroy()
                menu()
            else:
                continuer()

        fenetre.after(20, gameTick)

    # Joueur Droit
    def haut_d(event):
        canvas.move(r1, 0, -100)

    def bas_d(event):
        canvas.move(r1, 0, 100)

    # Joueur Gauche
    def haut_g(event):
        canvas.move(r2, 0, -100)

    def bas_g(event):
        canvas.move(r2, 0, 100)

    def rejouer():
        global fenetre
        fenetre.destroy()
        jeu()

    def continuer():

        popup = Tk()
        popup.title("Continuer ?")
        label = Label(popup, text="Manche Suivante ?", font=police10).pack(
            side="top", pady=10
        )
        oui = Button(
            popup, text="Continuer", command=lambda: [popup.destroy(), rejouer()]
        ).pack(side="left")
        quit = Button(
            popup, text="Quitter", command=lambda: [popup.destroy(), fenetre.destroy()]
        ).pack(side="right")
        popup.mainloop()

    # Vitesses
    v = 7
    vx = random.randrange(-v, v)
    vy = random.randrange(-v, v)
    rd = random.randrange(0, 3)

    # Nombre de points pour gagner
    npg = 3

    # Emplacement de la balle au démarrage
    x1 = 510
    y1 = 320
    x2 = 570
    y2 = 370

    # Valeurs pour la taille de la fenêtre
    largeur = 1080
    hauteur = 720
    dla = largeur / 2
    dlo = hauteur / 2

    # Fenêtre
    fenetre = Tk()
    fenetre.title("PONG")
    canvas = Canvas(fenetre, width=largeur, height=hauteur, bg="black")
    canvas.pack()
    canvas.focus_force()
    Bouton_Quitter = Button(fenetre, text="Quitter", command=fenetre.destroy)
    Bouton_Quitter.pack()

    # Balle
    ball = canvas.create_oval(x1, y1, x2, y2, fill="red", tag="ball")
    # Ligne
    line = canvas.create_line(
        dla, 0, 540, hauteur, fill="white", dash=(20, 10), width=4
    )

    # Joueur Droit
    r1 = canvas.create_rectangle(1050, 260, 1070, 430, fill="red")
    # Joueur Gauche
    r2 = canvas.create_rectangle(10, 260, 30, 430, fill="red")

    # Commandes Joueurs
    canvas.bind_all("<Up>", haut_d)
    canvas.bind_all("<Down>", bas_d)
    canvas.bind_all("a", haut_g)
    canvas.bind_all("q", bas_g)
    canvas.bind_all("A", haut_g)
    canvas.bind_all("Q", bas_g)

    gameTick()
    fenetre.mainloop()


def launch():
    global win, game, sj1, sj2
    menup.destroy()
    sj1 = 0
    sj2 = 0
    jeu()


def menu():
    global menup
    # Menu Principal
    menup = Tk()
    menup.title("PONG")
    txtaction = Label(menup, text="Voulez-vous faire une partie de pong").grid(
        row=0, column=1, pady=10
    )
    bjouer = Button(menup, text="Oui, Jouer", command=launch).grid(row=1, column=0)
    bquitter = Button(menup, text="Non, Quitter", command=menup.destroy).grid(
        row=1, column=2
    )
    txtou = Label(menup, text="ou").grid(row=1, column=1)
    menup.mainloop()


Police12 = ("Verdana", 12)
police10 = ("Verdana", 10)
police8 = ("Verdana", 8)

menu()
