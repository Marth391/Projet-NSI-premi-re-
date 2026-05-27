import pygame
import random
def balles (screen, clock) :
    info_ecran = pygame.display.Info() #récupère les infos de l'écran pour adapter la taille des balles et leur vitesse 
    class Balles :
        def __init__(self) :
            """Initie les propriétés des balles"""
            self.taille = random.randint(info_ecran.current_h//60,info_ecran.current_h//10)
            self.couleur = (random.randint(20,255), random.randint(20,255),random.randint(20,255))
            self.vitesse = random.randint(info_ecran.current_h//300,info_ecran.current_h//100) 
            self.x = random.randint(0,info_ecran.current_w-1) 
            self.y = 0-self.taille
            self.etat = True
            
        def draw(self, screen) :
            """affiche une balle sur un écran défini avec sa couleur, sa position et sa taille."""
            pygame.draw.circle(screen, self.couleur, (self.x, self.y), self.taille)
            pass
        
        def bouger (self) :
            """Pour faire bouger les balles"""
            self.y += self.vitesse
            pass
        
        def est_touchee (self):
            """Détecte si le curseur est sur la balle en utilisant les coordonnées du curseur et du centre de la balle ainsi que sa taille."""
            distance = ((position_souris[0] - self.x)**2 + (position_souris[1] - self.y)**2)**0.5
            return distance >= self.taille  
    mes_balles = [] #initialisation de la liste de balles 
    compteur = 0 #compteur de balles touchées 
    runing = True 
    while runing == True:
        
        if random.randint(0,50) == 1 : #il y a une probabilité de faire apparaître une balle 
            mes_balles.append(Balles())        
        for event in pygame.event.get() : #récupère les évènements qui ont eu lieu (touches pressées notamment) 
            
            if event.type == pygame.QUIT :
                runing = False
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE : #Les modalités pour fermer la fenêtre du jeu 
                    runing = False
                    
            if event.type == pygame.MOUSEBUTTONDOWN :
                position_souris = pygame.mouse.get_pos() #demande de vérifier si une balle est touchée à chaque clic de souris 
                for b in mes_balles :
                    b.etat = b.est_touchee()
                    
        screen.fill((0,0,0)) #remplit le fond en noir pour réinitialiser l'écran et ne pas avoir les anciennes images mais après on pourra mettre un fond 
        
        for b in mes_balles : 
            if b.etat == False :
                compteur += 1 #compteur de balles touchées 
            if b.y >= info_ecran.current_h :
                runing = False 
        mes_balles = [b for b in mes_balles if b.y <= (info_ecran.current_h + b.taille) and b.etat == True] #On gère l'affichage des balles et on supprime celles qui sont inutiles 
        
        for b in mes_balles : #affichage de toutes les balles 
            b.draw(screen)
            b.bouger()
        
        pygame.display.flip() #Affichage 
        clock.tick(60) 
    return compteur 