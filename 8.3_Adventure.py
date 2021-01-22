'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
import random
import time


room_list = []
# Creates each room
# Room parameters - ["Description", N, S, E, W]
# 0
room = ["grungy stairwell", 3, None, None, None]
room_list.append(room)
# 1
room = ["washroom", 4, None, None, None]
room_list.append(room)
# 2
room = ["torture hall", 7, None, None, None]
room_list.append(room)
# 3
room = ["main corridor", 9, 0, 4, 7]
room_list.append(room)
# 4
room = ["east corridor", 8, 1, 5, 3]
room_list.append(room)
# 5
room = ["storage closet", None, None, None, 4]
room_list.append(room)
# 6
room = ["keepers quarters", 12, 11, 7, None]
room_list.append(room)
# 7
room = ["west corridor", None, 2, 3, 6]
room_list.append(room)
# 8
room = ["desolate kitchen", None, 4, None, None]
room_list.append(room)
# 9
room = ["prisoners quarters", None, 3, 10, None]
room_list.append(room)
# 10
room = ["secret passage to closet", None, 5, None, None]
room_list.append(room)
# 11
room = ["secret passage to stairwell", None, None, 0, None]
room_list.append(room)
# 12
room = ["keepers hall", None, 6, 13, None]
room_list.append(room)
# 13
room = ["private washroom", None, 6, None, 12]
room_list.append(room)

# assign commonly used string values to variables for easy access
weapon = "weapon"
consumable = "consumable"
junk = "junk"
material = "material"
any_item = "any"
hostile = "hostile"
passive = "passive"


# Development Tools


# probability simulation for various events
def probsim(tier, runs, ipr=1):
    junkcount = 0
    weaponcount = 0
    materialcount = 0
    consumablecount = 0

    for x in range(0, runs):
        loot = gen_loot(ipr, tier, any_item)
        for i in range(0, len(loot)):
            if loot[i].item_type == junk:
                junkcount += 1
            elif loot[i].item_type == weapon:
                weaponcount += 1
            elif loot[i].item_type == material:
                materialcount += 1
            elif loot[i].item_type == consumable:
                consumablecount += 1

    print(f"Junk: {junkcount} items. {(junkcount/runs)*100}%\n weapons: {weaponcount} items. {(weaponcount/runs)*100}%\n "
          f"consumable: {consumablecount} items {(consumablecount/runs)*100}%\n material: {materialcount} items. {(materialcount/runs)*100}%")


# dev commands menu
def dev(inp):
    global removed
    if inp == "/list":
        for rooms in room_list:
            print(f"\n{room_list[room_list.index(rooms)][0].upper()}:")
            for those in room_list[room_list.index(rooms)][5]:
                print(those.name)
    elif inp == "/sim":
        sim = inp.split("m ")
        # kind = input("\n1) tier sim\n 2) loot sim\n 3) tier + loot sim")
        if sim == "tier":
            for i in range(0, 14):
                tier = random.choices([0, 1, 2, 3], weights=[5, 4, 3, 1.5], k=1)[0]
                print(tier)
        elif sim == "loot":
            a = input("Run Auto Sim? [y/n]")
            if a.upper() == "Y":
                print("\ntier 0")
                probsim(0, 100)
                print("\ntier 1")
                probsim(1, 100)
                print("\ntier 2")
                probsim(2, 100)
                print("\ntier 3")
                probsim(3, 100)
            elif a.upper() == "N":
                t = input("What tier loot?")
                r = input("How many runs?")
                i = input("How many items per run?")
                probsim(t, r, i)
        else:
            for them in room_list:
                thetier = random.choices([0, 1, 2, 3], weights=[5, 4, 3, 1.5], k=1)[0]
                test = []
                it = gen_loot(3, thetier, any_item)
                test.append(it)
    elif inp == "/clear":
        for rooms in room_list:
            print(f"Clearing rooms... {round((room_list.index(rooms)/len(room_list))*100)}%")
            removal = rooms[5]
            room_list[room_list.index(rooms)].remove(removal)
            # for loots in range(0, len(rooms[5])):
            #     room_list[room_list.index(rooms)][5]
        print("Done!")
        removed = True
    elif inp == "/gen" and removed is True:
        for that in room_list:
            roomm = int(room_list.index(that))
            loottier = random.choices([0, 1, 2, 3], weights=[5, 4, 3, 1.5], k=1)[0]
            Loot(roomm).add(gen_loot(3, loottier, any_item))
            print("done")
    elif inp == "/reset":
        print("Clearing rooms...")
        for rooms in room_list:
            # print(f"Clearing rooms... {round((room_list.index(rooms)/len(room_list))*100)}%")
            removal = rooms[5]
            room_list[room_list.index(rooms)].remove(removal)
        print("Regenerating Loot...")
        for that in room_list:
            roomm = int(room_list.index(that))
            loottier = random.choices([0, 1, 2, 3], weights=[5, 4, 3, 1.5], k=1)[0]
            Loot(roomm).add(gen_loot(3, loottier, any_item))
        print("Done.")
    elif inp == "/give":
        print("here you go!")
    elif inp == "/spawn":
        print("mob spawned!")
    elif inp == "/tp":
        print("teleported to room!")

