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

    # generate simulated loot for testing purposes
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
    # print total count of each item and what percentage of the simulated loot pool it was
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
            # run auto-sim
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
            # run sim with customized parameters
            elif a.upper() == "N":
                t = input("What tier loot?")
                r = input("How many runs?")
                i = input("How many items per run?")
                probsim(t, r, i)
        else:
            # generate a theoretical loot pool based on default probability
            for them in room_list:
                thetier = random.choices([0, 1, 2, 3], weights=[5, 4, 3, 1.5], k=1)[0]
                test = []
                it = gen_loot(3, thetier, any_item)
                test.append(it)
    # clear the loot pool, deleting item instances from all froms
    elif inp == "/clear":
        for rooms in room_list:
            print(f"Clearing rooms... {round((room_list.index(rooms)/len(room_list))*100)}%")
            removal = rooms[5]
            room_list[room_list.index(rooms)].remove(removal)
            # for loots in range(0, len(rooms[5])):
            #     room_list[room_list.index(rooms)][5]
        print("Done!")
        removed = True
    # re-generate the loot pool, only works if the /clear command is run first
    elif inp == "/gen" and removed is True:
        for that in room_list:
            roomm = int(room_list.index(that))
            loottier = random.choices([0, 1, 2, 3], weights=[5, 4, 3, 1.5], k=1)[0]
            Loot(roomm).add(gen_loot(3, loottier, any_item))
            print("done")
    # clears the loot pool and regenerates it with one command
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
    # spawn an item into the players inventory
    elif inp == "/give":
        print("here you go!")
    # spawn a monster to fight
    elif inp == "/spawn":
        print("mob spawned!")
    # teleport to a specific room
    elif inp == "/tp":
        print("teleported to room!")
    elif inp == "/stats":
        print(f"hp is: {player.hp}")

# Classes
class Color:
    # standard colors
    black = '\u001b[30m'
    red = '\u001b[31m'
    green = '\u001b[32m'
    yellow = '\u001b[33m'
    blue = '\u001b[34m'
    magenta = '\u001b[35m'
    cyan = '\u001b[36m'
    white = '\u001b[37m'
    reset = '\u001b[0m'
    # bright colors
    bright_black = '\u001b[30;1m'
    bright_red = '\u001b[31;1m'
    bright_green = '\u001b[32;1m'
    bright_yellow = '\u001b[33;1m'
    bright_blue = '\u001b[34;1m'
    bright_magenta = '\u001b[35;1m'
    bright_cyan = '\u001b[36;1m'
    bright_white = '\u001b[37;1m'

    # standard background colors
    background_black = '\u001b[40m'
    background_red = '\u001b[41m'
    background_green = '\u001b[42m'
    background_yellow = '\u001b[43m'
    background_blue = '\u001b[44m'
    background_magenta = '\u001b[45m'
    background_cyan = '\u001b[46m'
    background_white = '\u001b[47m'

    # decorative
    bold = '\u001b[1m'
    underline = '\u001b[4m'
    reversed = '\u001b[7m'


# creates an instance of a creature with relevant stats and metadata
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


# enables creation of items with various properties dependent on item type
class Item:

    def __init__(self, name, desc=""):
        self.name = name
        self.description = desc
        self.effect = ""
        self.saturation = 0
        self.special = ""
        self.craftable = ""


# weapon subclass for combat items. has unique parameters of damage, uses, tier, and special
class Weapon(Item):
    def __init__(self, name, desc, damage, uses=-1, tier=0, special="None"):
        self.item_type = weapon
        self.damage = damage
        self.uses = uses
        if self.uses == -1:
            self.uses = 99999
        self.tier = tier
        self.special = special
        if self.uses <= 0:
            print("your item broke")
        if self.damage <=2:
            self.tier = 1
        elif 2 < self.damage <= 5:
            self.tier = 2
        elif 5 < self.damage <= 7:
            self.tier = 3
        super(Weapon, self).__init__(name, desc)


# consumables subclass for healing/special effects items. parameters of saturation and effect
class Consumable(Item):
    def __init__(self, name, desc, saturation, effect=-1):
        self.item_type = consumable
        self.saturation = saturation
        self.effect = effect
        self.damage = 0
        super(Consumable, self).__init__(name, desc)


# Junk subclass, most items in this class are useless. some do damage
class Junk(Item):
    def __init__(self, name, desc, damage=0):
        self.item_type = junk
        self.damage = 0
        super(Junk, self).__init__(name, desc)


