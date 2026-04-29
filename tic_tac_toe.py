def tic_tac_toe(screen,clock) :
    import pygame 
    rouge = (255,000,000)
    blanc = (255,255,255)
    bleu = (000,000,255)
    noir = (000,000,000)
    croix = pygame.image.load("croix.png")
    rond = pygame.image.load("rond.png")
    fond_blanc = pygame.image.load("fond blanc.png") 


    class Case :
        def __init__(self, x, y, etat) :
            self.x = x
            self.y = y
            self.etat = etat
            
    runing = True

    while runing :
        info = pygame.display.Info()
        croix = pygame.transform.scale(croix,(info.current_h//3.5,info.current_h//3.5))
        fond_blanc = pygame.transform.scale(fond_blanc,(info.current_h//3.5,info.current_h//3.5))
        rond = pygame.transform.scale(rond,(info.current_h//3.5,info.current_h//3.5))
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT :
                runing = False
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE :
                    runing = False
            if event.type == pygame.MOUSEBUTTONDOWN :
                coordonnee = pygame.mouse.get_pos()
                x_interraction = round((coordonnee[0] - (info.current_w//2 - 1.5*(info.current_h//3.5)))//(info.current_h//3.5)) 
                y_interraction = round((coordonnee[1] - (info.current_h//3))//(info.current_h//3.5)) + 1 
        
        grille = [[blanc for i in range(3)]for j in range(3)]
        for i in range (3) :
            x_screen = (info.current_w//2) - (1.5*(info.current_h//3.5)) + round(i*(info.current_h//3.5))

            for j in range(3) :
                y_screen = (info.current_h//2) - (1.5*(info.current_h//3.5)) + round(j*(info.current_h//3.5))
                rectangle = pygame.Rect((x_screen,y_screen,info.current_h//3.5,info.current_h//3.5))
                screen.blit(rond, rectangle)
                
                
                pygame.draw.rect(screen,noir,(x_screen,y_screen,info.current_h//3.5,info.current_h//3.5), (info.current_h//200))
        pygame.display.flip()
        clock.tick(60) 
