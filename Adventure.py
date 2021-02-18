'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
import random
import time
import advtools
import roomgen
import loot
import entities
Creature = entities.Creature
color = advtools.Color
Junk = loot.Junk
Weapon = loot.Weapon
Consumable = loot.Consumable
Material = loot.Material
Integral = loot.Integral
Room = roomgen.Room
Loot = loot.Loot
border = advtools.border
# room instances
stairwell = Room(0, "Grungy Stairwell", r_north=3)
washroom = Room(1, "Public Washroom", r_north=4)
torture = Room(2, "Torture Hall")
main_corridor = Room(3, "Main Corridor", 9, 0, 4, 7)
east_corridor = Room(4, "East Corridor", 8, 1, 5, 3)
closet = Room(5, "Storage Closet", r_west=4)
keepers_quarters = Room(6, "Keepers Quarters", 12, 11, 7)
west_corridor = Room(7, "West Corridor", None, 2, 3, 6)
kitchen = Room(8, "Desolate Kitchen", r_south=4)
prisoners_quarters = Room(9, "Prisoners Quarters", r_south=3, r_east=10)
prison_passage = Room(10, "Secret Passage", r_south=5, r_west=9)
keepers_passage = Room(11, "Secret Passage", r_east=0, r_north=6)
keepers_hall = Room(12, "Keepers Hall", r_south=6, r_east=13)
private_washroom = Room(13, "Private Washroom", r_west=12)
rooms = [stairwell, washroom, torture, main_corridor, east_corridor, closet, keepers_quarters, west_corridor, kitchen, prisoners_quarters, prison_passage,
         keepers_passage, keepers_hall, private_washroom]


# Player class
class Player:
    def __init__(self, player_health, stamina, inv=[], pos=0):
        self.hp = player_health
        self.maxhp = player_health
        self.stamina = stamina
        self.inv = inv
        self.pos = stairwell.num
        self.room = stairwell
        self.item = None
        self.food = None
        self.throw = None
        self.lastpos = None
        self.msgs = []

    def damage(self, damage):
        global done
        global fight
        global escmsg
        global fight_msg
        self.hp -= damage
        if self.hp <= 0:
            fight = False
            kill()
        else:
            amount = ""
            if damage <= 2:
                amount = color.green + color.bold + "a little"
            elif 2 < damage <= 4:
                amount = color.bright_red + "some"
            elif damage >= 5:
                amount = color.red + color.bold + "a lot" + color.reset + color.yellow + " of"
            print(color.yellow + f"You took {amount + color.reset + color.yellow} damage!")
            # print(color.yellow + f"Your hp is: {color.bright_red}{self.hp}")

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
        msgs = [f"You pick up the {item.name}", f"You collect the {item.name}"]
        if item.name[0].lower() in ['a', 'e', 'i', 'o', 'u']:
            print(color.yellow + f"You found an {color.bright_green + item.name}. {color.reset + color.yellow + item.description}")
        else:
            print(color.yellow + f"You found a {color.bold_blue + item.name}. {color.reset + color.yellow + item.description}")
        if self.room == stairwell:
            print(color.magenta + "*you place it in your satchel*")
        if item in player.room.loot:
            player.room.del_loot(item)
        # print(random.choice(self.msgs))

    def consume(self, item):
        self.food = item

    def throw(self, item):
        self.throw = item


# assign commonly used string values to variables for easy access
weapon = "weapon"
consumable = "consumable"
junk = "junk"
material = "material"
any_item = "any"
hostile = "hostile"
passive = "passive"
room = 0
removed = False
fight = False
last_encounter = ""
escmsg = ""
action = 0
fight_msg = ""
attackmsg = ""
# spawn player, set starting variables
# location tracking
current_room = 0
last_room = 0
first = True
playerinv = []
# sets game controls
controlkeys = ('Q', 'E')
keys = ('directional keys', 'W', 'S', 'D', 'A')
directions = ('cardinal letters/words', 'N', 'S', 'E', 'W')
controls = keys
# enable/disable developer tools
dev_mode = True
death = False
# main game loop
done = False
firstdeath = True
moves = 0

