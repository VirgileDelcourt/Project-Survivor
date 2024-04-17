import pygame
from pygame.locals import QUIT
from time import time, sleep
from random import random

from Display import Display
from Player import Player
from Projectile import Projectile
from Enemy import Enemy

pygame.init()
Display.Instances = []
Player.Instance = None
Enemy.Enemies = []

dimx, dimy = 1080, 720
window = pygame.display.set_mode((dimx, dimy))

pap = Player()
print(Player.Instance)
cooldown = 0

game = True
last = time()
while game:
    delta = time() - last
    last = time()

    for event in pygame.event.get():
        if event.type == QUIT:
            game = False

    cooldown -= delta
    if cooldown <= 0:
        cooldown += 0.7
        Projectile(Player.Instance.rect.center, pygame.mouse.get_pos(), 0.15, 12, 1, 10)
    if len(Enemy.Enemies) == 0 or random() < 1 / ((len(Enemy.Enemies) + 1) * 50):
        Enemy("Images/bil.png", 10, 1)

    window.fill("light green")
    for display in Display.Instances:
        if display != Player.Instance:
            display.Update(delta)
            window.blit(display.surf, display.rect)
    Player.Instance.Update(delta)
    Player.Instance.Move(pygame.key.get_pressed(), delta)
    window.blit(Player.Instance.surf, Player.Instance.rect)

    if not Player.Instance.Get_State():
        game = False

    pygame.display.update()