# material subclass. materials are used for crafting or other special uses
class Material(Item):
    def __init__(self, name, desc, craftable="no"):
        self.item_type = material
        self.craftable = craftable
        self.damage = 0
        super(Material, self).__init__(name, desc)


# subclass for integral items (those needed to progress through stages in the game)
class Integral(Item):
    def __init__(self, name, desc):
        self.item_type = "Integral Item"
        self.name = name
        self.description = desc


# creates instances of generated loot for a room
# can be used to autogenerate the whole loot pool, or add a specific item to a specific room
class Loot:

    def __init__(self):
        self.room = ""
        self.loot = []
        self.item = []
        self.one = None

    # add randomly generated loot to a room
    def add(self, rooml, item):
        self.room = rooml
        # if multiple items specified, add them to list using this method
        if type(item) == list:
            self.item = item
            for x in self.item:
                self.one = self.item[self.item.index(x)]
                self.loot.append(self.one)
        else:
            self.loot.append(item)

        rooms_loot.append(self.loot)
        # if no existing loot, this method is used to set the initial index of list before generating
        if len(room_list[self.room]) < 6:
            room_list[self.room].append([])
        for items in self.loot:
            x = self.loot[self.loot.index(items)]
            # add each item to the loot index [5] of the room
            room_list[self.room][5].append(x)

    # list generated loot
    def list(self):
        for z in self.loot:
            print(z.name)


class Player:

    def __init__(self, player_health, stamina, inv=[], pos=0):
        self.hp = player_health
        self.maxhp = player_health
        self.stamina = stamina
        self.inv = inv
        self.pos = pos
        self.room = room_list[self.pos]
        self.item = None
        self.food = None
        self.throw = None
        self.lastpos = None
        self.msgs = []

    def damage(self, damage):
        global done
        global fight
        self.hp -= damage
        if self.hp <= 0:
            fight = False
            kill()
        else:
            print(color.yellow + f"You took {color.bright_red}{damage}{color.reset + color.yellow} damage!")
            print(color.yellow + f"Your hp is: {color.white} {self.hp}")

    def heal(self, regen):
        if self.hp == self.maxhp:
            print(color.yellow + "You are already at maximum health!")
            healed = False
        else:
            self.hp += regen
            healed = True
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        return healed

    def collect(self, item):
        self.inv.append(item)
        self.msgs = [f"You pick up the {item.name}", f"You collect the {item.name}"]
        if item.name[0].lower() in ['a','e','i','o','u']:
            print(color.yellow + f"You found an {color.bright_blue + item.name}. {color.reset + color.yellow + item.description}")
        else:
            print(color.yellow + f"You found a {color.bright_blue + item.name}. {color.reset + color.yellow + item.description}")
        player.room[5].remove(item)
        # print(random.choice(self.msgs))

    def consume(self, item):
        self.food = item

    def throw(self, item):
        self.throw = item

    # def move(self, nextt):
    #     self.room = room_list[self.pos]
    #     self.last_room = self.lastpos
    #     # print(f"You left the {self.room[0]}")
    #     travel(nextt)
    def move(self, nextt):
        self.last_room = self.room
        self.lastpos = self.pos
        travel(nextt)




# Creation of object instances

# Creation of Junk
hairbrush = Junk("Plastic Hairbrush", "It's bristles are slimy. You run it through your hair")
screwdriver = Junk('Broken Screwdriver', "Now what are you gonna do with a broken screwdriver, huh?")
bandage = Junk('Used Bandage', 'It may be used, but you can still use it again!')
eyepatch = Junk('Bloody Eyepatch', "You put it on. It feels sticky and warm.")
femur = Junk("Cracked Femur", "Finders keepers!")
plank = Junk("Rotted Wooden Plank", "Hit yourself over the head with it! Maybe this is all just a dream...")
pen = Junk("Ballpoint Pen", "Never a bad time to start writing your obituary.")
letteropen = Junk("Wooden Letter Opener", "Who are you expecting mail from? Your grandma?",1)
rubberband = Junk("Rubber Band", "Strike down your enemies!")
hair = Junk("Ball of Hair", "Did you cough that up? Gross.")
mirror = Junk("Broken Mirror", "It may be broken, but you can still see how ugly you are!")
gameboy = Junk("Gameboy Advanced", "An escape your life! The video games make the pain go away!")
soap = Junk("Used Bar Of Soap", "Should you eat it...? No. ")
# add junk to list
junks = [hair, hairbrush, screwdriver, bandage, eyepatch, femur, plank, pen, letteropen, rubberband, hair,
         mirror, gameboy]

