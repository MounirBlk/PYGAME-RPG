#!/usr/bin/env python
import pygame 
from pygame import * #a retirer
import random
from monster import *

class Comet(pygame.sprite.Sprite):
    def __init__(self, comet_event):
        super().__init__()
        self.comet_event = comet_event
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.speed = random.randint(1, 3)
        screen_width = self.comet_event.game.screen.get_width()
        self.rect.x = random.randint(20, screen_width * 0.9)
        self.rect.y = - random.randint(0, screen_width / 2)
        
    def remove(self):
        self.comet_event.all_comets.remove(self)
        if len(self.comet_event.all_comets) == 0: # check si le nb de comets est a 0
            self.comet_event.reset_percent()
            self.comet_event.game.start()
        
    def fall(self):
        self.rect.y += self.speed
        
        if self.rect.y >= 525:
            self.remove()
            if len(self.comet_event.all_comets) == 0: # check s'il y a des boules de feu en jeu
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False
        
        if self.comet_event.game.check_collision(self, self.comet_event.game.all_persons):
            self.remove()
            self.comet_event.game.player.get_damage(20)