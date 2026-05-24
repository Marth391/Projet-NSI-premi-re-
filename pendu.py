import random
import pygame

def pendu(screen,clock) : 
    pygame.init() 
    def liste_de_mots ():
        """Cette fonction définit une liste de mots utilisables pour le jeu à partir d'un fichier txt"""
        fichier = list(open("dico.txt")) #ici on convertie le fichier txt en liste de mots 
        
        for i in range (len(fichier)) :
            resultat = ""
            for a in range (len(fichier[i])-1) :     #on supprime les retours à la ligne 
                resultat += fichier[i][a]
            fichier[i] = resultat
        return fichier

    def epeler(mot) :
        """Cette fonction renvoie toutes les lettres d'un mot choisit sous la forme d'un tableau."""
        tableau = [None for i in range (len(mot))]
        for i in range(len(mot)) :
            tableau[i] = mot[i]
        return tableau

    def draw_text(text, font, color, surface, x, y):
        """Cette fonction permet d'écrire du texte centré sur une surface."""
        img = font.render(text, True, color)
        rect = img.get_rect(center=(x, y))
        surface.blit(img, rect)
        
    def draw_text2(text, font, color, x, y):
        """Cette fonction permet d'écrire du texte sur une surface sans qu'il soit centré."""
        img = font.render(text, True, color)
        screen.blit(img, (x,y))
        
    text_font_title = pygame.font.SysFont("Calibri",150, bold=True) #Police pour le titre du jeu 

    text_font = pygame.font.SysFont(False,80) #Police pour les petits textes 

    fichier = liste_de_mots() #on prépare un tableau comportant la liste de mots du dico 

    """On définie les différents objets constituant le dessin du pendu."""

    def socle () :
        return (pygame.draw.line(screen,(0,0,0), ((screen.get_width() // 2) - 200, 800), ((screen.get_width() // 2) + 200,800), 10))
    def poteau():
        return (pygame.draw.line(screen,(0,0,0), ((screen.get_width()//2), 800), ((screen.get_width()//2), 300), 10))
    def barre_haut():
        return (pygame.draw.line(screen,(0,0,0), ((screen.get_width()//2)-4, 300), ((screen.get_width()//2) + 200, 300), 10))
    def equere_haut() :
        return (pygame.draw.line(screen,(0,0,0), ((screen.get_width()//2) + 54, 296), ((screen.get_width()//2),350), 10))
    def corde() :
        return (pygame.draw.line(screen,(0,0,0), ((screen.get_width()//2) + 200, 296), ((screen.get_width()//2) + 200, 350), 10))
    def tete() :
        return (pygame.draw.circle(screen,(0,0,0),((screen.get_width()//2)+200,400), 50, 4))
    def corps():
        return (pygame.draw.line(screen,(0,0,0), ((screen.get_width()//2) + 200, 448), ((screen.get_width()//2) + 200, 550), 3))
    def bras() :
        return (pygame.draw.line(screen,(0,0,0), ((screen.get_width()//2) + 200, 480),((screen.get_width()//2)+225,525), 3)), (pygame.draw.line(screen,(0,0,0), ((screen.get_width()//2) + 200, 480),((screen.get_width()//2)+175,525), 3))
    def jambes() :
        return (pygame.draw.line(screen,(0,0,0), ((screen.get_width()//2) + 200, 550),((screen.get_width()//2)+225,625), 3)), (pygame.draw.line(screen,(0,0,0), ((screen.get_width()//2) + 200, 550),((screen.get_width()//2)+175,625), 3))

    bonhomme = [socle, poteau, barre_haut,equere_haut,corde,tete,corps,bras,jambes] #on met tous les éléments du bonhomme dans une liste pour pouvoir l'utiliser plus tard dans une boucle. 
    
    """On initialise le jeu""" 
    liste_lettre = [] #on initialise la liste des lettres déjà essayées 
    mot = fichier[random.randint(0,len(fichier))] #on sélection le mot de la manche dans le tableau comportant les termes du dico 
    mot = epeler(mot) #on convertie le mot en série de lettre pour pouvoir traiter celles-ci séparément 
    vie = 0 #on initialise le compteur de vie / une fois que celui-ci atteind 9, on a perdu 
    tableau = ["_ " for i in range (len(mot))] #on définie le tableau qui sera affiché / pour l'instant nous n'avons que des tirets car aucune lettre n'a encore été trouvée 
    
    affichage = "" 
    for i in range(len(tableau)) :
        affichage += tableau[i]                                                   #on affiche tous les éléments du tableau à la suite, sans crochets 
    draw_text(affichage, text_font, (0,0,0), screen, screen.get_width()//2, 1000)

    running = True #on règle running sur True pour avoir une boucle infinie 
    
    while running : #boucle infinie tant que running = True
        """C'est la boucle d'une manche, tant qu'elle est active, le mot doit être deviné et n'est pas changé."""
        
        for event in pygame.event.get(): #on prend connaissance des dernières actions 
            
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) :    #pour pouvoir fermer la fenêtre du jeu
                running = False
            
            elif event.type == pygame.KEYDOWN and event.key != pygame.K_TAB and event.key != pygame.K_LALT : #on regarde si une touche est pressée / on epêche la détection du alt-tab comme touches dans le pendu 
                lettre = event.unicode
                compteur_faute = 0
                for i in range(len(mot)) :
                    if str(mot[i]) == str(lettre) :
                        tableau[i] = lettre
                    else :
                        compteur_faute += 1
                if compteur_faute == len(mot):
                    vie += 1
                    liste_lettre.append(f"{lettre}  ")
        
        screen.fill((255,255,255))
        draw_text("Le jeu du pendu", text_font_title, (0,0,0), screen, screen.get_width()//2, 150)
        affichage = ""
        for i in range(len(tableau)) :
            affichage += tableau[i] 
        draw_text(affichage, text_font, (0,0,0), screen, screen.get_width()//2, 1000)
        affichage = ""
        for i in range(len(liste_lettre)) :
            affichage += liste_lettre[i]
        draw_text2(affichage, text_font, (255,0,0), 50, 850)
        
        for i in range(vie) :
            bonhomme[i]()
        
        pygame.display.flip() #pour update l'écran
        clock.tick(5) #on règle les fps sur 5
        affichage = ""
        for i in range(len(mot)) :
            affichage += mot[i]
        if vie == 9 :
            pygame.time.delay(2000) 
            screen.fill((255,255,255))
            draw_text("Perdu", text_font_title, (0,0,0), screen, screen.get_width()//2, 450)
            draw_text(f"le mot était {affichage} !", text_font, (0,0,0), screen, screen.get_width()//2, 800)
            pygame.display.flip()
            pygame.time.delay(2000) 
            return False 
            
        elif mot == tableau :
            screen.fill((255,255,255))
            draw_text("Gagné", text_font_title, (0,0,0), screen, screen.get_width()//2, 450)
            draw_text(f"le mot était {affichage} !", text_font, (0,0,0), screen, screen.get_width()//2, 800)
            pygame.display.flip()
            pygame.time.delay(2000) 
            return True 