# Dev Tools
# probability simulation for various events
# def probsim(tier, runs, ipr=1):
#     junkcount = 0
#     weaponcount = 0
#     materialcount = 0
#     consumablecount = 0
#
#     # generate simulated loot for testing purposes
#     for x in range(0, runs):
#         loot = gen_loot(ipr, tier, any_item)
#         for i in range(0, len(loot)):
#             if loot[i].item_type == junk:
#                 junkcount += 1
#             elif loot[i].item_type == weapon:
#                 weaponcount += 1
#             elif loot[i].item_type == material:
#                 materialcount += 1
#             elif loot[i].item_type == consumable:
#                 consumablecount += 1
#     # print total count of each item and what percentage of the simulated loot pool it was
#     print(f"Junk: {junkcount} items. {(junkcount/runs)*100}%\n weapons: {weaponcount} items. {(weaponcount/runs)*100}%\n "
#           f"consumable: {consumablecount} items {(consumablecount/runs)*100}%\n material: {materialcount} items. {(materialcount/runs)*100}%")
#
#
# # dev commands menu
# def dev(inp):
#     global removed
#     if inp == "/list":
#         for rooms in room_list:
#             print(f"\n{room_list[room_list.index(rooms)][0].upper()}:")
#             for those in room_list[room_list.index(rooms)][5]:
#                 print(those.name)
#     elif inp == "/sim":
#         sim = inp.split("m ")
#         # kind = input("\n1) tier sim\n 2) loot sim\n 3) tier + loot sim")
#         if sim == "tier":
#             for i in range(0, 14):
#                 tier = random.choices([0, 1, 2, 3], weights=[5, 4, 3, 1.5], k=1)[0]
#                 print(tier)
#         elif sim == "loot":
#             # run auto-sim
#             a = input("Run Auto Sim? [y/n]")
#             if a.upper() == "Y":
#                 print("\ntier 0")
#                 probsim(0, 100)
#                 print("\ntier 1")
#                 probsim(1, 100)
#                 print("\ntier 2")
#                 probsim(2, 100)
#                 print("\ntier 3")
#                 probsim(3, 100)
#             # run sim with customized parameters
#             elif a.upper() == "N":
#                 t = input("What tier loot?")
#                 r = input("How many runs?")
#                 i = input("How many items per run?")
#                 probsim(t, r, i)
#         else:
#             # generate a theoretical loot pool based on default probability
#             for them in room_list:
#                 thetier = random.choices([0, 1, 2, 3], weights=[5, 4, 3, 1.5], k=1)[0]
#                 test = []
#                 it = gen_loot(3, thetier, any_item)
#                 test.append(it)
#     # clear the loot pool, deleting item instances from all froms
#     elif inp == "/clear":
#         for rooms in room_list:
#             print(f"Clearing rooms... {round((room_list.index(rooms)/len(room_list))*100)}%")
#             removal = rooms[5]
#             room_list[room_list.index(rooms)].remove(removal)
#             # for loots in range(0, len(rooms[5])):
#             #     room_list[room_list.index(rooms)][5]
#         print("Done!")
#         removed = True
#     # re-generate the loot pool, only works if the /clear command is run first
#     elif inp == "/gen" and removed is True:
#         for that in room_list:
#             roomm = int(room_list.index(that))
#             loottier = random.choices([0, 1, 2, 3], weights=[5, 4, 3, 1.5], k=1)[0]
#             Loot(roomm).add(gen_loot(3, loottier, any_item))
#             print("done")
#     # clears the loot pool and regenerates it with one command
#     elif inp == "/reset":
#         print("Clearing rooms...")
#         for rooms in room_list:
#             # print(f"Clearing rooms... {round((room_list.index(rooms)/len(room_list))*100)}%")
#             removal = rooms[5]
#             room_list[room_list.index(rooms)].remove(removal)
#         print("Regenerating Loot...")
#         for that in room_list:
#             roomm = int(room_list.index(that))
#             loottier = random.choices([0, 1, 2, 3], weights=[5, 4, 3, 1.5], k=1)[0]
#             Loot(roomm).add(gen_loot(3, loottier, any_item))
#         print("Done.")
#     # spawn an item into the players inventory
#     elif inp == "/give":
#         print("here you go!")
#     # spawn a monster to fight
#     elif inp == "/spawn":
#         print("mob spawned!")
#     # teleport to a specific room
#     elif inp == "/tp":
#         print("teleported to room!")
#     elif inp == "/stats":
#         print(f"hp is: {player.hp}")