# Creation of Weapons
swiss = Weapon("Swiss Army Knife", "Maybe you can use it to cut swiss cheese?", 3, 5)
switchblade = Weapon("Rusty Switchblade", "Better hope you have your tetanus vaccine...", 2, 3)
chefknife = Weapon("Dull Chef's Knife", "Maybe you should prepare a meal before you become one.", 3.5, 5)
machette = Weapon("Steel Machete", "Too bad you arent trapped in a jungle!", 5, 8)
staff = Weapon("Iron bow-staff", "Is it a bow, or a staff? Maybe both...", 3, -1)
pencil = Weapon("#2 Pencil", "Sharper than your wits!", 1, 1)
fork = Weapon("Bent Fork", "Try and bend it back, then you'll just have a fork.", 1, 2)
nail = Weapon("6 inch Iron Nail", "Quick! Drive it through your skull and end the harsh reality that is your life.", 2, 5)
woodenstake = Weapon("Wooden Stake", "You can protect yourself from vampires!", 2.5, 6)
# add weapons to list
weapons = [swiss, switchblade, chefknife, machette, pencil, fork, nail, woodenstake, staff]

# Materials
nails = Material("Box of Nails", "Maybe you can build something...")
battery = Material('AAA battery', "Too bad you don't have a flashlight...")
matches = Material("Soggy Box of Matches", "Better hope they still work...")
stones = Material("Pile of Stones", "This could be used for something!")
gauze = Material("Fresh Gauze", "I have a feeling you'll be needing this...")
rope = Material("Knotted Rope", "Undo the knots and you can make a noose!")
hammer = Material("Small Hammer", "Are you strong enough to lift that?")
bhammer = Material("Big Hammer", "Who are you, Bob the Builder?")
# add materials to list
materials = [nails, matches, stones, gauze, rope, hammer, bhammer, battery]

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

jumbo_rat = Creature(hostile, "Jumbo Rat", "A Jumbo Rat Appears! He looms over you, waiting to strike...", 5, 5)
miniature_dragon = Creature(hostile, "Miniature Dragon", "A miniature dragon leaps out of the shadows! Me may be small, but he still breathes fire!", 14, 4)
abraham = Creature(hostile, "Abraham Lincoln", "Abraham Lincoln jump down from the ceiling! He think's you're a slave trader!", 10, 3)
hermon = Creature(hostile, "Mr. Hermon", "Mr. Hermon crawls out from the corner! Quick, solve his boom/chain problem before he sucks out your brains!", 2, 5)
joe = Creature(hostile, "Joe", "Joe materializes out of thin air! Wait, that's not very threatening! He gives you a bag of almonds", 6, 2.25)
monk = Creature(hostile, "Decrepid Monk", "A decrepid monk appears! He tries to shave your head.", 15, .8)
luke = Creature(hostile, "Luke Skywalker", "Luke skywalker sprints into the corridor. His light saber hums at his side, ready to slice off your philanges", 20, .7)
# add monsters to pool
monsters = [jumbo_rat, miniature_dragon, abraham, hermon, joe, monk, luke]

removed = False

# transformations. some consumables allow you to transform
shapes = ["Feral Rabbit", "Decrepid Racoon", "Flea Infested Squirrel", "Jumbotron", "Large sewer rat",
          "French Baguette", "Piece of Sidewalk Chalk", "Headless Pigeon", "Piece of Sandpaper"]
shape = Creature(passive)
shape.create(shapes)
room_monsters = []
last_encounter = ""
last_move = ""
fight = False

