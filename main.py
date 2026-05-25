import pygame
import rush
import balles
import tic_tac_toe
import pendu
import jeu_timing

pygame.init() 
screen = pygame.display.set_mode((0,0)) 
clock = pygame.time.Clock()

jeu_timing.jeu_timing(screen, clock) 

pendu.pendu(screen,clock)

tic_tac_toe.tic_tac_toe(screen, clock)

rush.rush(screen,clock) 

balles.balles(screen,clock)

pygame.quit() 