# create instance of player and color
player = Player(12, 12, [], 0)



# Room Functions, triggers different events in each room
# def stairwell():
#     print("The match")



# Creation of object instances
# Creation of Junk
hairbrush = Junk("Plastic Hairbrush", "It's bristles are slimy. You run it through your hair")
screwdriver = Junk('Broken Screwdriver', "Now what are you gonna do with a broken screwdriver, huh?")
bandage = Junk('Used Bandage', 'It may be used, but you can still use it again!')
eyepatch = Junk('Bloody Eyepatch', "You put it on. It feels sticky and warm.")
femur = Junk("Cracked Femur", "Finders keepers!")
plank = Junk("Rotted Wooden Plank", "Hit yourself over the head with it! Maybe this is all just a dream...")
pen = Junk("Ballpoint Pen", "Never a bad time to start writing your obituary.", 1, 1)
letteropen = Junk("Wooden Letter Opener", "Who are you expecting mail from? Your grandma?",1, 2)
rubberband = Junk("Rubber Band", "Strike down your enemies!", 3, 1)
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
stones = Material("Pile of Stones", "Don't eat them.")
splint = Material("Wooden Splint", "Try not to break your leg. But if you do, you've got a splint!")
stick = Material("Stick", "How'd this get here?? I don't see any trees...")
gauze = Material("Fresh Gauze", "I have a feeling you'll be needing this...")
rope = Material("Knotted Rope", "Undo the knots and you can make a noose!")
hammer = Material("Small Hammer", "Are you strong enough to lift that?")
bhammer = Material("Big Hammer", "Don't drop that on your foot... you wont last long with a broken foot")
flint = Material("Flint and Striker", "Do you even know how to use this?")
# add materials to list
materials = [nails, matches, stones, gauze, rope, hammer, bhammer, battery]

# Consumables
cheese = Consumable("Swiss Cheese", "It's got holes in it!", 1, effect=0)
flesh = Consumable("Rotten Flesh", "Wait, this isn't minecraft!", 3, effect=1)
apple = Consumable("Bruised Apple", "Watch your back, before you get bruised too...", 1.5, effect=0)
mouse = Consumable("Mutilated Mouse", "Not very appetizing... yet.", 4, effect=0)
bread = Consumable("Stale loaf of Bread", "This could do some damage... Or you could eat it", 2.5, effect=0)
medicine = Consumable("Mysterious Bottle Of Medicine", "At least you have a painless way out...", 0, effect=2)
ratpoison = Consumable("Rat Poison", "You shouldn't eat this... Should you?", 0, effect=2)
# add consumables to list
consumables = [cheese, flesh, apple, mouse, bread, medicine]

# creates progression items

shoes = Integral("Padded Leather Boots", "Maybe these will help dampen your footsteps...")


item_types = ["consumable", "material", "junk", "weapon"]
# add all items to loot pool
loot_pool = [consumables, materials, junks, weapons]
rooms_loot = []

# creation of enemies
jumbo_rat = Creature(hostile, "Jumbo Rat", "A Jumbo Rat Appears! He looms over you, waiting to strike...", 5, 5)
miniature_dragon = Creature(hostile, "Miniature Dragon", "A Miniature Dragon leaps out of the shadows! Me may be small, but he still breathes fire!", 14, 4)
abraham = Creature(hostile, "Abraham Lincoln", "Abraham Lincoln jumps down from the ceiling! He think's you're a slave trader!", 10, 3)
hermon = Creature(hostile, "Mr. Hermon", "Mr. Hermon crawls out from the corner! Quick, solve his boom/chain problem before he sucks out your brains!", 2, 5)
joe = Creature(hostile, "Joe", "Joe materializes out of thin air! Wait, that's not very threatening! He gives you a bag of almonds", 6, 3)
monk = Creature(hostile, "Decrepid Monk", "A Decrepid Monk appears! He tries to shave your head.", 15, 4)
luke = Creature(hostile, "Luke Skywalker", "Luke skywalker sprints into the corridor. His light saber hums at his side, ready to slice off your philanges", 20, 5)
# add monsters to pool
monsters = [jumbo_rat, miniature_dragon, abraham, hermon, joe, monk, luke]



