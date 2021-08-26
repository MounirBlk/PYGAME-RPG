#!/usr/bin/env python
import pygame 
from pygame import * #a retirer
import random
import math
import animation
class Monster(animation.AnimateSprite):
    def __init__(self, game, name, size, offset = 0):
        super().__init__(name, size)
        self.game = game
        health = 100
        self.health = health
        self.max_health = health
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = math.ceil(self.game.screen.get_width() * 0.9) - random.randint(0, 150)
        self.rect.y = math.ceil(self.game.player.rect.y + (self.game.player.rect.y / 12.5)) - offset
        self.loot_amount = 10
        self.speed = random.randint(2, 4)
        self.start_animation()
    
    def set_loot_amount(self, amount):
        self.loot_amount = amount
        
    def get_damage(self, amount):
        self.health -= amount # infliger des dégats au monstre
        if self.health <= 0: # verifier le nombre de points de vie
            # reapparaitre comme un nouveau monstre (possibilité de supprimer le monstre avec self.game.all_monsters.remove(self))
            '''self.rect.x = math.ceil(self.game.screen.get_width() * 0.9) - random.randint(0, 150)
            self.rect.y = math.ceil(self.game.player.rect.y + (self.game.player.rect.y / 12.5))
            self.health = self.max_health
            self.speed = random.randint(2, 3)'''
            self.game.all_monsters.remove(self)
            self.game.add_score(self.loot_amount)
            if self.game.comet_event.is_full_loaded(): # check si la barre d'evenement de comet est chargé
                self.game.all_monsters.remove(self)
                self.game.comet_event.attempt_fall() # declencher la pluie de cometes
            else:
                tabTypeMonstersClass = [Mummy, Alien]
                typeMonsterClass = tabTypeMonstersClass[random.randint(0, len(tabTypeMonstersClass) - 1)]
                self.game.spawn_monster(typeMonsterClass)
                
    def update_animation(self):
        self.animate(loop = True) # method from Class AnimateSprite -> animation.py
        
    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 15, self.max_health, 5]) # dessine le bg de la barre de vie
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 15, self.health, 5]) # dessine la barre de vie

    def forward(self):
        if not self.game.check_collision(self, self.game.all_persons): # le deplacement ne se fait que si il n'y a pas de collision avec un groupe de personne
            self.rect.x -= self.speed
        else:
            self.game.player.get_damage(self.attack)
            #infliger des dégats au player si le monstre est en collision

class Mummy(Monster):
    def __init__(self, game):
        super().__init__(game, 'mummy', (130, 130))
        self.set_loot_amount(20)
class Alien(Monster):
    def __init__(self, game):
        super().__init__(game, 'alien', (300, 300), offset = 130)
        health = 250
        self.health = health
        self.max_health = health
        self.attack = 0.5
        self.speed = random.randint(1, 2)
        self.set_loot_amount(80)

