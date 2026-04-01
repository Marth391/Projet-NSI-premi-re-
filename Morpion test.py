plateau =[0 for i in range 9]

def choix_joueur():
    case=int(input("Entrer un nombre entre 1 et 9: "))
    choix=case
    if case in range(len(plateau)):
        if plateau[case]==0:
            plateau[case]="X"
    else:
        return none
    print(plateau)

def bot ():
	bloque la victoire du joueur ou joue une case au hasard

def jeu():
    win=None
    if  plateau[case]== plateau[0]==plateau[1]==plateau[2]\
    or  plateau[case]== plateau[3]==plateau[4]==plateau[5]\
    or  plateau[case]== plateau[6]==plateau[7]==plateau[8]\
    or  plateau[case]== plateau[0]==plateau[3]==plateau[6]\
    or  plateau[case]== plateau[1]==plateau[4]==plateau[7]\
    or  plateau[case]== plateau[2]==plateau[5]==plateau[8]\
    or  plateau[case]== plateau[0]==plateau[4]==plateau[8]\
    or  plateau[case]== plateau[6]==plateau[4]==plateau[2]:
        win=True
    
    if  == plateau[0]==plateau[1]==plateau[2]\
    or  plateau[case_bot]== plateau[3]==plateau[4]==plateau[5]\
    or  plateau[case_bot]== plateau[6]==plateau[7]==plateau[8]\
    or  plateau[case_bot]== plateau[0]==plateau[3]==plateau[6]\
    or  plateau[case_bot]== plateau[1]==plateau[4]==plateau[7]\
    or  plateau[case_bot]== plateau[2]==plateau[5]==plateau[8]\
    or  plateau[case_bot]== plateau[0]==plateau[4]==plateau[8]\
    or  plateau[case_bot]== plateau[6]==plateau[4]==plateau[2]:
        win=False
    while win != True or win != False or 0 in plateau:
        tab[demande joueur] = 1
        verifie si le joueur a gagné
            si oui : win = true
        sinon : tab[bot] = 2
        verifie si le bot a gagné 
            si oui : win = false

if win == true:
return Le joueur a gagné !
if win == false:
return le joueur a perdu !
else:
return égalité !
