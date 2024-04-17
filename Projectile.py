import pygame

from Display import Display
from Enemy import Enemy


class Projectile(Display):
    def __init__(self, coord, target, duration, speed, pierce, power, image="Images/pip.png"):
        super().__init__(image, coord)
        self.movement = pygame.Vector2(target) - pygame.Vector2(coord)
        self.movement.normalize_ip()

        self.duration = duration
        self.pierce = pierce
        self.movement *= speed
        self.power = power

    def Update(self, dt):
        self.coord += self.movement * dt * 100
        super().Update(dt)

        i = 0
        while i < len(Enemy.Enemies) and self.pierce > 0:
            opp = Enemy.Enemies[i]
            size = (self.surf.get_size()[0] + self.surf.get_size()[1]) / 2
            if (self.coord - opp.coord).magnitude() < size:
                Enemy.Enemies[i].Damage(self.power)
                self.pierce -= 1
            else:
                i += 1

        if self.duration <= 0 or self.pierce == 0:
            Display.Instances.remove(self)
        else:
            self.duration -= dt
