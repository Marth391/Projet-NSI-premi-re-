import pygame
import rush
import balles 
pygame.init() 
screen = pygame.display.set_mode((0,0)) 
clock = pygame.time.Clock()

rush.rush(screen,clock) 

balles.balles(screen,clock)

pygame.quit() 