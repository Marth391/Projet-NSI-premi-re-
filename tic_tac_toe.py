def tic_tac_toe(screen,clock) :
    import pygame 
    rouge = (255,000,000)
    blanc = (255,255,255)
    bleu = (000,000,255)
    noir = (000,000,000) 

    class Case :
        def __init__(self, x, y, etat) :
            self.x = x
            self.y = y
            self.etat = etat
            
    runing = True

    while runing :
        info = pygame.display.Info()
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT :
                runing = False
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE :
                    runing = False
            if event.type == pygame.MOUSEBUTTONDOWN :
                coordonnee = pygame.mouse.get_pos()
                x_interraction = round((coordonnee[0] - (info.current_w//2 - 1.5*(info.current_h//3.5)))//(info.current_h//3.5)) 
                y_interraction = round((coordonnee[1] - (info.current_h//3))//(info.current_h//3.5))
                print(x_interraction, y_interraction) 
        
        grille = [[blanc for i in range(3)]for j in range(3)]
        for i in range (3) :
            x_screen = (info.current_w//2) - (1.5*(info.current_h//3.5)) + round(i*(info.current_h//3.5))
            for j in range(3) :
                y_screen = (info.current_h//2) - (1.5*(info.current_h//3.5)) + round(j*(info.current_h//3.5))
                pygame.draw.rect(screen,grille[j][i],(x_screen,y_screen,info.current_h//3.5,info.current_h//3.5))
        pygame.display.flip()
        clock.tick(60) 
