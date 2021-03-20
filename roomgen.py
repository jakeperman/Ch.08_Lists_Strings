# room class
import loot


class Room:
    def __init__(self, num, name, r_north=None, r_south=None, r_east=None, r_west=None, desc=""):
        self.num = num
        self.name = name
        self.description = desc
        self.north = r_north
        self.south = r_south
        self.east = r_east
        self.west = r_west
        self.rooms = [self.north, self.south, self.east, self.west]
        self.monsters = []
        self.loot = []
        self.first = True

    def add_loot(self, item):
        # if multiple items specified, add them to list using this method
        items = []
        if isinstance(item, list):
            for x in item:
                items.append(x)
        else:
            items.append(item)
        for those in items:
            # add each item to the loot index [5] of the room
            self.loot.append(those)

    def del_loot(self, item):
        # if multiple items specified, remove them from the list using this method
        items = []
        if isinstance(item, list):
            for x in item:
                items.append(x)
        else:
            items.append(item)
        for them in items:
            # remove each item from the loot of the room
            self.loot.remove(them)

    def spawn_mob(self, creature="any"):
        print("mob")

# loot gen