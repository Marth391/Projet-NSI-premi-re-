import pygame
pygame.init() #initialisation des différents modules de pygame 
screen = pygame.display.set_mode((400,400)) #création de l'écran 

running = True #pour faire tourner le programme à l'infini si running est dans une boucle while 

image = pygame.image.load("ballon.png").convert() #définition des différentes images 

clock = pygame.time.Clock() #on définie la vitesse de jeu (FPS) dans la variable clock

x = 0
            #coordonnées de l'image 
y = 0 

while running : #boucle infinie tant que running = True
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:    #pour pouvoir fermer la fenêtre 
            running = False
            
    pressed = pygame.key.get_pressed()  #pressed sert maintenant à avoir les touches pressées 
    
    if pressed[pygame.K_LEFT] : 
        x -= 1 
    if pressed[pygame.K_RIGHT] :
        x += 1
    if pressed[pygame.K_UP] :       #dans ce bloque on détecte la touche pressée et on fait une action en fonction 
        y -= 1 
    if pressed[pygame.K_DOWN] :
        y += 1  
        
    screen.fill((0,0,0)) #on remplie le fond en noir pour réinitialiser l'écran et ne pas avoir les anciennes images 
    screen.blit(image,(x,y)) #pour affichier l'objet "image" à l'écran "screen" 
    pygame.display.flip() #pour update l'écran
    clock.tick(60) #on règle les fps sur 60 
    
pygame.quit() #si on sort de la boucle, on ferme la fenêtre pygame 