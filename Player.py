import pygame
from pygame.locals import K_LEFT, K_RIGHT, K_UP, K_DOWN

from Display import Display
from Entity import Entity


class Player(Display, Entity):
    Instance = None

    def __init__(self, image="Images/pap.png"):
        Display.__init__(self, image, (0, 0))
        Entity.__init__(self, 10, 0, 0, 1)
        x, y = pygame.display.get_surface().get_size()
        x = x / 2
        y = y / 2
        self.origin = x, y

        self.invincible = 1

        Player.Instance = self

    def Update(self, dt):
        self.Update_Rect(self.origin)
        if self.invincible > 0:
            self.invincible -= dt
            if self.invincible <= 0:
                self.Tint(False, (255, 255, 255, 25))

    def Move(self, keys, dt):
        x, y = 0, 0
        if keys[K_LEFT]:
            x += 1
        if keys[K_RIGHT]:
            x -= 1
        if keys[K_UP]:
            y += 1
        if keys[K_DOWN]:
            y -= 1
        vec = pygame.Vector2(x, y)
        if (x, y) != (0, 0):
            vec.normalize_ip()
        for display in Display.Instances:
            display.coord += vec * dt * 400 * self.speed

    def Damage(self, pow, phys=True):
        if self.invincible <= 0:
            Entity.Damage(self, pow, phys)
            self.invincible = 1
            self.Tint(True)
