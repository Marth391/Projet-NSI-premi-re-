class Voiture :
    def __init__(self, x, y, longueur, direc,color) :
        self.x = x
        self.y = y
        self.longueur = longueur
        self.direc = direc 
        self.color = color 
    
    def draw(self) :
        if self.direc==0 :
            for i in range (self.longueur) :
                grille[self.y][self.x + i] = f"{self.color}⬛\033[0m"
        else :
            for i in range (self.longueur) :
                grille[self.y + i][self.x] = f"{self.color}⬛\033[0m"
        
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
    
    def avancer(self, sens) :
        if sens == "finx" :
            try : 
                if grille[self.y][self.x + self.longueur] == "⬜" :
                    self.x += 1 
            except : pass
        if sens == "finy" :
            try : 
                if grille[self.y+self.longueur][self.x] == "⬜" :
                    self.y += 1 
            except : pass
        
        if sens == "debutx" :
            try :
                if grille[self.y][self.x - 1] == "⬜" :
                    self.x -= 1
            except : pass 
        if sens == "debuty" :
            try :
                if grille[self.y-1][self.x] == "⬜" :
                    self.y -= 1 
            except : pass
        pass 

def afficher() :
    for i in grille :
        memo = ""
        for j in i :
            memo += j
        print(memo) 
    
grille = [["⬜" for i in range(6)]for j in range(6)]
voitures = [Voiture(1,2,3,0,"\033[31m"), Voiture(0,1,3,1,"\033[32m"),Voiture(5,3,3,1,"\033[33m")]
runing = True

while runing :
    clic = input()
    try :
        for v in voitures :
            sens = v.sens(int(clic[0]),int(clic[1]))
            if sens != False :
                v.avancer(sens)
    except : pass 
    grille = [["⬜" for i in range(6)]for j in range(6)]
    for v in voitures :
        v.draw()
    afficher()
    if grille[2][5] == "\33[31m⬛\33[0m" :
        print ("gagner")
        runing = False