# Classes


# creates an instance of a creature with relevant stats and metadata
class Creature:

    def __init__(self, kind, name="", description="", mob_hp=-1):
        self.name = name
        self.description = description
        self.hp = mob_hp
        self.kind = kind
        self.list = []
        self.value = None

    def create(self, lst):
        self.value = lst
        for y in self.value:
            self.list.append(y)

    def lst(self):
        for z in self.list:
            print(z)


# enables creation of items with various properties dependent on item type
class Item:

    def __init__(self, name, desc=""):
        self.name = name
        self.description = desc
        self.effect = ""
        self.saturation = 0
        self.special = ""
        self.craftable = ""


class Weapon(Item):
    def __init__(self, name, desc, damage, uses, tier=0, special="None"):
        self.item_type = weapon
        self.damage = damage
        self.uses = uses
        self.tier = tier
        self.special = special
        super(Weapon, self).__init__(name, desc)


class Consumable(Item):
    def __init__(self, name, desc, saturation, effect="effect"):
        self.item_type = consumable
        self.saturation = saturation
        self.effect = effect
        self.damage = 0
        super(Consumable, self).__init__(name, desc)


class Junk(Item):
    def __init__(self, name, desc):
        self.item_type = junk
        self.damage = 0
        super(Junk, self).__init__(name, desc)


class Material(Item):
    def __init__(self, name, desc, craftable="no"):
        self.item_type = material
        self.craftable = craftable
        self.damage = 0
        super(Material, self).__init__(name, desc)


# creates instances of generated loot for a room
class Loot:

    def __init__(self, rooml):
        self.room = rooml
        self.loot = []
        self.item = []
        self.one = None

    def add(self, item):
        if type(item) == list:
            self.item = item
            for x in self.item:
                self.one = self.item[self.item.index(x)]
                self.loot.append(self.one)
        else:
            self.loot.append(item)
        rooms_loot.append(self.loot)
        room_list[self.room].append(self.loot)

    def list(self):
        for z in self.loot:
            print(z.name)


# Creation of object instances


