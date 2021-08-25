#!/usr/bin/env python
import pygame 
from pygame import * #a retirer

class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.speed = 5
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0
        
    def rotate(self):
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1) # tourner le projectile
        self.rect = self.image.get_rect(center = self.rect.center)
        
    def remove(self):
        self.player.all_projectiles.remove(self) # supprimer le projectile 
        
    def move(self):
        self.rect.x += self.speed # deplacement du projectile
        self.rotate()
        if self.player.game.check_collision(self, self.player.game.all_monsters): # verifier si le projectile entre en collision avec un monstre
            self.remove() 
        if self.rect.x > self.player.game.screen.get_width():# verifier si notre projectile n'est plus présent sur l'ecran
            self.remove()
        