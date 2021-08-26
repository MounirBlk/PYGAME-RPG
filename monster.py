#!/usr/bin/env python
import pygame 
from pygame import * #a retirer
import random
import math
class Monster(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = math.ceil(self.game.screen.get_width() * 0.9) - random.randint(0, 150)
        self.rect.y = math.ceil(self.game.player.rect.y + (self.game.player.rect.y / 12.5))
        self.speed = random.randint(2, 4)
        
    def get_damage(self, amount):
        self.health -= amount # infliger des dégats au monstre
        if self.health <= 0: # verifier le nombre de points de vie
            # reapparaitre comme un nouveau monstre (possibilité de supprimer le monstre avec self.player.all_monsters.remove(self) # supprimer le monstre )
            self.rect.x = math.ceil(self.game.screen.get_width() * 0.9) - random.randint(0, 150)
            self.rect.y = math.ceil(self.game.player.rect.y + (self.game.player.rect.y / 12.5))
            self.health = self.max_health
            self.speed = random.randint(2, 3)
            
            if self.game.comet_event.is_full_loaded(): # check si la barre d'evement de comet est chargé
                self.game.all_monsters.remove(self)
                self.game.comet_event.attempt_fall() # declencher la pluie de cometes

        
    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 15, self.max_health, 5]) # dessine le bg de la barre de vie
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 15, self.health, 5]) # dessine la barre de vie

    def forward(self):
        if not self.game.check_collision(self, self.game.all_persons): # le deplacement ne se fait que si il n'y a pas de collision avec un groupe de personne
            self.rect.x -= self.speed
        else:
            self.game.player.get_damage(self.attack)
            #infliger des dégats au player si le monstre est en collision