# transformations. some consumables allow you to transform
shapes = ["Feral Rabbit", "Decrepid Racoon", "Flea Infested Squirrel", "Jumbotron", "Large sewer rat",
          "French Baguette", "Piece of Sidewalk Chalk", "Headless Pigeon", "Piece of Sandpaper"]
shape = Creature(passive)
shape.create(shapes)
room_monsters = []


def craft(item1, item2):
    print("crafted")


# Spawning and generation
def enemy():
    global done
    global fight
    global last_encounter
    global escmsg
    global action
    global fight_msg
    global attackmsg
    global moves
    moves = 0
    last_item = ""
    last_move = 0
    mob = random.choice(monsters)
    fight = True
    # if the player successfully runs from a monster, only to encounter it again immediately after, run this statement
    if last_encounter == mob and last_move == 2:
        border(45)
        print(color.red + f"{last_encounter.name + color.yellow} has followed you to the {color.blue + room_list[current_room][0] + color.yellow}. You may have escaped their clutches before, "
              f"but will you be so lucky again?")
        border(45)
    # if the user kills a monster but encounters it again, run this statement
    elif last_encounter == mob and last_move == 1:
        border(45)
        print(color.red + f"{last_encounter.name + color.yellow} has risen from the dead! Now even stronger, and with a thirst for vengeance!")
        border(45)
    # run the normal message if not a special encounter
    else:
        if mob.description[0] == mob.name[0]:
            x = 1
        else:
            x = 2
        fight_msg = color.bold + color.yellow + mob.description[0:mob.description.index(mob.name[0])] + color.red + mob.description[mob.description.index(mob.name[0]):len(mob.name)+x] + color.reset + color.yellow + mob.description[len(mob.name)+x:]
        border(fight_msg, color.red)
        print(fight_msg)
        border(fight_msg, color.red)
    # continue the fighting loop until fight is set to false. either by the monster defeating you, it being defeated
    while fight is True:
        # give user 3 actions to take upon encountering monster
        opt = ['F', 'R', 'C', 'L']
        act = user_input("custom", "What will you do? [F]ight [R]un [C]hat [L]ast Action", opt)
        actions = [1, 2, 3, 4]
        action = actions[opt.index(act)]
        # first action is to fight, user can choose eligible item from inventory to attack with
        if action == 1 or action == 4 and last_move == 1:
            if player.inv:
                if action != 4:
                    open_inv()
                # choice = int(user_input("custom", "Select an item to use in battle!", range(0, len(playerinv)+1)))
                if action == 4 and last_item != "":
                    if last_item in player.inv:
                        item = last_item
                    else:
                        print(f"You don't have the {last_item} anymore!")
                else:
                    item = player.inv[user_input("custom", "Select an item to use in battle!", range(0, len(player.inv)+1))-1]
                    last_item = item
                # some weapons can kill a mob in one hit
                attackmsg = color.yellow + f"You attacked the {color.reset + color.bright_red + mob.name + color.reset + color.yellow} with your {color.blue + color.bold + item.name + color.reset}"
                border(attackmsg, color.yellow + color.bold)
                print(attackmsg)
                border(attackmsg, color.red)
                time.sleep(.25)
                if item.damage >= mob.hp:
                    print(color.yellow + f"You beat {color.bright_red + mob.name}!")
                    if isinstance(item, Weapon):
                        item.uses -= 1
                    print(color.red + f"{item.uses}{color.yellow} uses left on your {color.blue + color.bold + item.name}")
                    fight = False
                # if the player still has health, damage the monster
                else:
                    # take durability off of item if applicable
                    if isinstance(item, Weapon):
                        item.uses -= 1
                    mob.hp -= item.damage
                    # inform the player of the damage dealt
                    print(color.yellow + f"You did {color.bright_red}{item.damage} damage" + color.reset)
                    print(color.yellow + f"{mob.name} hp is {color.bright_red}{mob.hp}" + color.reset)
                    # monster dies if hp drops below 0
                    if mob.hp <= 0:
                        print(color.yellow + f"You beat {mob.name}. Well done!")
                        fight = False
                    else:
                        last_encounter = mob
                        player.damage(mob.damage)
                        if player.hp == player.maxhp:
                            border(attackmsg, color.red)
                            break
                    if isinstance(item, Weapon) and item.uses <= 0:
                        print(color.yellow + f"Your {color.bright_blue + item.name + color.reset + color.yellow} broke!")
                        player.inv.remove(item)
                    border(attackmsg, color.reset + color.red)
            else:
                print(color.red + "Theres nothing in your inventory!")
                continue
            last_move = 1
        # second combat option is to run
        elif action == 2:
            while True:
                # a pre-determined correct direction is generated. This cannot be a null direction, only one which the player can travel
                r = random.choice(player.room.rooms)
                if r is None:
                    continue
                else:
                    x = player.room.rooms.index(r) + 1
                    break
            print(f"direction is {controls[x]}")
            # ask user which direcion they will run from the monster
            direction = user_input("custom", f"Which way will you run?", controls[1:5])
            # if the player correctly guesses the direction, they escape
            if controls.index(direction) == x:
                print(color.yellow + f"You successfully escaped {color.red + color.bold + mob.name}!")
                fight = False
                travel(r)
            # if the player guesses incorrectly, they die.
            else:
                if player.room.rooms[controls.index(direction)-1] is None:
                    escmsg = color.yellow + f"You tried to escape, but you ran into a wall!"
                else:
                    escmsg = color.yellow + f"You tried to escape but {color.bright_red + mob.name + color.reset + color.yellow} was too fast!"
                border(escmsg, color.red)
                print(escmsg)
                print(color.bright_red + f"{mob.name + color.reset + color.yellow} attacks you.")
                last_encounter = mob
                player.damage(mob.damage)
            last_move = 2
        # the third option is to sit down in front of the monster. In some cases this will provide success over other alternatives
        elif action == 3:
            talk = input("What would you like to talk about?")
            isdead = random.randint(0,4)
            last_encounter = mob
            if isdead == 1:
                print(f"{mob.name} enjoys talking about {talk}! You chat for a few minutes, then they let you pass.")
                fight = False
            else:
                print(f"{mob.name} hates talking about {talk}! They're so angry that they sacrifice their life to ensure your death.")
                print(color.bright_red + f"{mob.name + color.reset + color.yellow} attacks you with the force of a thousand men.")
                kill()
            last_move = 3
        else:
            continue
    # tracks the last monster encountered and how it was defeated


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
    print(color.bright_yellow + "Your satchel contains:" + color.reset)
    i = 1
    # print the name of each item instance with a number in front of each for organization and selection
    border(45)
    for z in player.inv:
        if isinstance(z, Weapon):
            print(color.blue + f"{color.yellow}{i}) {color.blue + z.name} {color.white}[{z.item_type}] {color.green}[uses: {z.uses}] [tier: {z.tier}]")
        else:
            print(color.blue + f"{color.yellow}{i}) {color.blue + z.name} {color.white}[{z.item_type}]")
        i += 1
    border(45)


