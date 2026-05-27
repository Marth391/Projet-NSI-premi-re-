import random
import pygame 
def rush(screen,clock) :
    pygame.init() 
    info = pygame.display.Info()
    rouge = (255,000,000)
    vert = (000,255,000)
    blanc = (255,255,255)
    jaune = (255,255,000)
    violet = (255,000,255)
    orange = (255,150,80)
    bleu = (000,000,255)
    noir = (000,000,000)
    rose = (255,105,180)
    cyan = (000,255,255)
    gris = (150,150,150)
    beige = (200,173,127) 

    class Voiture :
        def __init__(self, x, y, longueur, direc,color) :
            """cette fonction définit les voitures"""
            self.x = x
            self.y = y
            self.longueur = longueur
            self.direc = direc 
            self.color = color 
            
        def sens(self,x,y) :
            """cette fonction définit le sens dans lequel une voiture doit avancer en fonction des coordonnées d'un clic de souris"""
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
            """cette fonction gère l'affichage des voitures en fonction du sens et de la longueur"""
            if self.direc == 0 : #les voitures à l'horizontale 
                for i in range(self.longueur) :
                    grille[self.y][self.x + i] = self.color
            if self.direc == 1 : #les voitures à la verticale 
                for u in range(self.longueur) :
                    grille[self.y + u][self.x] = self.color
            pass 
        
        def avancer(self, sens) :
            if sens == "finx" :
                try : 
                    if grille[self.y][self.x + self.longueur] == blanc :
                        self.x += 1 
                except : pass
            if sens == "finy" :
                if grille[self.y+self.longueur][self.x] == blanc :
                    self.y += 1 
            
            if sens == "debutx" :
                if grille[self.y][self.x - 1] == blanc and self.x -1 >= 0:
                    self.x -= 1
            if sens == "debuty" :
                if grille[self.y-1][self.x] == blanc and self.y -1 >= 0 :
                    self.y -= 1 
            pass 
    #définition de toutes les positions initiales possibles avant d'en choisir 1 
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
    while runing : #boucle du jeu 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT : #détecte la fermeture de la fenêtre 
                runing = False
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE : #arrête le jeu si la touche échap est pressée 
                    runing = False
            if event.type == pygame.MOUSEBUTTONDOWN : #détecte un clic de souris 
                coordonnee = pygame.mouse.get_pos() 
                x_interraction = (coordonnee[0] - (info.current_w//2 - 3*(info.current_h//10)))//(info.current_h//10)  
                y_interraction = (coordonnee[1] - (info.current_h//5))//(info.current_h//10) #calcul des coordonnées sur la grille à partir des coordonnées sur l'écran 
                for v in voitures :
                    if v.sens(x_interraction,y_interraction) != False : #vérifie si une voiture est cliquée et, si oui, à quelle extrémité 
                        v.avancer(v.sens(x_interraction,y_interraction)) #la voiture avance en conséquence 
        grille = [[blanc for i in range(6)]for j in range(6)] #réinitialisation de la grille d'affichage 
        screen.fill(noir) #réinitialisation de l'écran 
        for v in voitures :
            v.sur_grille() #ajout des voitures sur la grille d'affichage 
        for i in range (6) :
            x_screen = (info.current_w//2) - (3*(info.current_h//10)) + (i*(info.current_h//10))
            for j in range(6) : #affichage de la grille 
                y_screen = info.current_h//5 + round(j*(info.current_h//10))
                pygame.draw.rect(screen,grille[j][i],(x_screen,y_screen,info.current_h//10,info.current_h//10))
        pygame.display.flip() 
        if grille[2][5] == rouge : #détection de victoire 
            return True 
        clock.tick(60) 
    return False 