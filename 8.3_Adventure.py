'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''


room_list = []
# Room parameters - ["Description", N, S, E, W]
room = ["You are in the main chamber of the dungeon", ]
room_list.append(room)
room = ["", None, None, None, None]
room_list.append(room)
room = ["", None, None, None, None]
room_list.append(room)
room = ["", None, None, None, None]
room_list.append(room)
room = ["", None, None, None, None]
room_list.append(room)

#spawn player
current_room = 0

done = False
while not done:
    