# def obstacle():
#

# searches the room for loot
def search():
    # player must have available energy to search for loot
    if player.stamina > 0:
        # if the room has available loot, grant it to player and remove energy
        if len(player.room.loot) > 0:
            s = random.choice(player.room.loot)
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
    global moves
    global room
    d = None
    true = False
    # move the player in the specified direction, or inform them to select a valid direction if one is not provided
    while d is None and true is False:
        if direction in controls:
            d = controls.index(direction.upper())
            if d is None:
                print(color.bright_red + "Invalid direction")
                break
            next_room = player.room.rooms[d-1]
            # if the direction selected yields an available room, move the player and inform them of it.
            if next_room is not None:
                player.lastpos = player.pos
                player.last_room = rooms[player.lastpos]
                player.pos = next_room
                player.room = rooms[player.pos]
                room = player.room
                loc()
                moves += 1
                if shoes in player.inv:
                    if random.randint(0,3) == 1:
                        enemy()
                elif moves > 4:
                    print(color.magenta + "You're making a lot of noise. Be more careful...")
                    if random.randint(0, 1) == 1:
                        enemy()
                # 33% chance that a monster will spawn on any given move, other than the first move
                else:
                    if random.randint(0, 2) == 1 and first is not True:
                        enemy()
            # inform the user the direction they selected is not valid
            else:
                print(color.bright_red + "You cant go that direction.")
        elif direction in room.rooms:
            player.lastpos = player.pos
            player.last_room = rooms[player.lastpos]
            player.pos = direction
            player.room = rooms[player.pos]
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
        regen = random.randint(3, 5)
        player.heal(regen)
    elif effect == 1:
        print("you aight")
    elif effect == 2:
        anim = random.choice(shapes)
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
    global fight
    global fight_msg
    global attackmsg
    border(attackmsg, color.reset + color.red)
    if death:
        print(color.bright_red + "You died.")
        done = True
    else:
        if firstdeath:
            pause()
            print(color.yellow + "That's strange... You're back in the grungy stairwell")
            pause()
            print(f"Last you remember you were being struck down by {color.bright_red + last_encounter.name + color.reset}")
            pause()
            print(color.yellow + "You notice your items are gone. Your head is pounding.")
            firstdeath = False
            fight = False

        else:
            print(color.bright_red + "You died.")
            print(color.bright_yellow + "You have been returned to the grungy stairwell")
            print(f"Your items were dropped in the {player.last_room.name}")
        for k in player.inv:
            player.room.add_loot(k)
            player.inv.remove(k)
        player.hp = player.maxhp
        player.stamina = 12
        player.pos = 0
        player.lastpos = player.pos
        player.room = rooms[0]
        player.last_room = player.room





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
    print(color.reset + color.yellow + f"You are in the {color.bright_blue + player.room.name}" + color.reset)
    yes = "no"


