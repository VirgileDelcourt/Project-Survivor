import pygame
from random import choices, randrange

from Display import Display
from Player import Player
from Entity import Entity


sides = ['top', 'bottom', 'left', 'right']


class Enemy(Display, Entity):
    Enemies = []

    def __init__(self, image, hp, speed):
        Display.__init__(self, image, (0, 0))
        Entity.__init__(self, hp, 1, 0, speed)
        Enemy.Enemies.append(self)

        width, height = pygame.display.get_surface().get_size()
        weights = [width, width, height, height]

        side = choices(sides, weights)[0]
        if side == 'top':
            y = 0
            x = randrange(width-4)
        elif side == 'bottom':
            y = height-4
            x = randrange(width-4)
        elif side == 'left':
            x = 0
            y = randrange(height-4)
        elif side == 'right':
            x = width-4
            y = randrange(height-4)
        self.Update_Rect((x, y))

    def Update(self, dt):
        if not (self.coord - Player.Instance.coord).magnitude() < self.surf.get_size()[0]:
            movement = Player.Instance.coord - self.coord
            movement.normalize_ip()
            self.coord += movement * dt * 50 * self.speed
        else:
            Player.Instance.Damage(self.power)
        super().Update(dt)

    def Damage(self, pow, phys=True):
        Entity.Damage(self, pow, phys)
        if not self.Get_State():
            Enemy.Enemies.remove(self)
            Display.Instances.remove(self)
