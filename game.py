#!/usr/bin/env python
import pygame 
from pygame import * #a retirer
from player import Player
from monster import *
from comet_event import CometFallEvent
import math
import random

FPS = 60
class Game:
    def __init__(self):
        self.is_playing = False # definir si le jeu a commencé ou pas
        pygame.init()
        self.screen = pygame.display.set_mode((1080, 720)) #Creer la fenetre du jeu
        pygame.display.set_caption("PyGame - Comet fall")
        self.background = pygame.image.load('assets/bg.jpg')
        self.init_menu()
        self.all_persons = pygame.sprite.Group()
        self.player = Player(self)
        self.all_persons.add(self.player)
        self.comet_event = CometFallEvent(self) # evenement des comets
        self.all_monsters = pygame.sprite.Group() # groupe de monstres
        self.pressed = {}
        
    def start(self):
        self.is_playing = True
        for monster in range(2):
            self.spawn_monster(Mummy)
        self.spawn_monster(Alien)
        
    def game_over(self): # remettre le jeu à neuf
        self.all_monsters = pygame.sprite.Group() 
        self.comet_event.all_comets = pygame.sprite.Group() 
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False
        
    def init_menu(self):
        self.banner = pygame.image.load('assets/banner.png')
        self.banner = pygame.transform.scale(self.banner, (500, 500))
        self.banner_rect = self.banner.get_rect()
        self.banner_rect.x = math.ceil(self.screen.get_width() / 4)
        
        self.play_button = pygame.image.load('assets/button.png')
        self.play_button = pygame.transform.scale(self.play_button, (400, 150))
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.x = math.ceil(self.screen.get_width() / 3.33)
        self.play_button_rect.y = math.ceil(self.screen.get_height() / 2)
        
        
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
    
    def spawn_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self)) # instancie la Class en fonction du parametre de la fonction
        
    def walls(self, direction):
        if direction == 'right':
            return True if self.player.rect.x + self.player.rect.width < self.screen.get_width() else False
        elif direction == 'left':
            return True if self.player.rect.x > 0 else False
        
    def commandes(self):
        if self.pressed.get(pygame.K_RIGHT) and self.pressed.get(pygame.K_LEFT):
            self.player.health = self.player.health + 0.25 if self.player.health < self.player.max_health else self.player.health
        elif self.pressed.get(pygame.K_RIGHT) and self.walls('right'):
            self.player.move('right')
        elif self.pressed.get(pygame.K_LEFT) and self.walls('left'):
            self.player.move('left')
            
    def update(self):
        self.screen.blit(self.player.image, self.player.rect) #appliquer l'image du player
        self.player.update_health_bar(self.screen) # actualiser la bar de vie du joueur
        self.comet_event.update_bar(self.screen) # actualiser la barre d'evenement du jeu
        self.player.update_animation() # actualiser l'animation du player
        
        for projectile in self.player.all_projectiles:
            projectile.move() # mouvement des projectiles
        for monster in self.all_monsters:
            monster.forward() # avancement des monstres
            monster.update_health_bar(self.screen) # update de la bare de vie
            monster.update_animation() # animation du sprite
        for comet in self.comet_event.all_comets:
            comet.fall() # avancement des monstres

        self.player.all_projectiles.draw(self.screen) #appliquer l'ensemble des images du groupe de projectiles
        self.all_monsters.draw(self.screen) #appliquer l'ensemble des images du groupe de monstres
        self.comet_event.all_comets.draw(self.screen) #appliquer l'ensemble des images du groupe de comets
        self.commandes()
        
    def run(self):  
        clock = pygame.time.Clock()          
        running = True
        while running:
            self.screen.blit(self.background, (0, -200)) # arriere plan
            if self.is_playing:
                self.update() #INIT RPG GAME
            else:
                self.screen.blit(self.play_button, self.play_button_rect)
                self.screen.blit(self.banner, self.banner_rect)
            pygame.display.flip() #mettre a jour l'ecran
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
                    
                elif event.type == pygame.MOUSEBUTTONDOWN and self.is_playing == False: # verification pour savoir si la souris est en collision avec le button play
                    if self.play_button_rect.collidepoint(event.pos):
                        self.start() # lancer le jeu
                        
            clock.tick(FPS) #SET FPS
        pygame.quit() #Quit