#!/usr/bin/env python
import pygame 
from pygame import * #a retirer

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.speed = 10 #pixel
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 500
        
    def move(self, direction):
        self.facing = direction
        if direction == 'right':
            self.rect.x += self.speed
        if direction == 'left':
            self.rect.x -= self.speed
