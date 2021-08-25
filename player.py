#!/usr/bin/env python
import pygame 
from pygame import * #a retirer
from projectile import Projectile#a retirer

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.speed = 10 #pixel
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 500
        
    def get_damage(self, amount):
        if self.health - amount > amount: # verifier le nombre de points de vie
            self.health -= amount # infliger des dégats au player
        
    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 25, self.max_health, 7]) # dessine le bg de la barre de vie
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 25, self.health, 7]) # dessine la barre de vie
        
    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))
        
    def move(self, direction):
        if not self.game.check_collision(self, self.game.all_monsters): # si le joueur n'est pas en collision avec un monstre
            if direction == 'right':
                self.rect.x += self.speed
        if direction == 'left':
            self.rect.x -= self.speed
