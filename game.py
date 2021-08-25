#!/usr/bin/env python
import pygame 
from pygame import * #a retirer
from player import Player
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1080, 720)) #Creer la fenetre du jeu
        pygame.display.set_caption("PyGame - Comet fall")
        self.background = pygame.image.load('assets/bg.jpg')
        self.player = Player(self.screen)
        self.pressed = {}
    def walls(self, direction):
        if direction == 'right':
            return True if self.player.rect.x + self.player.rect.width < self.screen.get_width() else False
        elif direction == 'left':
            return True if self.player.rect.x > 0 else False
        
    def commandes(self):
        if self.pressed.get(pygame.K_RIGHT) and self.pressed.get(pygame.K_LEFT):
            self.player.health = self.player.health + 1 if self.player.health < self.player.max_health else self.player.health
        elif self.pressed.get(pygame.K_RIGHT) and self.walls('right'):
            self.player.move('right')
        elif self.pressed.get(pygame.K_LEFT) and self.walls('left'):
            self.player.move('left')
            
    def initialisation(self):
        self.screen.blit(self.background, (0, -200)) #arriere plan
        self.screen.blit(self.player.image, self.player.rect)#appliquer l'image du player
        for projectile in self.player.all_projectiles:
            projectile.move()
        self.player.all_projectiles.draw(self.screen) #appliquer l'ensemble des images du groupe de projectiles
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
                elif event.type == pygame.KEYDOWN: #touche appuyé
                    self.pressed[event.key] = True
                    if event.key == pygame.K_SPACE: 
                        self.player.launch_projectile() # lancement du projectile
                    
                elif event.type == pygame.KEYUP: #touche non appuyé
                    self.pressed[event.key] = False

            clock.tick(60) #SET FPS
        pygame.quit() #Quit