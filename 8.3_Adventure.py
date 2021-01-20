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
controlkeys = ['q', 'e']
keys = ['directional keys', 'W', 'S', 'D', 'A']
directions = ['cardinal letters/words', 'N', 'S', 'E', 'W']


loot_pool = [[("Bent Fork", "You couldn't eat with this!"), ("Plastic Hairbrush", "It's Sticky. You run it through your hair"), 'Broken Screwdriver', 'AAA battery',
              'Used Bandage', 'Bloody Eye-patch', 'Cracked Femur', 'Ball of Hair', 'Rubber Band',
              'Ballpoint Pen', 'Wooden Letter Opener', 'Rotted Wooden Plank', 'Broken Mirror'], ['Swiss Army Knife', 'GameBoy Advanced', "Rusty Switchblade", 'Roll of DuctTape',
             "8 inch Chef's Knife", "Box of Matches", '']]
weapons = []
loot_pool.append(weapons)
materials = []
loot_pool.append(materials)
consumables = []
loot_pool.append(consumables)
junk = []
loot_pool.append(junk)


def add(self, loot_type, name, description, tier = 0, damage = 1):
    if loot_type == "weapon":
        item = [name, description, damage, tier]
        weapons.append(item)
    elif loot_type == "material":
        item = (name, description)
        materials.append(item)
    elif loot_type == "consumable":
        item = (name, description, tier)
        consumables.append(item)
    elif loot_type == "junk":
        item = (name, description, tier)
        junk.append(item)


def edit(self, name):
    print(loot_pool[name])

def generate(self, location, tier = 'any', loot_type = 'any'):
    print("Loot generated")
if add == "add":
    add_loot()

addloot = loot(add)


def enemies():
    def add_enemy():

    def


def health():
    global health
    def damage(amount):
        health -= amount
    def regen(amount):
        health += amount



# Prints location of player
def loc():
    playerpos = room_list[current_room]
    print(f"You are in the {playerpos[0]}")


# Takes various forms of user input
def userinput(inp_type):
    inp = None
    while inp is None:
        if inp_type == "direction":
            direct = input(f"Please enter a direction: {directions}").upper()
            if direct[0] in controls[1:5]:
                inp = direct[0]
            else:
                print(f"Invalid Direction")
                continue
        elif inp_type == "action":
            act = input("Please select an action.")
            inp = act
        elif inp_type == "inventory":
            inv = input("")
            inp = inv
    return inp


# Allows the player to travel to different rooms
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
        else:
            print("You cant go that direction.")




# spawn player, set starting variables
current_room = 0
last_room = 0
done = False
first = True
controls = None
health = 100
hunger = 100
energy = 10

# Configures settings
def settings():
    global controls
    print(f"Controls are set to: {controls[0]}")
    cont = input(f"Would you like to use: {keys[0]} [k] or {directions[0]} [d].")
    if cont.lower() == "k":
        controls = keys
    elif cont.lower() == "d":
        controls = directions


# main game loop
while done is False:
    if first is True:
        print("Generating terrain...")
        print("Randomizing loot...")
        print("Spawning monsters...")
        print("Planting a garden...")
        print("Welcome to adventure game!")
        loc()
        first = False

    travel(current_room, userinput("direction"))
    print(current_room)




