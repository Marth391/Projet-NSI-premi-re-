from random import randint
from random import choice

plateau=[[0,0,0],[0,0,0],[0,0,0]]
dico={"A":0,"B":1,"C":2,"1":0,"2":1,"3":2}



def coup():
    """Demande au joueur quel colone et ligne il veut jouer, renvoie un tableau de 2 str"""
    case=[]
    test=False
    case.append(str(input("choisissez une colone "))) #A changer pour Pygame
    case[0]=case[0].upper()
    case.append(str(input("entrez une ligne ")))
    assert case[0] in "A" or "B" or "C"
    assert case[1] in "1" or "2" or "3"
    if plateau[dico[case[0]]][dico[case[1]]] != 0:
        test=True
    print(test)
    return case

def coup_bot():
    global plateau
    combos=[("A","1","B","1","C","1"), #Première ligne
            ("A","2","B","2","C","2"), #Deuxième ligne
            ("A","3","B","3","C","3"), #Troisième ligne
            ("A","1","B","2","C","3"), #Première diagonal
            ("A","3","B","2","C","1"), #Deuxième diagonal
            ("A","1","A","2","A","3"), #Première colone
            ("B","1","B","2","B","3"), #Deuxième colone
            ("C","1","C","2","C","3")  #Troisième colone
            ]
    
    def case_vide(col,lig):
        return plateau[dico[col]][dico[lig]] == 0

    def chercher_coup(valeur):
        for a_col, a_lig, b_col, b_lig, c_col, c_lig in combos:
            cases = [(a_col, a_lig), (b_col, b_lig), (c_col, c_lig)]
            valeurs = [plateau[dico[col]][dico[lig]] for col, lig in cases]
            if valeurs.count(valeur) == 2 and valeurs.count(0) == 1:
                index = valeurs.index(0)
                return list(cases[index])
        return None
    
    coup=chercher_coup(1) #Cherche un coup gagnant
    if coup:
        return coup
    
    coup=chercher_coup(9) #Cherche à bloquer le joueur
    if coup:
        return coup
    
    cases_vides = [[col, lig] for col in ["A","B","C"] for lig in ["1","2","3"]
                   if case_vide(col, lig)] #Joue au hasard
    return choice(cases_vides)
    

def verifie():
    """Verifie si trois symbole sont allignes dans la grille, renvoie True"""
    global plateau
    for i in range(3):
        if plateau[i][0] == plateau[i][1] == plateau[i][2] !=0:
            return True
        if plateau[0][i] == plateau[1][i] == plateau[2][i] !=0:
            return True
    if plateau[0][0] == plateau[1][1] == plateau[2][2] !=0:
        return True
    if plateau[0][2] == plateau[1][1] == plateau[2][0] !=0:
        return True
    return False
    
def jeu():
    """Fonction principal du jeu, à lancer pour jouer"""
    global plateau
    plateau=[[0,0,0],[0,0,0],[0,0,0]]
    
    premier=randint(1,2)
    print("Vous avez les cercles !")
    
    if premier == 1:
        joueur=True
    else:
        joueur=False
        bot=True
    
    cpt_case=9
    
    
    while cpt_case != 0:
        if joueur==True:
            coup_jouer=coup()
            plateau[dico[coup_jouer[0]]][dico[coup_jouer[1]]]=9
            
        
        else:
            coup_jouer=coup_bot()
            plateau[dico[coup_jouer[0]]][dico[coup_jouer[1]]]=1
        
        cpt_case -=1
        qui_a_joue= "joueur" if joueur else "bot"
        joueur = not joueur
        
        if verifie():
            return qui_a_joue
        
    return "nul"
