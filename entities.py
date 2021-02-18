class Creature:
    def __init__(self, kind, name="", description="", mob_hp=-1, damage=-1):
        self.name = name
        self.damage = damage
        self.description = description
        self.hp = mob_hp
        self.maxhp = mob_hp
        self.kind = kind
        self.list = []
        self.value = None

    # creates instance of a creature
    def create(self, lst):
        self.value = lst
        for y in self.value:
            self.list.append(y)

    # list instnaces of creatures
    def lst(self):
        for z in self.list:
            print(z)