# Spawning and generation
def enemy():
    global done
    global last_move
    global last_encounter
    global fight
    mob = random.choice(monsters)
    fight = True
    # if the player successfully runs from a monster, only to encounter it again immediately after, run this statement
    if last_encounter == mob and last_move == 2:
        print(color.red + f"{last_encounter.name + color.yellow} has followed you to the {color.blue + room_list[current_room][0] + color.yellow}. You may have escaped their clutches before, "
              f"but will you be so lucky again?")
    # if the user kills a monster but encounters it again, run this statement
    elif last_encounter == mob and last_move == 1:
        print(color.red + f"{last_encounter.name + color.yellow} has risen from the dead! Now even stronger, and with a thirst for vengeance!")
    # run the normal message if not a special encounter
    else:
        print(color.yellow + mob.description)
    # continue the fighting loop until fight is set to false. either by the monster defeating you, it being defeated
    while fight is True:
        # give user 3 actions to take upon encountering monster
        action = user_input("custom", "What will you do? Fight [1] Run [2] Sit [3]", [1, 2, 3])
        # first action is to fight, user can choose eligible item from inventory to attack with
        if action == 1:
            if player.inv:
                open_inv()
                # choice = int(user_input("custom", "Select an item to use in battle!", range(0, len(playerinv)+1)))
                item = player.inv[user_input("custom", "Select an item to use in battle!", range(0, len(player.inv)+1))-1]
                # some weapons can kill a mob in one hit
                print(color.yellow + f"You attacked the {color.bright_red + mob.name + color.reset + color.yellow} with your {color.bright_blue + item.name + color.reset}")
                if item.damage >= mob.hp:
                    print(color.yellow + "You beat {color.bright_red + mob.name}!")
                    if isinstance(item, Weapon):
                        item.uses -= 1
                    print(color.red + f"{item.uses} {color.yellow} uses left on your {color.blue + item.name}")
                    fight = False
                # if the player still has health, damage the monster
                else:
                    if isinstance(item, Weapon):
                        item.uses -= 1
                    mob.hp -= item.damage
                    print(color.yellow + f"You did {color.bright_red} {item.damage} damage" + color.reset)
                    print(color.yellow + f"{mob.name} hp is {color.bright_green} {mob.hp}" + color.reset)
                    # monster dies if hp drops below 0
                    if mob.hp <= 0:
                        print(color.yellow + f"You beat {mob.name}. Well done!")
                        fight = False
                    else:
                        last_encounter = mob
                        player.damage(mob.damage)
                        if player.hp == player.maxhp:
                            break
                    if isinstance(item, Weapon) and item.uses <= 0:
                        print(color.yellow + f"Your {color.bright_blue + item.name + color.reset + color.yellow} broke!")
                        player.inv.remove(item)

            else:
                print(color.red + "Theres nothing in your inventory!")
                continue
        # second combat option is to run
        elif action == 2:
            while True:
                # a pre-determined correct direction is generated. This cannot be a null direction, only one which the player can travel
                r = random.choice(player.room[1:5])
                if r is None:
                    continue
                else:
                    x = player.room.index(r)
                    break
            print(f"x is {x}")
            # ask user which direcion they will run from the monster
            direction = user_input("custom", f"Which way will you run? {controls[1:]}", controls[1:5])
            print(direction)
            # if the player correctly guesses the direction, they escape
            if controls.index(direction) == x:
                print(color.yellow + f"You successfully escaped {color.red + mob.name}!")
                fight = False
                travel(r)
            # if the player guesses incorrectly, they die.
            else:
                print(color.yellow + f"You tried to escape but {color.bright_red + mob.name + color.reset + color.yellow} was too fast!")
                print(color.bright_red + f"{mob.name + color.reset + color.yellow} attacks you, dealing damage.")
                player.damage(mob.damage)
                done = True
                fight = False
        # the third option is to sit down in front of the monster. In some cases this will provide success over other alternatives
        elif action == 3:
            action = input("What style of sitting would you like to partake in?")
            print("You died.")
            fight = False
            done = True
        else:
            continue
    # tracks the last monster encountered and how it was defeated
    last_encounter = mob
    last_move = action


# function for generating the loot pool
def gen_loot(count, tier, itemtype):
    nums = [0, 1, 2, 3]
    rooms_loott = []
    # if item generation is set to any, run random generation
    while count > 0:
        count -= 1
        if itemtype == "any":
            # different odds for each tier of loot, 0 is the worst, 3 is the highest
            # mostly junk, some consumables and materials, no weapons
            if tier == 0:
                index = random.choices(nums, weights=[2, 2, 6, 0], k=1)
                room_loot = random.choices(loot_pool[index[0]], k=1)
            # even amount of consumables, materials, and weapons, but mostly junk
            elif tier == 1:
                index = random.choices(nums, weights=[2, 2, 5, 2], k=1)
                room_loot = random.choices(loot_pool[index[0]], k=1)
            # even amount of all items
            elif tier == 2:
                index = random.choices(nums, weights=[3, 3, 3, 3], k=1)
                room_loot = random.choices(loot_pool[index[0]], k=1)
            # almost no junk, mostly weapons and materials, some consumables
            elif tier == 3:
                index = random.choices(nums, weights=[3, 4, 1, 5], k=1)
                room_loot = random.choices(loot_pool[index[0]], k=1)
        # if loot type is specified, pick random items from that item's loot pool
        elif itemtype in item_types:
            room_loot = random.choices(loot_pool[item_types.index(itemtype)], k=1)[0]
        else:
            print("No items generated")
            room_loot = "none"
        # add loot data to the room
        rooms_loott.append(room_loot)

    return rooms_loott


