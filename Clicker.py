from tkinter import *
from random import randint
import time
import rush
import pygame
import tic_tac_toe as morpion
import balles



fenetre =Tk()
fenetre.title("Clicker")
fenetre.geometry('620x535')
#fenetre.attributes('-topmost',TRUE)

image2 = PhotoImage( file = "sans.png")

class amelioration:
    def __init__(self, prix, clic, etat, nom):
        self.prix = prix
        self.clic = clic
        self.etat = etat
        self.nom = nom

clic = 1
argent = IntVar(value=0)
amelioration1 = amelioration(20, 3, False, "Foreuse")
amelioration2 = amelioration(500, 10, False, "Engin")
amelioration3 = amelioration(500, 10, False, "Engin2")
amelioration4 = amelioration(500, 10, False, "Engin3")

les_ameliorations = [amelioration1, amelioration2, amelioration3, amelioration4]

def ajout():
    global clic
    argent.set(argent.get() + clic)

def update_bouton():
    index = recherche_ame()

    if index is None:
        amelio.destroy()
        Label(fenetre, text="Vous avez acheté toutes les améliorations !").pack()
    else:
        ame = les_ameliorations[index]
        amelio.config(text=ame.nom, command=lambda: achat(index))

def achat(index):
    global clic
    ame = les_ameliorations[index]

    if argent.get() >= ame.prix:
        argent.set(argent.get() - ame.prix)
        clic += ame.clic
        ame.etat = True
        update_bouton(index)

def update_bouton(index):
    if index == 0:
        amelio.config(state = DISABLED,text='Acheté !')
    if index == 1:
        amelio2.config(state = DISABLED,text='Acheté !')
    if index == 2:
        amelio3.config(state = DISABLED,text='Acheté !')
    if index == 3:
        amelio4.config(state = DISABLED,text='Acheté !')
        
cadre_clicker = Frame(fenetre, bg = 'black',highlightbackground='brown',highlightthickness=3)
cadre_clicker.place(x=0,y=0,width=340,height=360)

cadre_amélioration = Frame(fenetre, bg = 'cyan',highlightbackground='brown',highlightthickness=3)
cadre_amélioration.place(x=337,y=0,width=283,height=360)

cadre_mini_jeux = Frame(fenetre, bg = 'yellow',highlightbackground='brown',highlightthickness=3)
cadre_mini_jeux.place(x=0,y=357,width=620,height=178)

compteur = Label(cadre_clicker,bg='brown', textvariable=argent,font='Impact 20')
compteur.place(x=40,y=30,width=260,height=80)

clicker = Button(cadre_clicker, text="Cliquez !", command=ajout,image=image2,font='Impact 25')
clicker.place(width = 260,height = 170,x=40,y=160)

amelio = Button(cadre_amélioration,text=amelioration1.nom,command=lambda:achat(0),font='Georgia 10')
amelio.place(x=20, y=70,width=100,height=50)

texte_amelio = Label(cadre_amélioration,text=f'Prix : {amelioration1.prix} ｜Clic + {amelioration1.clic}',font='Impact 12',bg='cyan')
texte_amelio.place(x=130, y=95,anchor=W)

amelio2 = Button(cadre_amélioration,text=amelioration2.nom,command=lambda:achat(1),font='Georgia 10')
amelio2.place(x=20, y=140,width=100,height=50)

texte_amelio2 = Label(cadre_amélioration,text=f'Prix : {amelioration2.prix} ｜Clic + {amelioration2.clic}',font='Impact 12',bg='cyan')
texte_amelio2.place(x=130, y=165,anchor=W)

amelio3 = Button(cadre_amélioration,text=amelioration3.nom,command=lambda:achat(2),font='Georgia 10')
amelio3.place(x=20, y=210,width=100,height=50)

texte_amelio3 = Label(cadre_amélioration,text=f'Prix : {amelioration3.prix} ｜Clic + {amelioration3.clic}',font='Impact 12',bg='cyan')
texte_amelio3.place(x=130, y=235,anchor=W)

amelio4 = Button(cadre_amélioration,text=amelioration4.nom,command=lambda:achat(3),font='Georgia 10')
amelio4.place(x=20, y=280,width=100,height=50)