# Creation of Junk
hairbrush = Junk("Plastic Hairbrush", "It's Sticky. You run it through your hair")
screwdriver = Junk('Broken Screwdriver', "Now what are you gonna do with a broken screwdriver, huh?")
battery = Junk('AAA battery', "Too bad you don't have a flashlight...")
bandage = Junk('Used Bandage', 'It may be used, but you can still use it again!')
eyepatch = Junk('Bloody Eyepatch', "I wonder how the blood got there...")
femur = Junk("Cracked Femur", "Finders keepers!")
plank = Junk("Rotted Wooden Plank", "Hit yourself over the head with it! Maybe this is all just a dream...")
pen = Junk("Ballpoint Pen", "Never a bad time to start writing your obituary.")
letteropen = Junk("Wooden Letter Opener", "Who are you expecting mail from? Your grandma?")
rubberband = Junk("Rubber Band", "Strike down your enemies!")
hair = Junk("Ball of Hair", "Did you cough that up? Gross.")
mirror = Junk("Broken Mirror", "It may be broken, but you can still see how ugly you are!")
gameboy = Junk("Gameboy Advanced", "You'll need a way to stay entertained down here!")
soap = Junk("Used Bar Of Soap", "Should you eat it...? No.")
# add junk to list
junks = [hair, hairbrush, screwdriver, battery, bandage, eyepatch, femur, plank, pen, letteropen, rubberband, hair,
         mirror, gameboy]

# Creation of Weapons
swiss = Weapon("Swiss Army Knife", "Maybe you can use it to cut swiss cheese?", 3, 5)
switchblade = Weapon("Rusty Switchblade", "Better hope you have your tetanus vaccine...", 2, 3)
chefknife = Weapon("Dull Chef's Knife", "Maybe you should prepare a meal before you become one.", 3.5, 5)
machette = Weapon("16 inch Machete", "Too bad you arent trapped in a jungle!", 5, 2, 8)
pencil = Weapon("#2 Pencil", "Sharper than your wits!", 1, 1)
fork = Weapon("Bent Fork", "Try and bend it back, then you'll just have a fork.", 1, 2)
nail = Weapon("6 inch Iron Nail", "Quick! Drive it through your skull and end the harsh reality that is your life.", 2, 5)
woodenstake = Weapon("Wooden Stake", "You can protect yourself from vampires!", 2.5, 6)
# add weapons to list
weapons = [swiss, switchblade, chefknife, machette, pencil, fork, nail, woodenstake]

# Materials
nails = Material("Box of Nails", "Maybe you can build something...")
matches = Material("Soggy Box of Matches", "Better hope they still work...")
stones = Material("Pile of Stones", "This could be used for something!")
gauze = Material("Fresh Gauze", "I have a feeling you'll be needing this...")
rope = Material("Knotted Rope", "Undo the knots and you can make a noose!")
hammer = Material("Small Hammer", "Are you strong enough to lift that?")
bhammer = Material("Big Hammer", "Who are you, Bob the Builder?")
# add materials to list
materials = [nails, matches, stones, gauze, rope, hammer, bhammer]

# Consumables
cheese = Consumable("Swiss Cheese", "It's got holes in it!", 1, effect=0)
flesh = Consumable("Rotten Flesh", "Wait, this isn't minecraft!", 3, effect=1)
apple = Consumable("Bruised Apple", "Watch your back, before you get bruised too...", 1.5, effect=0)
mouse = Consumable("Mutilated Mouse", "Not very appetizing... yet.", 4, effect=0)
bread = Consumable("Stale loaf of Bread", "This could do some damage... Or you could eat it", 2.5, effect=0)
medicine = Consumable("Mysterious Bottle Of Medicine", "At least you have a painless way out...", 0, effect=2)
ratpoison = Consumable("Rat Poison", "You shouldn't eat this... Should you?", 0, effect=1)
# add consumables to list
consumables = [cheese, flesh, apple, mouse, bread, medicine]
item_types = ["consumable", "material", "junk", "weapon"]
# add all items to loot pool
loot_pool = [consumables, materials, junks, weapons]
rooms_loot = []

jumbo_rat = Creature(hostile, "Jumbo Rat", "A Jumbo Rat Appears! He looms over you, waiting to strike...", 5)
miniature_dragon = Creature(hostile, "Miniature Dragon", "A miniature dragon leaps out of the shadows! Me may be small, but he still breathes fire!", 14)
abraham = Creature(hostile, "Abraham Lincoln", "Abraham Lincoln jump down from the ceiling! He think's you're a slave trader!", 10)
hermon = Creature(hostile, "Mr. Hermon", "Mr. Hermon crawls out from the corner! Quick, solve his boom/chain problem before he sucks out your brains!", -1)
joe = Creature(hostile, "Joe", "Joe materializes out of thin air! Wait, that's not very threatening! He gives you a bag of almonds", -1)
monk = Creature(hostile, "Decrepid Monk", "A decrepid monk appears! He tries to shave your head.", 15)
luke = Creature(hostile, "Luke Skywalker", "Luke skywalker sprints into the corridor. His light saber hums at his side, ready to slice off your philanges", 20)

