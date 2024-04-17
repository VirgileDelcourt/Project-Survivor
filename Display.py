import pygame


class Display(pygame.sprite.Sprite):
    Instances = []

    def __init__(self, image, coord):
        super().__init__()

        if image:
            self.current_image = image

        self.active = True
        self.tinted = False
        self.coord = pygame.Vector2(coord)
        self.Load_Img()

        Display.Instances.append(self)

    def Load_Img(self, source=None):
        if source is None:
            source = self.current_image
        else:
            self.current_image = source
        self.surf = pygame.image.load(source).convert_alpha()
        self.rect = self.surf.get_rect()
        self.Update_Rect()

    def Update_Rect(self, coord=None):
        if coord is None:
            x, y = self.coord
        else:
            self.coord = pygame.Vector2(coord)
            x, y = coord
        self.rect.center = x, y

    def Set_Active(self, active=True):
        self.active = active

    def Tint(self, tint=True, color=(100, 100, 100, 0)):
        if tint:
            self.Load_Img()
            self.surf.fill(color, special_flags=pygame.BLEND_ADD)
        if not tint:
            self.Load_Img()

    def Update(self, dt):
        self.Update_Rect()

