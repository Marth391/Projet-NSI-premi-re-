def tic_tac_toe(screen,clock) : 
    import pygame
    import random 
    noir = (000,000,000)
    croix = pygame.image.load("croix.png")
    rond = pygame.image.load("rond.png")
    fond_blanc = pygame.image.load("fond blanc.png")
    
    combos = [
                ((0,0), (0,1), (0,2)), # Lignes
                ((1,0), (1,1), (1,2)),
                ((2,0), (2,1), (2,2)),
                ((0,0), (1,0), (2,0)), # Colonnes
                ((0,1), (1,1), (2,1)),
                ((0,2), (1,2), (2,2)),
                ((0,0), (1,1), (2,2)), # Diagonales
                ((0,2), (1,1), (2,0))
                ]
    
    initialisation = True
    tour_self = random.randint(1,2) 
    tour = 1

    runing = True
    
    while runing :
        info = pygame.display.Info()
        t = info.current_h//3.5 
        croix = pygame.transform.scale(croix,(t,t))
        fond_blanc = pygame.transform.scale(fond_blanc,(t,t))
        rond = pygame.transform.scale(rond,(t,t))
        if initialisation :
            grille = [[0 for i in range(3)]for j in range(3)]
        initialisation = False 
        etats_possibles = [fond_blanc, rond, croix]
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT :
                runing = False
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE :
                    runing = False
            if event.type == pygame.MOUSEBUTTONDOWN :
                for i in range (3) :
                    x_screen = (info.current_w//2) - (1.5*t) + round(i*t)
                    for j in range(3) :
                        y_screen = (info.current_h//2) - (1.5*t) + round(j*t)
                        rectangle = pygame.Rect(x_screen,y_screen,t,t)
                        if rectangle.collidepoint(event.pos) and tour == tour_self :
                            if grille[j][i] == 0 :
                                grille[j][i] = tour
                                if tour == 1 :
                                    tour = 2
                                elif tour == 2 :
                                    tour = 1
        for i in range (3) :
            x_screen = (info.current_w//2) - (1.5*t) + round(i*t)
            for j in range(3) :
                y_screen = (info.current_h//2) - (1.5*t) + round(j*t)
                rectangle = pygame.Rect(x_screen,y_screen,t,t)
                screen.blit(etats_possibles[grille[j][i]], rectangle)
                pygame.draw.rect(screen,noir,(x_screen,y_screen,t,t), (info.current_h//200))
        pygame.display.flip()
        clock.tick(60)
        if tour != tour_self and not (all(grille[i][j] != 0 for i in range (3) for j in range(3))):
            jouer = True
            for c1, c2, c3 in combos :
                if jouer == True : 
                    valeurs = [grille[c1[0]][c1[1]], grille[c2[0]][c2[1]], grille[c3[0]][c3[1]]]
                    if valeurs.count(tour) == 2 and valeurs.count(0) == 1 :
                        cases = [c1, c2, c3]
                        index = valeurs.index(0)
                        jouer = False
                        pygame.time.delay(500) 
                        grille[cases[index][0]][cases[index][1]] = tour
            for c1, c2, c3 in combos :
                if jouer == True : 
                    valeurs = [grille[c1[0]][c1[1]], grille[c2[0]][c2[1]], grille[c3[0]][c3[1]]]
                    if valeurs.count(tour_self) == 2 and valeurs.count(0) == 1 :
                        cases = [c1, c2, c3]
                        index = valeurs.index(0)
                        jouer = False
                        pygame.time.delay(500) 
                        grille[cases[index][0]][cases[index][1]] = tour
            if jouer == True :
                boucle = True
                while boucle :
                    case_random = random.randint(0,2), random.randint(0,2) 
                    if grille[case_random[0]][case_random[1]] == 0 :
                        pygame.time.delay(500) 
                        grille[case_random[0]][case_random[1]] = tour
                        boucle = False
                        jouer = False 
                        break          
            if tour == 1 :
                tour = 2
            elif tour == 2 :
                tour = 1
                
        for i in range(3):
            if grille[i][0] == grille[i][1] == grille[i][2] != 0:
                if grille[i][1] == tour_self :
                    pygame.time.delay(500) 
                    return True
                else :
                    pygame.time.delay(500) 
                    return False 
            if grille[0][i] == grille[1][i] == grille[2][i] != 0:
                if grille[1][i] == tour_self :
                    pygame.time.delay(500) 
                    return True
                else :
                    pygame.time.delay(500) 
                    return False 
        if grille[0][0] == grille[1][1] == grille[2][2] != 0:
            if grille[1][1] == tour_self :
                pygame.time.delay(500) 
                return True
            else :
                pygame.time.delay(500) 
                return False 
        if grille[0][2] == grille[1][1] == grille[2][0] != 0:
            if grille[0][2] == tour_self :
                pygame.time.delay(500) 
                return True
            else :
                pygame.time.delay(500) 
                return False
        if all(grille[i][j] != 0 for i in range (3) for j in range(3)) :
            grille = [[0 for i in range(3)]for j in range(3)]
        