# Player control functions

# opens payer inventory
def open_inv():
    print(color.bright_yellow + "Your inventory contains:" + color.reset)
    i = 1
    # print the name of each item instance with a number in front of each for organization and selection
    for z in player.inv:
        if isinstance(z, Weapon):
            print(color.cyan + f"{i}) {z.name} {color.white}[{z.item_type}] {color.green}[uses: {z.uses}] [tier: {z.tier}]")
        else:
            print(color.cyan + f"{i}) {z.name} {color.white}[{z.item_type}]")
        i += 1


# searches the room for loot
def search():
    # player must have available energy to search for loot
    if player.stamina > 0:
        # if the room has available loot, grant it to player and remove energy
        if len(player.room[5]) > 0:
            s = random.choice(player.room[5])
            player.collect(s)
            player.stamina -= 1
        # if no items remain, print this message
        else:
            print(color.yellow + "You found all the items in this room!")
    # if player has no energy, they cannot search for loot
    else:
        print(color.red + "You are out of energy!")


# function allow player to use an item, for example a material or consumable
def use():
    print("item used")


# moves player based on directional input
def travel(direction):
    global current_room
    global last_room
    d = None
    true = False
    # move the player in the specified direction, or inform them to select a valid direction if one is not provided
    while d is None and true is False:
        if direction in controls:
            d = controls.index(direction)
            if d is None:
                print(color.bright_red + "You cant go that direction")
                break
            next_room = player.room[d]
            # if the direction selected yields an available room, move the player and inform them of it.
            if next_room is not None:
                player.lastpos = player.pos
                player.pos = next_room
                player.room = room_list[player.pos]
                loc()
                # 33% chance that a monster will spawn on any given move, other than the first move
                if random.randint(0, 2) == 1 and first is not True:
                    enemy()
            # inform the user the direction they selected is not valid
            else:
                print(color.bright_red + "You cant go that direction.")
        elif direction in player.room:
            player.lastpos = player.pos
            player.pos = direction
            player.room = room_list[player.pos]
            true = True
            x = "yep"
            loc()
        else:
            print(color.bright_red + "You cant go that direction.")
            true = True
            x = "nope"


# called when a player consumes an item
def consume(item):
    effect = item.effect
    if effect == 0:
        regen = random.randint(3, 6)
        player.heal(regen)
    elif effect == 1:
        print("you aight")
    elif effect == 2:
        anim = random.choice(shape)
        print("Thought you'd get out of here that easily, huh?")
        print(f"You turned into a {anim}")
    elif effect == -1:
        print(color.bright_red + "You cant eat that.")


def kill():
    def pause():
        time.sleep(1.5)
    global death
    global firstdeath
    global done
    if death:
        print(color.bright_red + "You died.")
        done = True
    else:
        if firstdeath:
            pause()
            print("That's strange... You're back in the grungy stairwell")
            pause()
            print(f"Last you remember you were being struck down by {last_encounter.name}")
            pause()
            print("You notice your items are gone. Your head is pounding.")
            firstdeath = False

        else:
            print(color.bright_red + "You died.")
            print("You have been returned to the grungy stairwell")
            print("Your items were dropped d")
        for k in player.inv:
            player.room[5].append(k)
            player.inv.remove(k)
        player.hp = player.maxhp
        player.stamina = 12
        player.pos = 0
        player.lastpos = player.pos
        player.room = room_list[0]
        player.last_room = player.room


# Utility Functions


# Configures settings
def settings():
    global controls
    # change control scheme used by the game to control the player.
    while controls is None:
        cont = input(f"Would you like to use: [D]irectional Keys (W,A,S,D) or [C]ardinal Directions (N,S,E,W)?")
        if cont.lower() == "d":
            controls = keys
        elif cont.lower() == "c":
            controls = directions
        else:
            print(color.bright_red + "invalid selection.")

    # inform player of selected control scheme
    print(f"Controls are set to: {controls[0]}")


