import pygame
import rush
import balles
import tic_tac_toe
pygame.init() 
screen = pygame.display.set_mode((0,0)) 
clock = pygame.time.Clock()

tic_tac_toe.tic_tac_toe(screen, clock)

rush.rush(screen,clock) 

balles.balles(screen,clock)

pygame.quit() 