monsters = [jumbo_rat, miniature_dragon, abraham, hermon, joe, monk, luke]

removed = False

# transformations
shapes = ["Feral Rabbit", "Decrepid Racoon", "Flea Infested Squirrel", "Jumbotron", "Large sewer rat",
          "French Baguette", "Piece of Sidewalk Chalk", "Headless Pigeon", "Piece of Sandpaper"]
shape = Creature(passive, -1)
shape.create(shapes)
room_monsters = []


# Spawning and generation
def enemy():
    global done
    mob = random.choice(monsters)
    # print(mob.name)
    # room_monsters.insert(current_room, mob)
    print(mob.description)
    action = int(input("What will you do? Fight [1] Run [2] Sit [3]"))
    if action == 1:
        open_inv()
        choice = int(input("Select an item to use in battle!"))
        item = playerinv[choice-1]
        if (item.damage * 3) > mob.hp:
            print(f"You beat {mob.name}!")
    elif action == 2:
        x = random.randint(0, 1)
        if x == 0:
            input(f"Which way will you run? {controls[1:]}")
            print(f"{mob.name} Killed you.")
            done = True
        elif x == 1:
            travel(current_room, user_input("direction", f"Which way will you run? {controls[1:]}"))
            print(f"You successfully escaped {mob.name}!")
    elif action == 3:
        action = input("What style of sitting would you like to partake in?")
        print("You died")
        done = True
    else:
        print("That wasnt a valid option")

def gen_loot(count, tier, itemtype):
    nums = [0, 1, 2, 3]
    # if item generation is set to any, run random generation
    if itemtype == "any":
        # different odds for each tier of loot, 0 is the worst, 3 is the highest
        # mostly junk, some consumables and materials, no weapons
        if tier == 0:
            index = random.choices(nums, weights=[2, 2, 6, 0], k=count)
            room_loot = random.choices(loot_pool[index[0]], k=count)
        # even amount of consumables, materials, and weapons, but mostly junk
        elif tier == 1:
            index = random.choices(nums, weights=[2, 2, 5, 2], k=count)
            room_loot = random.choices(loot_pool[index[0]], k=count)
        # even amount of all items
        elif tier == 2:
            index = random.choices(nums, weights=[3, 3, 3, 3], k=count)
            room_loot = random.choices(loot_pool[index[0]], k=count)
        # almost no junk, mostly weapons and materials, some consumables
        elif tier == 3:
            index = random.choices(nums, weights=[3, 4, 1, 5], k=count)
            room_loot = random.choices(loot_pool[index[0]], k=count)
    # if loot type is specified, pick random items from that item's loot pool
    elif itemtype in item_types:
        room_loot = random.choices(loot_pool[item_types.index(itemtype)], k=count)
    else:
        print("No items generated")
        room_loot = "none"
    # add loot data to the room
    rooms_loot.append(room_loot)

    return room_loot


# Player control functions

# opens payer inventory
def open_inv():
    print("Your inventory contains:")
    i = 1
    for z in playerinv:
        print(f"{i}) {z.name} [{z.item_type}]")
        i +=1


# searches the room for loot
def search():
    if len(room_list[current_room][5]) > 0:
        s = random.choice(room_list[current_room][5])
        print(f"You found a {s.name}. {s.description}")
        room_list[current_room][5].remove(s)
        playerinv.append(s)
    else:
        print("You found all the items in this room!")


