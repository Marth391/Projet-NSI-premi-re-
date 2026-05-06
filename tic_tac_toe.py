def tic_tac_toe(screen,clock) :
    import pygame 
    noir = (000,000,000)
    croix = pygame.image.load("croix.png")
    rond = pygame.image.load("rond.png")
    fond_blanc = pygame.image.load("fond blanc.png")
    
    initialisation = True 
    clic = False
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
        liste_cases = []
        for i in range (3) :
            x_screen = (info.current_w//2) - (1.5*t) + round(i*t)
            for j in range(3) :
                y_screen = (info.current_h//2) - (1.5*t) + round(j*t)
                rectangle = pygame.Rect(x_screen,y_screen,t,t)
                screen.blit(etats_possibles[grille[j][i]], rectangle)
                pygame.draw.rect(screen,noir,(x_screen,y_screen,t,t), (info.current_h//200))
        pygame.display.flip()
        clock.tick(60)
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
                        if rectangle.collidepoint(event.pos) :
                            if grille[j][i] == 0 :
                                if tour == 1 :
                                    tour = 2
                                elif tour == 2 :
                                    tour = 1
                                grille[j][i] = tour 

