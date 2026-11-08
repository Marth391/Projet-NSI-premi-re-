import random
import pygame 
def rush(screen,clock) :
    """C'est la fonction qui fera tourner tout le programme en prenant en paramètre
    une surface d'affichage pygame et une fréquence d'image."""
    pygame.init() 
    info = pygame.display.Info() # Demande les dimensions de l'écran pour adapter la taille des éléments 
    rouge = (255,000,000)
    vert = (000,255,000)
    blanc = (255,255,255)
    jaune = (255,255,000)
    violet = (255,000,255)
    orange = (255,150,80) # Définition des couleurs qui seront utilisées dans l'affichage du code 
    bleu = (000,000,255)
    noir = (000,000,000)
    rose = (255,105,180)
    cyan = (000,255,255)
    gris = (150,150,150)
    beige = (200,173,127) 

    class Voiture :
        def __init__(self, x, y, longueur, direc,color) :
            """Définit les attributs de la classe Voiture :
                - x la position en x
                - y la position en y
                - longueur la longueur de la voiture (le nombre de cases en positif ou négatif)
                - direc la direction de la voiture (horizontale ou verticale)
                - color la couleur de la voiture sur la représentation graphique"""
            self.x = x
            self.y = y
            self.longueur = longueur
            self.direc = direc 
            self.color = color 
            
        def sens(self,x,y) :
            """Cette fonction sert à déterminer si une voiture est cliquée à certaines
            coordonnées et si c'est le cas à déterminer s'il s'agit de la case correspondant
            à l'avant ou à l'arrière de la voiture. On renvoie ainsi l'extrémité cliquée ou
            False si la voiture n'est pas cliquée."""
            if self.x == x and self.y == y and self.direc == 0 :
                return "debutx"
            elif self.x == x and self.y == y and self.direc == 1 :
                return "debuty"
            elif self.x + self.longueur -1 == x and self.y == y and self.direc == 0 :
                return "finx"
            elif self.x == x and self.y + self.longueur -1 == y and self.direc == 1 :
                return "finy" 
            else :
                return False 
        
        def sur_grille(self) :
            """Cette fonction gère l'affichage des voitures en fonction de la direction
            et de la longueur."""
            if self.direc == 0 : # Voitures à l'horizontale 
                for i in range(self.longueur) :
                    grille[self.y][self.x + i] = self.color
            if self.direc == 1 : # Voitures à la verticale 
                for u in range(self.longueur) :
                    grille[self.y + u][self.x] = self.color
            pass 
        
        def avancer(self, sens) :
            """On utilise la méthode sens pour savoir comment doit se déplacer une voiture
            et on répercute les changements sur les coordonnées des voitures.
            
            Le try permet de rajouter une condition implicite sur la position de la voiture
            afin qu'elle reste sur la grille sans avoir à réaliser un calcul avec les coordonnées,
            le sens, la longueur.""" 
            if sens == "finx" :
                try : 
                    if grille[self.y][self.x + self.longueur] == blanc :
                        self.x += 1 
                except : pass
            if sens == "finy" :
                try : 
                    if grille[self.y+self.longueur][self.x] == blanc :
                        self.y += 1 
                except : pass 
            if sens == "debutx" :
                try : 
                    if grille[self.y][self.x - 1] == blanc :
                        self.x -= 1
                except : pass 
            if sens == "debuty" :
                try : 
                    if grille[self.y-1][self.x] == blanc :
                        self.y -= 1
                except : pass 
            pass 
    # Définition de toutes les positions initiales possibles avant d'en choisir une avec un randint 
    positions_disponibles = [[Voiture(0,0,3,0,jaune), Voiture(3,0,3,0,violet), Voiture(2,1,3,0,bleu),Voiture(0,2,2,0,rouge), Voiture(2,2,2,1,vert), Voiture(0,4,3,0,jaune), Voiture(5,4,2,1,orange)], 
                             [Voiture(0,0,3,0,jaune), Voiture(4,0,3,1,violet), Voiture(1,1,2,1,vert), Voiture(2,2,2,0,rouge), Voiture(4,3,2,0,orange), Voiture(4,4,2,0,rose), Voiture(2,4,2,1,bleu)],
                             [Voiture(0,0,2,0,vert), Voiture(2,0,2,0,orange), Voiture(4,0,2,1,cyan), Voiture(0,2,2,0,rouge), Voiture(3,2,2,1,rose), Voiture(0,3,3,0,jaune), Voiture(1,4,2,1,violet), Voiture(3,4,3,0,bleu)],
                             [Voiture(4,0,2,0,vert), Voiture(4,1,3,1,jaune), Voiture(2,2,2,0,rouge), Voiture(5,2,2,1,orange), Voiture(0,3,2,0,bleu), Voiture(2,3,2,0,rose), Voiture(0,4,2,9,violet), Voiture(2,4,2,1,cyan),Voiture(4,4,2,0,gris), Voiture(4,5,2,0,beige)],
                             [Voiture(2,0,3,1,jaune), Voiture(5,1,2,1,vert), Voiture(0,2,2,0,rouge), Voiture(4,3,3,1,violet), Voiture(0,4,2,1,orange), Voiture(1,4,2,0,bleu)],
                             [Voiture(1,0,3,1,jaune), Voiture(2,1,2,0,vert), Voiture(2,2,2,0,rouge), Voiture(4,2,2,1,orange), Voiture(5,1,3,1,violet), Voiture(3,3,2,1,bleu), Voiture(4,4,2,0,rose), Voiture(0,5,2,0,gris), Voiture(2,5,2,0,cyan)],
                             [Voiture(0,0,3,1,jaune), Voiture(1,0,2,1,vert), Voiture(2,0,2,1,orange), Voiture(3,0,3,0,violet), Voiture(4,1,2,1,beige), Voiture(5,1,2,1,rose), Voiture(1,2,2,0,rouge), Voiture(0,3,3,0,bleu), Voiture(4,3,2,1,vert), Voiture(5,3,2,1,cyan), Voiture(4,5,2,0,gris)],
                             [Voiture(2,0,2,0,gris), Voiture(4,0,2,0,orange), Voiture(2,1,3,0,jaune), Voiture(5,1,2,1,cyan), Voiture(0,2,2,0,rouge), Voiture(2,2,3,1,violet), Voiture(4,2,2,1,rose), Voiture(0,5,3,0,vert), Voiture(4,4,2,1,beige), Voiture(5,3,3,1,bleu)],
                             [Voiture(0,0,2,1,vert), Voiture(1,0,2,0,orange), Voiture(5,0,3,1,jaune), Voiture(1,1,2,0,bleu), Voiture(4,1,2,1,rose), Voiture(0,2,2,0,rouge), Voiture(2,2,2,1,violet), Voiture(1,4,2,1,cyan), Voiture(2,4,2,0,gris), Voiture(4,4,2,1,beige)],
                             [Voiture(0,0,2,1,vert), Voiture(1,0,3,1,jaune), Voiture(2,0,2,1,orange), Voiture(3,0,2,1,beige), Voiture(4,0,2,0,rose), Voiture(2,2,2,0,rouge), Voiture(5,1,2,1,violet), Voiture(2,3,3,1,violet), Voiture(4,3,2,0,cyan), Voiture(3,4,3,0,bleu), Voiture(0,5,2,0,gris)]]
    voitures = positions_disponibles[random.randint(0,9)]
    
    runing = True
    while runing : # Boucle du jeu 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT : # Détecte la fermeture de la fenêtre 
                runing = False
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE : # Arrête le jeu si la touche Échap est pressée 
                    runing = False
            if event.type == pygame.MOUSEBUTTONDOWN : # Détecte un clic de souris 
                coordonnee = pygame.mouse.get_pos() 
                x_interraction = (coordonnee[0] - (info.current_w//2 - 3*(info.current_h//10)))//(info.current_h//10)  
                y_interraction = (coordonnee[1] - (info.current_h//5))//(info.current_h//10) # Calcul des coordonnées sur la grille à partir des coordonnées sur l'écran 
                for v in voitures :
                    if v.sens(x_interraction,y_interraction) != False : # Vérifie si une voiture est cliquée et, si oui, à quelle extrémité 
                        v.avancer(v.sens(x_interraction,y_interraction)) # La voiture avance en conséquence 
        grille = [[blanc for i in range(6)]for j in range(6)] # Réinitialisation de la grille d'affichage 
        screen.fill(noir) # Réinitialisation de l'écran 
        for v in voitures :
            v.sur_grille() # Ajout des voitures sur la grille d'affichage réinitialisée 
        for i in range (6) : # Affichage de la grille 
            x_screen = (info.current_w//2) - (3*(info.current_h//10)) + (i*(info.current_h//10))
            for j in range(6) : 
                y_screen = info.current_h//5 + round(j*(info.current_h//10))
                pygame.draw.rect(screen,grille[j][i],(x_screen,y_screen,info.current_h//10,info.current_h//10))
        pygame.display.flip() 
        if grille[2][5] == rouge : # Détection de victoire 
            return True 
        clock.tick(60) 
    return False