# Takes various forms of user input. designed as a more flexible, specialized form of the default input() as needed for the game
def user_input(userinput="none", prompt="default", options=()):
    inp = None
    while inp is None:
        try:
            # if no parameter is specified when the function is called, ask the user to input a command.
            if userinput == "none":
                cmd = input(color.white + color.bold + "Please enter a command:" + color.reset)
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
                        cmd = int(input(color.bright_magenta + color.bold + prompt + color.reset))
                        if cmd in options:
                            inp = cmd
                        else:
                            print(color.bright_red + "Invalid input.")
                    except ValueError:
                        print(color.bright_red + 'Please enter a number.')
                        continue
                else:
                    cmd = input(color.bright_magenta + color.bold + prompt + color.reset).upper()
                    if cmd in options:
                        inp = cmd
                    else:
                        print(color.bright_red + "Invalid input.")
                        continue

            else:
                print(color.bright_red + "Invalid Command")
                continue
        except IndexError:
            print(color.bright_red + "Invalid Command")
            continue
        # the function returns the user input as a value usable as required by a function or otherwise
        return inp


def dialogue(text):
    for item in text:
        print(item, end='', flush=True)
        time.sleep(.1)


def main():
    for each in rooms[1:]:
        loot_tier = random.choices([0, 1, 2, 3], weights=[5, 4, 3, 1.5], k=1)[0]
        loot = gen_loot(3, loot_tier, any_item)
        for loots in loot:
            each.add_loot(loots)
    # creates starting item in the entry room
    stairwell.add_loot(eyepatch)
    # print(color.yellow + "You wake up in a room", end='')
    # time.sleep(2)
    # print(", its dark.")
    # time.sleep(2)
    # print(f"Cold.")
    # time.sleep(1)
    # print(f"Afraid.")
    # time.sleep(1)
    # print(f"And Alone...")
    # time.sleep(1)
    # print(f"You stand up, ", end='')
    # time.sleep(1)
    # print(f"your legs shaking")
    # time.sleep(1)
    # input(f"Press {color.red + controls[1] + color.yellow} to take a step")
    user_input("custom", "You feel a small object press against your bare foot as you shakily take a step. Press 'q' to"
               " pick it up.", 'Q')
    player.collect(flint)
    time.sleep(1)
    user_input("custom", "Press 'e' to open your satchel", 'E')
    open_inv()
    user_input("custom", f"Press 1 to select your {flint.name}", '1')
    speak = f"{color.yellow}You take out your {flint.name} and strike it. "
    dialogue(speak)
    time.sleep(2)
    print(f"The room bursts into view for a split second as the sparks illuminate it", end=', ')
    time.sleep(2.5)
    print("then darkness again.. ")
    time.sleep(1.5)
    print("If only you had something to ignite with it...")
    while done is False:

        # runs each time the game loops, primary point of interaction
        user_input()

    # if the player dies and the loop breaks, the game ends.
    print("Game Over.")


if __name__ == "__main__":
    main()


