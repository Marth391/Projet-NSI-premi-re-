import random
import pygame 

def jeu_timing(screen, clock) :
    boucle = True
    sens = 1 
    zones_possibles = [10,13,15,20,25,30,35,40,45,50,55]
    tour_last = 0 
    tour = 0
    hauteur = (pygame.display.Info()).current_h
    largeur = (pygame.display.Info()).current_w
    hauteur_bande = hauteur // 25
    x = largeur//2
    zone_detection = pygame.Rect(random.randint(0,largeur - (largeur // zones_possibles[tour])),hauteur//2 - hauteur_bande//2, largeur//zones_possibles[tour],hauteur_bande)
    curseur = pygame.Rect(x,hauteur//2 - hauteur_bande//2,4,hauteur_bande) 
    while boucle == True and tour < 10 :
        dt = clock.tick(60) / 1000 
        event = pygame.event.get()
        for e in event :
            if e.type == pygame.QUIT :
                boucle = False
            if e.type == pygame.KEYDOWN :
                if e.key == pygame.K_ESCAPE :
                    boucle = False 
                if curseur.colliderect(zone_detection) :
                    tour += 1
                """else :
                    return tour """
        if tour > tour_last and tour < 10 :
            tour_last += 1
            zone_detection = pygame.Rect(random.randint(0,largeur - (largeur // zones_possibles[tour])),hauteur//2 - hauteur_bande//2, largeur//zones_possibles[tour],hauteur_bande)
            
        vitesse = (zones_possibles[tour] /3) * 60 
        if x <= 0 :
            sens = 1
        elif x >= largeur - 4 :
            sens = -1
        x += sens * vitesse * dt 
        curseur = pygame.Rect(x,hauteur//2 - hauteur_bande//2,4,hauteur_bande) 
        bande = pygame.Rect(0,(hauteur//2)-(hauteur_bande//2),largeur,hauteur_bande)
        screen.fill((0,0,0))
        pygame.draw.rect(screen,(100,100,100),bande)
        pygame.draw.rect(screen,(100,100,255),zone_detection) 
        pygame.draw.rect(screen,(255,255,255),curseur)
        pygame.display.flip()
    return tour 
        