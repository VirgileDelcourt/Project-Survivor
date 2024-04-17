import pygame

from Projectile import Projectile
from Player import Player


class Weapon:
    def __init__(self, name, cd, proj_image, proj_nbr, duration, speed, pierce, power):
        self.name = name

        self.timer = 0.01
        self.maxtimer = cd
        self.combo = proj_nbr - 1
        self.currentcombo = proj_nbr - 1
        self.image = proj_image

        self.duration = duration
        self.speed = speed
        self.pierce = pierce
        self.power = power

    def Fire(self, coord, target):
        Projectile(coord, target, self.duration, self.speed, self.pierce, self.power, self.image)

    def Update(self, dt):
        self.timer -= dt
        if self.timer <= 0:
            self.Fire(Player.Instance.rect.center, pygame.mouse.get_pos())
            if self.currentcombo <= 0:
                self.timer += self.maxtimer
                self.currentcombo = self.combo
            else:
                self.timer = self.maxtimer / 5
                self.currentcombo -= 1
