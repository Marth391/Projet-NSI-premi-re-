import pygame
import random 
def tic_tac_toe(screen,clock) :
    info = pygame.display.Info() #demande les informations de l'écran 
    t = info.current_h//3.5 #définit la taille des cases 
    
    noir = (000,000,000) 
    
    croix = pygame.transform.scale(pygame.image.load("croix.png"),(t,t))
    rond = pygame.transform.scale(pygame.image.load("rond.png"),(t,t)) #définition des images possibles dans les cases 
    fond_blanc = pygame.transform.scale(pygame.image.load("fond blanc.png"),(t,t))
    etats_possibles = [fond_blanc, rond, croix] #création d'une liste pour manipuler des nombres et non des images 
    
    combos = [ #positions gagnantes 
                ((0,0), (0,1), (0,2)), # Lignes
                ((1,0), (1,1), (1,2)),
                ((2,0), (2,1), (2,2)),
                ((0,0), (1,0), (2,0)), # Colonnes
                ((0,1), (1,1), (2,1)),
                ((0,2), (1,2), (2,2)),
                ((0,0), (1,1), (2,2)), # Diagonales
                ((0,2), (1,1), (2,0))
                ]
    
    grille = [[0 for i in range(3)]for j in range(3)] #création de la grille sous forme d'une liste 
    
    tour_self = random.randint(1,2) #définition d'un tour aléatoire pour le joueur (s'il joue en premier ou en deuxième) 
    tour = 1 #le tour de jeu est défini à 1 et correspondra donc aux ronds 

    runing = True #mise en place de la boucle de jeu 
    
    while runing :

        if tour != tour_self : #tour de jeu du bot (on le met en premier pour avoir un délai avant qu'il y ait un nouveau symbole) 
            jouer = True #variable qui garantit que le bot ne joue pas deux fois 
            pygame.time.delay(500) #délai 
            for c1, c2, c3 in combos : 
                if jouer == True : 
                    valeurs = [grille[c1[0]][c1[1]], grille[c2[0]][c2[1]], grille[c3[0]][c3[1]]] 
                    if valeurs.count(tour) == 2 and valeurs.count(0) == 1 : #le bot cherche s'il peut gagner 
                        cases = [c1, c2, c3]
                        jouer = False 
                        grille[cases[valeurs.index(0)][0]][cases[valeurs.index(0)][1]] = tour
            for c1, c2, c3 in combos :
                if jouer == True : 
                    valeurs = [grille[c1[0]][c1[1]], grille[c2[0]][c2[1]], grille[c3[0]][c3[1]]]
                    if valeurs.count(tour_self) == 2 and valeurs.count(0) == 1 : #le bot cherche s'il peut gêner le joueur 
                        cases = [c1, c2, c3]
                        jouer = False
                        grille[cases[valeurs.index(0)][0]][cases[valeurs.index(0)][1]] = tour
            if jouer == True :  #sinon, il joue aléatoirement en faisant une série de propositions aléatoires jusqu'à trouver une case libre 
                while True :
                    case_random = random.randint(0,2), random.randint(0,2) 
                    if grille[case_random[0]][case_random[1]] == 0 :
                        grille[case_random[0]][case_random[1]] = tour
                        jouer = False 
                        break
            tour = tour%2 + 1 #le tour passe au suivant 
        
        for event in pygame.event.get(): #détection des actions du joueur 
            if event.type == pygame.QUIT : #permet la fermeture de la fenêtre 
                runing = False
            if event.type == pygame.KEYDOWN : 
                if event.key == pygame.K_ESCAPE : #permet de mettre fin à la fonction 
                    runing = False
            if event.type == pygame.MOUSEBUTTONDOWN : #fait jouer le joueur en détectant un clic et en le localisant sur la grille 
                for i in range (3) :
                    x_screen = (info.current_w//2) - (1.5*t) + round(i*t)
                    for j in range(3) :
                        y_screen = (info.current_h//2) - (1.5*t) + round(j*t) 
                        rectangle = pygame.Rect(x_screen,y_screen,t,t)
                        if rectangle.collidepoint(event.pos) and tour == tour_self :
                            if grille[j][i] == 0 : #vérifie si la case est libre (sinon il ne se passe rien) 
                                grille[j][i] = tour 
                                tour = tour%2 + 1 #le tour passe au suivant 
        
        screen.fill(noir) #remise à 0 de l'écran (fond noir) 
        for i in range (3) : #affichage des cases 
            x_screen = (info.current_w//2) - (1.5*t) + round(i*t)
            for j in range(3) :
                y_screen = (info.current_h//2) - (1.5*t) + round(j*t)
                rectangle = pygame.Rect(x_screen,y_screen,t,t)
                screen.blit(etats_possibles[grille[j][i]], rectangle)
                pygame.draw.rect(screen,noir,(x_screen,y_screen,t,t), (info.current_h//200))
        pygame.display.flip() #met à jour l'affichage 
        clock.tick(60) #définition du nombre d'affichages par seconde 
        
        for i in range(3): #vérification des conditions de victoire : 
            if grille[i][0] == grille[i][1] == grille[i][2] != 0: #colonnes 
                if grille[i][1] == tour_self :
                    pygame.time.delay(500) 
                    return True
                else :
                    pygame.time.delay(500) 
                    return False 
            if grille[0][i] == grille[1][i] == grille[2][i] != 0: #lignes 
                if grille[1][i] == tour_self :
                    pygame.time.delay(500) 
                    return True
                else :
                    pygame.time.delay(500) 
                    return False 
        if grille[0][0] == grille[1][1] == grille[2][2] != 0: #diagonale 
            if grille[1][1] == tour_self :
                pygame.time.delay(500) 
                return True
            else :
                pygame.time.delay(500) 
                return False 
        if grille[0][2] == grille[1][1] == grille[2][0] != 0: #autre diagonale 
            if grille[0][2] == tour_self :
                pygame.time.delay(500) 
                return True
            else :
                pygame.time.delay(500) 
                return False
        
        if all(grille[i][j] != 0 for i in range (3) for j in range(3)) : #vérifie si toute la grille est pleine 
            grille = [[0 for i in range(3)]for j in range(3)] #si la grille est pleine, elle est réinitialisée 