# moves player based on directional input
def travel(current, direction):
    global current_room
    global last_room
    d = None
    while d is None:
        d = controls.index(direction)
        next_room = room_list[current][d]
        if next_room is not None:
            last_room = current_room
            current_room = next_room
            loc()
            if random.randint(0, 2) == 1:
                enemy()
        else:
            print("You cant go that direction.")


# called when a player consumes an item
def consume(item):
    effect = item.effect
    if effect == 0:
        regen = random.randint(3, 6)
        health(regen)
    elif effect == 1:
        print("you aight")
    elif effect == 2:
        anim = random.choice(shape)
        print("Thought you'd get out of here that easily, huh?")
        print(f"You turned into a {anim}")
    elif effect == -1:
        print("You cant eat that.")


# player status functions


# controls player health
def health(regen=0, damage=0):
    global hp
    hp -= damage
    hp += regen


# Utility Functions

# Configures settings
def settings():
    global controls
    while controls is None:
        cont = input(f"Would you like to use: {keys[0]} (W,A,S,D) or {directions[0]} (N,S,E,W)? type [d/c]")
        if cont.lower() == "d":
            controls = keys
        elif cont.lower() == "c":
            controls = directions
        else:
            print("invalid selection.")

    print(f"Controls are set to: {controls[0]}")


# Prints location of player
def loc():
    playerpos = room_list[current_room]
    print(f"You are in the {playerpos[0]}")


# Takes various forms of user input
def user_input(userinput="none", prompt="default"):
    inp = None
    while inp is None:
        if userinput == "none":
            cmd = input(f"Please enter a command:")
            if cmd.upper()[0] in controls[1:5]:
                inp = cmd[0].upper()
                travel(current_room, inp)
            elif cmd.upper()[0] == "E":
                open_inv()
            elif cmd.lower() == "v":
                devinp = input("1) list items in each room.\n2) probability simulation.")
                dev(devinp)
                inp = "dev"
            elif cmd.upper()[0] == "Q":
                search()
            elif cmd[0] == "/" and dev_mode is True:
                print(cmd)
                dev(cmd)
            else:
                print(f"Invalid Command. Valid Commands: {controls + controlkeys}")
                continue
        elif userinput == "direction":
            if prompt == "default":
                prompt = "Please input a direction:"
            direct = input(prompt).upper()
            inp = direct[0]
        # elif userinput == "dev":
        #     devinp = input("1) list items in each room.\n2) probability simulation.")
        #     dev(devinp)
        #     inp = "dev"
        else:
            print("Invalid Command")
            continue
        return inp



# spawn player, set starting variables
# location tracking
current_room = 0
last_room = 0
first = True
controls = None
# sets base player status's
hp = 100
hunger = 100
energy = 10
playerinv = []
# sets game controls
controlkeys = ['Q', 'E']
keys = ['directional keys', 'W', 'S', 'D', 'A']
directions = ['cardinal letters/words', 'N', 'S', 'E', 'W']
# enable/disable developer tools
dev_mode = True


# main game loop
done = False
while done is False:
    if first is True:
        settings()
        # print(len(loot_pool[0]+loot_pool[1]+loot_pool[2]+loot_pool[3]))
        print("Generating terrain...")
        time.sleep(.25)
        print("Randomizing loot...")
        time.sleep(.25)
        for each in room_list:
            room = int(room_list.index(each))
            loot_tier = random.choices([0, 1, 2, 3], weights=[5, 4, 3, 1.5], k=1)[0]
            Loot(room).add(gen_loot(3, loot_tier, any_item))
        print("Spawning monsters...")
        time.sleep(.25)
        print("Tending the garden...")
        time.sleep(.25)
        print("Welcome to Dungeon Adventure [Alpha 1.4]!")
        time.sleep(.25)
        loc()
        travel(current_room, user_input("direction"))
        first = False
    user_input()
    if len(playerinv) == len(loot_pool[0]+loot_pool[1]+loot_pool[2]+loot_pool[3]):
        print("You win!")
        done = True

print("Game Over.")

