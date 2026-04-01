def rush(screen,clock) :
    import pygame 
    rouge = (255,000,000)
    vert = (000,255,000)
    blanc = (255,255,255)
    jaune = (255,255,000)
    violet = (255,000,255)
    orange = (255,150,80)
    bleu = (000,000,255)
    noir = (000,000,000) 

    class Voiture :
        def __init__(self, x, y, longueur, direc,color) :
            self.x = x
            self.y = y
            self.longueur = longueur
            self.direc = direc 
            self.color = color 
            
        def sens(self,x,y) :
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
            if self.direc == 0 :
                for i in range(self.longueur) :
                    grille[self.y][self.x + i] = self.color
            if self.direc == 1 :
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
                try : 
                    if grille[self.y+self.longueur][self.x] == blanc :
                        self.y += 1 
                except : pass
            
            if sens == "debutx" :
                try :
                    if grille[self.y][self.x - 1] == blanc and self.x -1 >= 0:
                        self.x -= 1
                except : pass 
            if sens == "debuty" :
                try :
                    if grille[self.y-1][self.x] == blanc and self.y -1 >= 0 :
                        self.y -= 1 
                except : pass
            pass 


    voitures = [Voiture(0,0,3,0,jaune), Voiture(3,0,3,0,violet), Voiture(2,1,3,0,bleu),Voiture(0,2,2,0,rouge), Voiture(2,2,2,1,vert), Voiture(0,4,3,0,jaune), Voiture(5,4,2,1,orange)]

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
                x_interraction = (coordonnee[0] - (info.current_w//2 - 3*(info.current_h//10)))//(info.current_h//10)  
                y_interraction = (coordonnee[1] - (info.current_h//5))//(info.current_h//10)
                for v in voitures :
                    if v.sens(x_interraction,y_interraction) != False :
                        v.avancer(v.sens(x_interraction,y_interraction))
        grille = [[blanc for i in range(6)]for j in range(6)]
        for v in voitures :
            v.sur_grille()
        for i in range (6) :
            x_screen = (info.current_w//2) - (3*(info.current_h//10)) + (i*(info.current_h//10))
            for j in range(6) : 
                y_screen = info.current_h//5 + round(j*(info.current_h//10))
                pygame.draw.rect(screen,grille[j][i],(x_screen,y_screen,info.current_h//10,info.current_h//10)) 
        clock = 60
        pygame.display.flip() 