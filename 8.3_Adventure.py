'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''

import getch
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
controls = directions

settings = False
if settings is False:
    controls
    print(f"Controls are set to: {controls[0]}")
    cont = input(f"Would you like to use: {keys[0]} [k] or {directions[0]} [d].")
    if cont.lower() == "k":
        controls = keys
    elif cont.lower() == "d":
        controls = directions

    settings = True

    if first is True:
        print("Welcome to adventure game!")
        loc()
        first = False

    travel(current_room, userinput("direction"))
    print(current_room)



