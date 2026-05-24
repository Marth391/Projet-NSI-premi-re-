import pygame
import rush
import balles
import tic_tac_toe
import pendu

pygame.init() 
screen = pygame.display.set_mode((0,0)) 
clock = pygame.time.Clock()

pendu.pendu(screen,clock)

tic_tac_toe.tic_tac_toe(screen, clock)

rush.rush(screen,clock) 

balles.balles(screen,clock)

pygame.quit() 