texte_amelio4 = Label(cadre_amélioration,text=f'Prix : {amelioration4.prix} ｜Clic + {amelioration4.clic}',font='Impact 12',bg='cyan')
texte_amelio4.place(x=130, y=305,anchor=W)

texte_amelio = Label(cadre_amélioration,text='Améliorations',font='Impact 20',bg='cyan')
texte_amelio.place(x=60,y=5)

# --- Section Mini-Jeux ---
liste_jeux = ["MORPION","X2","RUSHHOUR","÷2","BALLES"]
boutons_mini_jeux = []

def lancer_roulette():
    global argent
    bouton_roulette.config(state=DISABLED)
    hasard = randint(0,4)
    print(hasard)
    hasard2 = randint(0,4)
    coup_animation = 30 + abs(hasard-hasard2)
    for i in range(15):
        boutons_mini_jeux[(hasard2+i)%5].config(bg='gold')
        boutons_mini_jeux[(hasard2+i)%5].update_idletasks()
        time.sleep(0.08)
        boutons_mini_jeux[(hasard2+i)%5].config(bg='white')
        boutons_mini_jeux[(hasard2+i)%5].update_idletasks()
    for i in range(coup_animation-15):
        boutons_mini_jeux[(hasard2+i)%5].config(bg='gold')
        boutons_mini_jeux[(hasard2+i)%5].update_idletasks()
        time.sleep(0.2)
        boutons_mini_jeux[(hasard2+i)%5].config(bg='white')
        boutons_mini_jeux[(hasard2+i)%5].update_idletasks()
    for _ in range(10):
        boutons_mini_jeux[hasard2].config(bg='gold')
        boutons_mini_jeux[hasard2].update_idletasks()
        time.sleep(0.2)
        boutons_mini_jeux[hasard2].config(bg='white')
        boutons_mini_jeux[hasard2].update_idletasks()
    time.sleep(0.2)
    if hasard == 2:
        win = rush.rush(pygame.display.set_mode((0,0)),pygame.time.Clock())
        if win == True:
            argent.set(argent.get() + 500)
            pygame.quit()
        else:
            pygame.quit()
    if hasard == 0:
        win = morpion.tic_tac_toe(pygame.display.set_mode((0,0)),pygame.time.Clock())
        if win == True:
            argent.set(argent.get()+500)
            pygame.quit()

        if win == False:
            argent.set(argent.get()-250)
            pygame.quit()
        else:
            pygame.quit()
    if hasard == 1:
        argent.set(argent.get()*2)
    if hasard == 3:
        argent.set(argent.get()//2)
    if hasard == 4:
        score = balles.balles(pygame.display.set_mode((0,0)),pygame.time.Clock())
        argent.set(argent.get()+(score*10))
        pygame.quit()

        
    boutons_mini_jeux[hasard].config(bg='white')
    bouton_roulette.config(state=ACTIVE)
        
    


# Boucle pour les 5 boutons
for i in range(5):
    texte_vertical = "\n".join(list(liste_jeux[i]))
    btn = Button(cadre_mini_jeux, 
                 text=texte_vertical, 
                 font='Impact 11', 
                 bg='white',
                 state=DISABLED)
    btn.place(x=10 + (65 * i), y=10, width=55, height=155)
    boutons_mini_jeux.append(btn)

# Ajout du bouton Roulette à la fin
bouton_roulette = Button(cadre_mini_jeux, 
                         text="R\nO\nU\nL\nE\nT\nT\nE", 
                         font='Impact 10', 
                         bg='red', 
                         fg='white',
                         command=lancer_roulette)
bouton_roulette.place(x=5*65+30, y=10, width=65, height=155)

boutons_mini_jeux[1].config(font='Impact 20')
boutons_mini_jeux[3].config(font='Impact 20')
texte_dette = Label(cadre_mini_jeux,textvariable=argent,font='Impact 13')
texte_dette.place(x=450, y = 10)
texte_dette2 = Label(cadre_mini_jeux,text='/1000000',font='Impact 13')
texte_dette2.place(x=490, y = 10)
bouton_dette = Button(cadre_mini_jeux,text='Remboursez votre dette !',font='Impact 10')
bouton_dette.place(x=450, y=40, width = 140, height = 110)
        
fenetre.mainloop()
