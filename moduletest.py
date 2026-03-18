from tkinter import *
import time
fenetre = Tk()
fenetre.title("Roue")

couleur="purple"
couleur2="blue"

cadre = Frame(fenetre)
cadre.grid(row=0,column = 10)

cadre2 = Frame(fenetre)
cadre2.grid(row=0,column = 0)

caneva2 = Canvas(cadre2,width = 500,height = 500,bg="black")
caneva2.grid(row=0,column = 0)

caneva = Canvas(cadre,width=250,height=50,bg=couleur2)
caneva.grid(row=1,column = 10)
caneva3 = Canvas(cadre,width=250,height=50,bg="purple")
caneva3.grid(row=0,column= 10)
caneva4 = Canvas(cadre,width=250,height=50,bg="purple")
caneva4.grid(row=2,column= 10)


texte = Label(cadre,text="Mini-jeu",bg="blue",fg="White",font="Times 15 italic bold")
texte.grid(row=1,column = 10)

def test ():
    print(test)

event_func = [test()]
event_caneva=[caneva]

def roulette ():
    for _ in range(2):
        (event_caneva[a]).bg= "yellow"
        caneva.update
        time.sleep(0.5)
        (event_caneva[a]).bg="blue"
    
        
bouton_test = Button(cadre,text="Test",command=roulette)
bouton_test.grid(row=20)
    
    

fenetre.mainloop()