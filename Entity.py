class Entity:
    def __init__(self, hp, pow, res, spd):
        print(hp)
        self.maxhp = hp
        self.hurt = 0
        self.power = pow
        self.resistance = res
        self.speed = spd

    def Get_State(self):
        if self.hurt < self.maxhp:
            return self.maxhp - self.hurt
        else:
            return False

    def Damage(self, pow, phys=True):
        if phys:
            pow -= self.resistance
        self.hurt += pow
        print("an entity took " + str(pow) + " damage")
        if not self.Get_State():
            return False
        else:
            return pow
