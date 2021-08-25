#!/usr/bin/env python
import pygame 
from pygame import * #a retirer

class Monster(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = int(self.game.screen.get_width() * 0.9)
        self.rect.y = int(self.game.player.rect.y + (self.game.player.rect.y / 12.5))
        self.speed = 5
        
    def forward(self):
        if not self.game.check_collision(self, self.game.all_persons): # le deplacement ne se fait que si il n'y a pas de collision avec un groupe de personne
            self.rect.x -= self.speed
        

