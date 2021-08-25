#!/usr/bin/env python
import pygame 
from pygame import * #a retirer
from player import Player
class Game:
    def __init__(self):
        pygame.init()
        width = 1080
        height = 720
        self.screen = pygame.display.set_mode((width, height)) #Creer la fenetre du jeu
        pygame.display.set_caption("PyGame - Comet fall")
        self.background = pygame.image.load('assets/bg.jpg')
        self.player = Player()
        self.pressed = {}
    def walls(self, direction):
        if direction == 'right':
            return True if self.player.rect.x + self.player.rect.width < self.screen.get_width() else False
        elif direction == 'left':
            return True if self.player.rect.x > 0 else False
        
    def commandes(self):
        if self.pressed.get(pygame.K_RIGHT) and self.pressed.get(pygame.K_LEFT):
            print('POWER')
        elif self.pressed.get(pygame.K_RIGHT) and self.walls('right'):
            self.player.move('right')
        elif self.pressed.get(pygame.K_LEFT) and self.walls('left'):
            self.player.move('left')
            
    def initialisation(self):
        self.screen.blit(self.background, (0, -200)) #arriere plan
        self.screen.blit(self.player.image, self.player.rect)#appliquer l'image du player
        self.commandes()
        pygame.display.flip() #mettre a jour l'ecran
        
    def run(self):  
        clock = pygame.time.Clock()          
        running = True
        while running:
            self.initialisation() #INIT RPG GAME
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    self.pressed[event.key] = True
                elif event.type == pygame.KEYUP:
                    self.pressed[event.key] = False

            clock.tick(60) #SET FPS
        pygame.quit() #Quit