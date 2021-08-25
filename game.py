#!/usr/bin/env python
import pygame 
from pygame import * #a retirer
from player import Player
from monster import Monster

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1080, 720)) #Creer la fenetre du jeu
        pygame.display.set_caption("PyGame - Comet fall")
        self.background = pygame.image.load('assets/bg.jpg')
        self.all_persons = pygame.sprite.Group()
        self.player = Player(self)
        self.all_persons.add(self.player)
        self.all_monsters = pygame.sprite.Group() # groupe de monstres
        self.pressed = {}
        self.spawn_monster()
        self.spawn_monster()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
    
    def spawn_monster(self):
        self.all_monsters.add(Monster(self))
        
    def walls(self, direction):
        if direction == 'right':
            return True if self.player.rect.x + self.player.rect.width < self.screen.get_width() else False
        elif direction == 'left':
            return True if self.player.rect.x > 0 else False
        
    def commandes(self):
        if self.pressed.get(pygame.K_RIGHT) and self.pressed.get(pygame.K_LEFT):
            self.player.health = self.player.health + 0.5 if self.player.health < self.player.max_health else self.player.health
        elif self.pressed.get(pygame.K_RIGHT) and self.walls('right'):
            self.player.move('right')
        elif self.pressed.get(pygame.K_LEFT) and self.walls('left'):
            self.player.move('left')
            
    def initialisation(self):
        self.screen.blit(self.background, (0, -200)) #arriere plan
        self.screen.blit(self.player.image, self.player.rect) #appliquer l'image du player
        
        self.player.update_health_bar(self.screen) # actualiser la bar de vie du joueur
        
        for projectile in self.player.all_projectiles:
            projectile.move() # mouvement des projectiles
        for monster in self.all_monsters:
            monster.forward() # avancement des monstres
            monster.update_health_bar(self.screen)
            
        self.player.all_projectiles.draw(self.screen) #appliquer l'ensemble des images du groupe de projectiles
        self.all_monsters.draw(self.screen) #appliquer l'ensemble des images du groupe de monstres
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
                        if not self.pressed.get(pygame.K_RIGHT) or not self.pressed.get(pygame.K_LEFT):
                            self.player.launch_projectile() # lancement du projectile
                    
                elif event.type == pygame.KEYUP: #touche non appuyé
                    self.pressed[event.key] = False

            clock.tick(60) #SET FPS
        pygame.quit() #Quit