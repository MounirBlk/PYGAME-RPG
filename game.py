#!/usr/bin/env python
import pygame 
from pygame import * #a retirer

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1080, 720)) #Creer la fenetre du jeu
        pygame.display.set_caption("PyGame - Comet fall")
        self.background = pygame.image.load('assets/bg.jpg')
        
    def run(self):  
        clock = pygame.time.Clock()          
        running = True
        while running:
            self.screen.blit(self.background, (0, -200)) #arriere plan
            pygame.display.flip() #mettre a jour l'ecran
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            clock.tick(60) #SET FPS
        pygame.quit() #Quit