# Prints location of player
def loc():
    print(color.yellow + f"You are in the {color.bright_blue + player.room[0]}" + color.reset)
    yes = "no"


# Takes various forms of user input. designed as a more flexible, specialized form of the default input() as needed for the game
def user_input(userinput="none", prompt="default", options=()):
    inp = None
    while inp is None:
        # if no parameter is specified when the function is called, ask the user to input a command.
        if userinput == "none":
            cmd = input(color.bright_white + "Please enter a command:" + color.reset)
            # if movement key is selected, then move player
            if cmd.upper()[0] in controls[1:5]:
                inp = cmd[0].upper()
                travel(inp)
            # e to open player inventory
            elif cmd.upper()[0] == "E":
                open_inv()
            # v enables developer mode, with in game commands
            elif cmd.lower() == "v":
                devinp = input(color.bright_white + "1) list items in each room.\n2) probability simulation." + color.reset)
                dev(devinp)
                inp = "dev"
            # if user presses q, search the room for loot
            elif cmd.upper()[0] == "Q":
                search()
            # first character of any dev command
            elif cmd[0] == "/" and dev_mode is True:
                print(cmd)
                dev(cmd)
            # print invalid command if key pressed is not within control scheme, and inform player of valid commands
            else:
                print(color.bright_red + f"Invalid Command. Valid Commands: {controls + controlkeys}")
                continue
        # if direction is specified as function input type upon being called, automatically run the direction travel function
        elif userinput == "direction":
            if prompt == "default":
                prompt = "Please input a direction:"
            direct = input(color.bright_white + prompt.upper() + color.reset)
            inp = direct[0]

        # most useful part of user_input function. allows for custom prompts and limits allowed user input to specified keys
        # allows for customized input, best used to handle mis-pressed keys on custom inputs
        elif userinput == "custom" and options != "default" and prompt != "default":
            # can check if the program should be looking for integer input or char input. avoids many errors
            if isinstance(options[0], int):
                # try/except block handles errors in the event of mispressed key
                try:
                    cmd = int(input(color.magenta + prompt))
                    if cmd in options:
                        inp = cmd
                    else:
                        print(color.bright_red + "Invalid input.")
                except ValueError:
                    print(color.bright_red + 'Please enter a number.')
                    continue
            else:
                cmd = input(color.magenta + prompt).upper()
                if cmd in options:
                    inp = cmd
                else:
                    print(color.bright_red + "Invalid input.")
                    continue

        else:
            print(color.bright_red + "Invalid Command")
            continue
        # the function returns the user input as a value usable as required by a function or otherwise
        return inp


# spawn player, set starting variables
# location tracking
current_room = 0
last_room = 0
first = True
controls = None
# create instance of player with base stats
player = Player(12, 12, [], 0)
playerinv = []
# sets game controls
controlkeys = ('Q', 'E')
keys = ('directional keys', 'W', 'S', 'D', 'A')
directions = ('cardinal letters/words', 'N', 'S', 'E', 'W')
# enable/disable developer tools
dev_mode = True

death = False
# main game loop
done = False
firstdeath = True
color = Color
while done is False:
    if first is True:
        # run settings config on first bootup
        settings()
        # prints "fake" generation messages for user enjoyment
        print(color.bright_red + "Generating terrain...")
        time.sleep(.25)
        print("Randomizing loot...")
        time.sleep(.25)
        # generates the loot in each room
        for each in room_list[1:]:
            room = int(room_list.index(each))
            loot_tier = random.choices([0, 1, 2, 3], weights=[5, 4, 3, 1.5], k=1)[0]
            loot = gen_loot(3, loot_tier, any_item)
            for loots in loot:
                Loot().add(room, loots)
        # creates starting item in the entry room
        Loot().add(0, eyepatch)
        print("Spawning monsters...")
        time.sleep(.25)
        print("Tending the garden...")
        time.sleep(.25)
        print(color.blue + "Welcome to Dungeon Adventure [Alpha 1.4]!" + color.reset)
        time.sleep(.25)
        # tells player their initial location
        loc()
        # tells user to choose a direction to travel first
        first = False
    # runs each time the game loops, primary point of interaction
    user_input()

    # currently in its unfinished state, the objective is to obtain all the loot in the dungeon
    if len(playerinv) == len(loot_pool[0]+loot_pool[1]+loot_pool[2]+loot_pool[3]):
        print("You win!")
        done = True

# if the player dies and the loop breaks, the game ends.
print("Game Over.")

