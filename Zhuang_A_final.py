#/usr/bin/env/python3
'''
Introduction


Name: Austin Zhuang
Date: 1/19/21

Version 4
Version Notes: (crappy) Final version
'''

#imported modules
import time
import random
#global variables
global row, space, fill, grid, cell_row1, cell_row2, cell_row3, x, y
global role, items, alive, rooms, direction
global room_grid, room_cell_row1, room_cell_row2, room_cell_row3
rooms = {"room00":"", "room01":"", "room02":"", "room10":"", "room11":"", "room12":"", "room20":"", "room21":"", "room22":""}
objectives = ["treasure", "artifacts", "souvenoirs"]

#randomizes location of end objectives
while len(objectives) > 0:
    i = random.randint(0, 2)
    j = random.randint(0, 2)
    if rooms["room{}{}".format(i, j)] != "": continue
    else: rooms["room{}{}".format(i, j)] = objectives.pop()

row = "+ - - - - + - - - - + - - - - +"
space = "|         "
fill = "| ||||||| "
grid = [[space, fill, fill], [fill, fill, fill], [fill, fill, fill]]
room_grid = [[space, fill, fill], [fill, fill, fill], [fill, fill, fill]]
cell_row1 = "{}\n{}{}{}|\n{}{}{}|\n{}{}{}|\n{}{}{}|".format(row, grid[0][0], grid[0][1], grid[0][2], grid[0][0], grid[0][1], grid[0][2], grid[0][0], 
grid[0][1], grid[0][2], grid[0][0], grid[0][1], grid[0][2])
cell_row2 = "{}\n{}{}{}|\n{}{}{}|\n{}{}{}|\n{}{}{}|".format(row, grid[1][0], grid[1][1], grid[1][2], grid[1][0], grid[1][1], grid[1][2], grid[1][0], 
grid[1][1], grid[1][2], grid[1][0], grid[1][1], grid[1][2])
cell_row3 = "{}\n{}{}{}|\n{}{}{}|\n{}{}{}|\n{}{}{}|".format(row, grid[2][0], grid[2][1], grid[2][2], grid[2][0], grid[2][1], grid[2][2], grid[2][0], 
grid[2][1], grid[2][2], grid[2][0], grid[2][1], grid[2][2])
room_cell_row1 = "{}\n{}{}{}|\n{}{}{}|\n{}{}{}|\n{}{}{}|".format(row, room_grid[0][0], room_grid[0][1], room_grid[0][2], room_grid[0][0], room_grid[0][1], room_grid[0][2], room_grid[0][0], 
room_grid[0][1], room_grid[0][2], room_grid[0][0], room_grid[0][1], room_grid[0][2])
room_cell_row2 = "{}\n{}{}{}|\n{}{}{}|\n{}{}{}|\n{}{}{}|".format(row, room_grid[1][0], room_grid[1][1], room_grid[1][2], room_grid[1][0], room_grid[1][1], room_grid[1][2], room_grid[1][0], 
room_grid[1][1], room_grid[1][2], room_grid[1][0], room_grid[1][1], room_grid[1][2])
room_cell_row3 = "{}\n{}{}{}|\n{}{}{}|\n{}{}{}|\n{}{}{}|".format(row, room_grid[2][0], room_grid[2][1], room_grid[2][2], room_grid[2][0], room_grid[2][1], room_grid[2][2], room_grid[2][0], 
room_grid[2][1], room_grid[2][2], room_grid[2][0], room_grid[2][1], room_grid[2][2])
role = ''
items = []
x = 0
y = 0
alive = True
direction = ""

#functions
def init_map():
    '''init_map prints an image of a map with the top left square open and returns None'''
    global cell_row1, cell_row2, cell_row3
    print(cell_row1)
    print(cell_row2)
    print(cell_row3)
    print(row)

def update_map(b, a):
    '''update_map takes in integers a and b and opens the corresponding square of the map 
    (index of 0, so top row middle is a=0, b=1) and returns None'''
    print('Map')
    time.sleep(0.5)
    global grid, cell_row1, cell_row2, cell_row3
    grid[a][b] = space
    if a == 0: cell_row1 = "{}\n{}{}{}|\n{}{}{}|\n{}{}{}|\n{}{}{}|".format(row, grid[0][0], grid[0][1], grid[0][2], grid[0][0], grid[0][1], grid[0][2], grid[0][0], 
    grid[0][1], grid[0][2], grid[0][0], grid[0][1], grid[0][2])
    elif a == 1: cell_row2 = "{}\n{}{}{}|\n{}{}{}|\n{}{}{}|\n{}{}{}|".format(row, grid[1][0], grid[1][1], grid[1][2], grid[1][0], grid[1][1], grid[1][2], grid[1][0], 
    grid[1][1], grid[1][2], grid[1][0], grid[1][1], grid[1][2])
    else: cell_row3 = "{}\n{}{}{}|\n{}{}{}|\n{}{}{}|\n{}{}{}|".format(row, grid[2][0], grid[2][1], grid[2][2], grid[2][0], grid[2][1], grid[2][2], grid[2][0], 
    grid[2][1], grid[2][2], grid[2][0], grid[2][1], grid[2][2])
    print(cell_row1)
    print(cell_row2)
    print(cell_row3)
    print(row)
    time.sleep(0.5)

'''update_roomgrid updates the grid in the same way update map does and returns None'''
def update_roomgrid(b, a):
    global room_grid, room_cell_row1, room_cell_row2, room_cell_row3
    room_grid[a][b] = space
    if a == 0: room_cell_row1 = "{}\n{}{}{}|\n{}{}{}|\n{}{}{}|\n{}{}{}|".format(row, room_grid[0][0], room_grid[0][1], room_grid[0][2], room_grid[0][0], room_grid[0][1], room_grid[0][2], room_grid[0][0], 
    room_grid[0][1], room_grid[0][2], room_grid[0][0], room_grid[0][1], room_grid[0][2])
    elif a == 1: room_cell_row2 = "{}\n{}{}{}|\n{}{}{}|\n{}{}{}|\n{}{}{}|".format(row, room_grid[1][0], room_grid[1][1], room_grid[1][2], room_grid[1][0], room_grid[1][1], room_grid[1][2], room_grid[1][0], 
    room_grid[1][1], room_grid[1][2], room_grid[1][0], room_grid[1][1], room_grid[1][2])
    else: room_cell_row3 = "{}\n{}{}{}|\n{}{}{}|\n{}{}{}|\n{}{}{}|".format(row, room_grid[2][0], room_grid[2][1], room_grid[2][2], room_grid[2][0], room_grid[2][1], room_grid[2][2], room_grid[2][0], 
    room_grid[2][1], room_grid[2][2], room_grid[2][0], room_grid[2][1], room_grid[2][2])
    print(room_cell_row1)
    print(room_cell_row2)
    print(room_cell_row3)
    print(row)
    time.sleep(0.5)

def intro():
    '''intro runs the start of the game, asks the user what role they want to be, and updates the global role and items variables
    and returns None'''
    global role, items
    print("Welcome to the Egyptian tomb! Once you complete a room, you can not enter and stay in it again. Each role has its own unique objective. Choose your role (A/L/T)")
    time.sleep(0.5)
    print("Archaeology student: Starts with a flashlight, archaeology tools, a granola bar, and a water bottle")
    time.sleep(0.5)
    print("Local: Starts with a shovel, a torch, roasted nuts, and a water bottle")
    time.sleep(0.5)
    print("Tourist: Starts with a cellphone, a sandwich, bug spray, and a water bottle")
    time.sleep(0.5)
    role = input("Who do you want to be?\n--> ")
    role = error_trap(role, ['A', 'L', 'T'])
    if role == 'A': items = ['flashlight', 'tools', 'granola', 'water']
    elif role == "L": items = ['shovel', 'torch', 'nuts', 'water']
    else: items = ['phone', 'sandwich', 'spray' 'water']

def game_restart():
    '''game_restart resets the map to the initial map and sets alive to True. Returns None'''
    global alive, x, y, grid, cell_row1, cell_row2, cell_row3
    global room_grid, room_cell_row1, room_cell_row2, room_cell_row3
    end_game = input("You died! Do you want to restart? (Y/N)\n--> ")
    end_game = error_trap(end_game, ['Y', 'N'])
    if end_game.upper() == 'Y':
        alive = True
        x = 0
        y = 0
        grid = [[space, fill, fill], [fill, fill, fill], [fill, fill, fill]]
        room_grid = [[space, fill, fill], [fill, fill, fill], [fill, fill, fill]]
        cell_row1 = "{}\n{}{}{}|\n{}{}{}|\n{}{}{}|\n{}{}{}|".format(row, grid[0][0], grid[0][1], grid[0][2], grid[0][0], grid[0][1], grid[0][2], grid[0][0], 
        grid[0][1], grid[0][2], grid[0][0], grid[0][1], grid[0][2])
        cell_row2 = "{}\n{}{}{}|\n{}{}{}|\n{}{}{}|\n{}{}{}|".format(row, grid[1][0], grid[1][1], grid[1][2], grid[1][0], grid[1][1], grid[1][2], grid[1][0], 
        grid[1][1], grid[1][2], grid[1][0], grid[1][1], grid[1][2])
        cell_row3 = "{}\n{}{}{}|\n{}{}{}|\n{}{}{}|\n{}{}{}|".format(row, grid[2][0], grid[2][1], grid[2][2], grid[2][0], grid[2][1], grid[2][2], grid[2][0], 
        grid[2][1], grid[2][2], grid[2][0], grid[2][1], grid[2][2])
        room_cell_row1 = "{}\n{}{}{}|\n{}{}{}|\n{}{}{}|\n{}{}{}|".format(row, room_grid[0][0], room_grid[0][1], room_grid[0][2], room_grid[0][0], room_grid[0][1], room_grid[0][2], room_grid[0][0], 
        room_grid[0][1], room_grid[0][2], room_grid[0][0], room_grid[0][1], room_grid[0][2])
        room_cell_row2 = "{}\n{}{}{}|\n{}{}{}|\n{}{}{}|\n{}{}{}|".format(row, room_grid[1][0], room_grid[1][1], room_grid[1][2], room_grid[1][0], room_grid[1][1], room_grid[1][2], room_grid[1][0], 
        room_grid[1][1], room_grid[1][2], room_grid[1][0], room_grid[1][1], room_grid[1][2])
        room_cell_row3 = "{}\n{}{}{}|\n{}{}{}|\n{}{}{}|\n{}{}{}|".format(row, room_grid[2][0], room_grid[2][1], room_grid[2][2], room_grid[2][0], room_grid[2][1], room_grid[2][2], room_grid[2][0], 
        room_grid[2][1], room_grid[2][2], room_grid[2][0], room_grid[2][1], room_grid[2][2])

def check_objective():
    '''check_objective checks if the end objective for the role the player chose is in the room they completed
    and returns True if yes and False if no'''
    room = "room{}{}".format(y, x)
    if role == 'A' and rooms[room] == 'artifacts':
        print("You found {}!".format(rooms[room]))
        return True
    elif role == 'L' and rooms[room] == 'treasure':
        print("You found {}!".format(rooms[room]))
        return True
    elif role == 'T' and rooms[room] == 'souvenoirs': 
        print("You found {}!".format(rooms[room]))
        return True
    else: return False

def pause():
    '''pause creats a break between rooms so the user knows they are in a different room and returns None'''
    for i in range(3):
        print("|")
        time.sleep(0.5)

def error_trap(value, valid_inputs):
    '''error trap accepts the input, value, a list with the valid inputs, valid_inputs,
    and the variable type of the input, var, you want and returns an input with all the requirements'''
    while value not in valid_inputs:
        value = input("Invalid input. Please try again\n--> ")
    else:
        return value

'''Each room_x function runs thorugh the challenge/dialogue in that room returns whether the user is alive or not after that room'''
def room_1():
    global direction
    print("Map")
    time.sleep(0.5)
    init_map()
    time.sleep(0.5)
    direction = input("You enter the first room. Do you want to go right or down? (R/D)\n--> ")
    direction = error_trap(direction, ['R', 'D'])

def room_2():
    pause()
    global grid, cell_row1, cell_row2, cell_row3
    correct_path = ['R', 'D', 'D', 'R']
    i = 0
    print("The doors slam shut behind you. In front of you is a three by three grid. You step on the first tile.")
    print("Grid")
    update_roomgrid(0, 0)
    step = input("Do you want to go right or down? (R/D)\n--> ")
    step = error_trap(step, ['R', 'D'])
    while step == correct_path[i]:
        if i == 0: 
            update_roomgrid(1, 0)
            step = input("Do you want to go right or down? (R/D)\n--> ")
            step = error_trap(step, ['R', 'D'])
        elif i == 1: 
            update_roomgrid(1, 1)
            step = input("Do you want to go right, down, or left? (R/D/L)\n--> ")
            step = error_trap(step, ['R', 'D', 'L'])
        elif i == 2: 
            update_roomgrid(1, 2)
            step = input("Do you want to go right or left? (R/L)\n--> ")
            step = error_trap(step, ['R', 'L'])
        else: 
            update_roomgrid(2, 2)
            print("You made it past the falling tiles!")
            time.sleep(0.5)
            return True
        i += 1
    else: 
        print("The tile crumbles underneath you, revealing very pointy spikes. Nice knowing you.")
        time.sleep(0.5)
        return False

def room_3():
    pause()
    correct_waits = ["5", "15", "15"]
    i = 0
    print("The doors slam shut behind you. In front of you are three machines shooting darts at irregular intervals. You think their poisonous, and you don't want to find out.")
    wait = input("Do you want to wait 5, 10, or 15 seconds?\n--> ")
    wait = error_trap(wait, ["5", "10", "15"])
    while correct_waits[i] == wait:
        print("You wait {} seconds and make a run for it. Luckily, the machine stops shooting the exact moment you pass it.".format(wait))
        if i < 2: 
            wait = input("Do you want to wait 5, 10, or 15 seconds?\n--> ")
            wait = error_trap(wait, ["5", "10", "15"])
        else: 
            print("You made it past the darts!")
            time.sleep(0.5)
            return True
        i += 1
    else:
        print("You wait {} seconds and make a run for it. As you are running by, you feel a pinch, and your vision starts blurring.\nAt least now you know they're poisonous.".format(wait))
        time.sleep(0.5)
        return False

def room_4():
    pause()
    print("The doors slam shut behind you. In front of you is a ladder over some pointy spikes. Those don't look they would be fun to fall onto.")
    time.sleep(0.5)
    chance = random.randint(1, 4)
    if chance == 4:
        print("You climb onto the ladder and begin crossing, but your hand slips and you fall off.")
        time.sleep(0.5)
        return False
    else:
        print("You climb onto the ladder and cross with ease.")
        time.sleep(0.5)
        return True

def room_5():
    pause()
    print("The doors slam shut behind you. The noise disturbs the swarm of locusts in the room. Annoyed, they go straight at you.")
    time.sleep(0.5)
    print("Your items:")
    time.sleep(0.5)
    for item in items:
        print(item)
        time.sleep(0.5)
    choice = input("What will you use to stop the locusts?\n--> ")
    choice = error_trap(choice, items)
    if choice == 'water' or choice == 'phone':
        print("You chuck your {} at the swarm. It passes right through it, and the bugs keep coming. What did you think was going to happen?".format(choice))
        time.sleep(0.5)
        return False
    elif choice == 'shovel' or choice == 'tools':
        print("You swing your {} at the swarm, which only makes them angrier. Great job!".format(choice))
        time.sleep(0.5)
        return False
    elif choice == 'nuts' or choice == 'sandwich' or choice == 'granola':
        print("You throw your {} on the ground, distracting the locuts. You try to run towards the exit, but it's still sealed shut. The locuts turn back to you. :(".format(choice))
        time.sleep(0.5)
        return False
    elif choice == 'flashlight':
        print("You turn on your flashlight and shine it at the swarm. The locusts disintegrate, and you get out alive.")
        time.sleep(0.5)
        return True
    elif choice == 'torch':
        print("The flame on your torch burns all the locusts, and you get out alive.")
        time.sleep(0.5)
        return True
    else:
        print("You spray the locusts, and, thankfully, the bug spray does its job. You get out alive")
        time.sleep(0.5)
        return True

def room_6():
    pause()
    prob = random.randint(1, 10)
    print("The room looks empty.")
    time.sleep(0.5)
    if prob == 4:
        print("You accidentally step on a button on the floor, and you hear rumbling. You look up, and the last thing you see is a boulder.")
        time.sleep(0.5)
        return False
    else: 
        print("Free room!")
        time.sleep(0.5)
        return True

def room_7():
    pause()
    num_guesses = 7
    print("The doors slam shut behind you. In front of you is a...monkey? Holding a guess the number game?")
    ans = random.randint(1, 100)
    guess = 0
    while guess != ans and num_guesses > 0:
        guess = input("Guess an integer between 1 and 100\n--> ")
        while not guess.isdigit():
            guess = input("Please input an integer between 1 and 100\n--> ")
        else: guess = int(guess)
        if guess < ans:
            print("Too low!")
            num_guesses -= 1
            time.sleep(0.5)
            print("Number of guesses left: {}".format(num_guesses))
            time.sleep(0.5)
            continue
        elif guess > ans:
            print("Too high!")
            num_guesses -= 1
            time.sleep(0.5)
            print("Number of guesses left: {}".format(num_guesses))
            time.sleep(0.5)
            continue
        else:
            num_guesses = 0
            continue
    else:
        if guess == ans:
            print("You guessed the number right!")
            time.sleep(0.5)
            return True
        elif num_guesses == 0:
            print("The monkey's eyes flash red. You hear explosions in the distance, and the roof collapses. Not good")
            time.sleep(0.5)
            return False

def room_8():
    pause()
    print("The doors slam shut behind you. In front of you is a maze.")
    correct_path = ['L', 'D', 'R', 'R', 'U', 'L', 'U']
    i = 0
    direction = input("You enter the maze. Do you want to go left, right, or up? (L/R/U)\n--> ")
    direction = error_trap(direction, ['L', 'R', 'U'])
    while direction.upper() == correct_path[i]:
        if i < 6:
            direction = input("You enter an identical room. Do you want to go left, right, up, or down? (L/R/U/D)\n--> ")
            direction = error_trap(direction, ['L', 'R', 'U', 'D'])
        else: 
            print("You made it out of the maze!")
            time.sleep(0.5)
            return True
        i += 1
    else: 
        print("You enter an identical room, and you notice a giant minotaur in the middle of it. It turns around and stares you down. This does not end well for you.")
        time.sleep(0.5)
        return False

def room_9():
    pause()
    yes_no = input("There's just a pile of dirt in the center. Do you want to search it? (Y/N)\n--> ")
    yes_no = error_trap(yes_no, ['Y', 'N'])
    if yes_no == 'Y':
        if role == 'A':
            chance = random.randint(1, 10)
            if chance == 4:
                print("You use your archaeology tools to dig through the pile, and your spade hits something. You hear a click. Uh oh.")
                time.sleep(0.5)
                return False
            else: 
                print("You find nothing in the pile. Crazy. I guess it was just a pile of dirt.")
                time.sleep(0.5)
                return True
        elif role == 'L':
            chance = random.randint(1, 5)
            if chance == 4:
                print("You use your shovel to dig through the pile, and it hits something. You hear a click. Uh oh.")
                time.sleep(0.5)
                return False
            else: 
                print("You find nothing in the pile. Crazy. I guess it was just a pile of dirt.")
                time.sleep(0.5)
                return True
        else:
            chance = random.randint(1, 20)
            if chance == 4:
                print("You use your hands to dig through the pile, and they hit something. You hear a click. Uh oh.")
                time.sleep(0.5)
                return False
            else: 
                print("You find nothing in the pile. Crazy. I guess it was just a pile of dirt.")
                time.sleep(0.5)
                return True
    else:
        print("It is just a pile of dirt. I would skip it too")
        time.sleep(0.5)
        return True

#main
'''main goes through every possibility/choice in the game'''
play_again = 'Y'
while play_again == 'Y':
    while alive:
        intro()
        if role == 'A': 
            print("You are an archaeology student starting your first excavation in an Egyptian tomb.")
        elif role == 'L': 
            print("You are a local helping archaeologists dig but decide to leave the group and search for treasure.")
        else:
            print("You signed up for a tomb tour in Egypt but woke up late and missed it. You decide to explore the tomb by yourself.")
        time.sleep(0.5)
        win = check_objective()
        if win: break
        room_1()
        if direction == 'R':
            x += 1
            alive = room_2()
            if not alive: 
                game_restart()
                continue
            win = check_objective()
            if win: break
            update_map(x, y)
            direction = input("You are in the second room. Do you want to go right or down? (R/D)\n--> ")
            direction = error_trap(direction, ['R', 'D'])
            if direction == 'R':
                x += 1
                alive = room_3()
                if not alive:
                    game_restart()
                    continue
                win = check_objective()
                if win: break
                update_map(x, y)
                print("You are in the third room. You can only go down")
                y += 1
                alive = room_6()
                if not alive:
                    game_restart()
                    continue
                win = check_objective()
                if win: break
                update_map(x, y)
                direction = input("You are in the sixth room. Do you want to go left or down? (L/D)\n--> ")
                direction = error_trap(direction, ['L', 'D'])
                if direction == "D":
                    y += 1
                    alive = room_9()
                    if not alive:
                        game_restart()
                        continue
                    win = check_objective()
                    if win: break
                    update_map(x, y)
                    print("You are in the ninth room. You can only go left")
                    x -= 1
                    alive = room_8()
                    if not alive:
                        game_restart()
                        continue
                    win = check_objective()
                    if win: break
                    update_map(x, y)
                    direction = input("You are in the eighth room. Do you want to go left or up? (L/U)\n--> ")
                    direction = error_trap(direction, ['L', 'U'])
                    if direction == 'L':
                        x -= 1
                        alive = room_7()
                        if not alive:
                            game_restart()
                            continue
                        win = check_objective()
                        if win: break
                        update_map(x, y)
                        print("You are in the seventh room. You can only go up.")
                        y -= 1
                        alive = room_4()
                        if not alive:
                            game_restart()
                            continue
                        win = check_objective()
                        if check_objective(): break
                        update_map(x, y)
                        print("You are in the fourth room. You can only go right.")
                        x += 1
                        alive = room_4()
                        if not alive:
                            game_restart()
                            continue
                        win = check_objective()
                        if win: break
                    else:
                        y -= 1
                        alive = room_5
                        if not alive:
                            game_restart()
                            continue
                        win = check_objective()
                        if win: break
                        update_map(x, y)
                        print("You are in the fifth room. You can only go left.")
                        x -= 1
                        alive = room_4
                        if not alive:
                            game_restart()
                            continue
                        win = check_objective()
                        if win: break
                        update_map(x, y)
                        print("You are in the fourth room. You can only go down.")
                        y += 1
                        alive = room_7
                        if not alive:
                            game_restart()
                            continue
                        win = check_objective()
                        if win: break
                else:
                    x -= 1
                    alive = room_5()
                    if not alive:
                        game_restart()
                        continue
                    win = check_objective()
                    if win: break
                    update_map(x, y)
                    direction = input("You are in the fifth room. Do you want to go left or down? (L/D)\n--> ")
                    direction = error_trap(direction, ['L', 'D'])
                    if direction == 'L':
                        x -= 1
                        alive = room_4()
                        if not alive:
                            game_restart()
                            continue
                        win = check_objective()
                        if win: break
                        update_map(x, y)
                        print("You are in the fourth room. You can only go down.")
                        y += 1
                        alive = room_7()
                        if not alive:
                            game_restart()
                            continue
                        win = check_objective()
                        if win: break
                        update_map(x, y)
                        print("You are in the seventh room. You can only go right")
                        x += 1
                        alive = room_8()
                        if not alive:
                            game_restart()
                            continue
                        win = check_objective()
                        if win: break
                        update_map(x, y)
                        print("You are in the eighth room. You can only go right")
                        x += 1
                        alive = room_9()
                        if not alive:
                            game_restart()
                            continue
                        win = check_objective()
                        if win: break
                    else:
                        y += 1
                        alive = room_8()
                        if not alive:
                            game_restart()
                            continue
                        win = check_objective()
                        if win: break
                        update_map(x, y)
                        direction = input("You are in the eighth room. Do you want to go left or right? (L/R)")
                        direction = error_trap(direction, ['L', 'R'])
                        if direction == 'L':
                            x -= 1
                            alive = room_7()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                            update_map(x, y)
                            print("You are in the seventh room. You go back into the eighth room and head to the room in the bottom right corner.")
                            x += 2
                            alive = room_9()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                        else:
                            x += 1
                            alive = room_9()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                            update_map(x, y)
                            print("You are in the ninth room. You go back into the eighth room and head to the room in the bottom left corner.")
                            alive = room_7()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
            else:
                y += 1
                alive = room_5()
                if not alive: 
                    game_restart()
                    continue
                win = check_objective()
                if win: break
                update_map(x, y)
                direction = input("You are in the fifth room. Do you want to go left, right, or down? (L/R/D)\n--> ")
                direction = error_trap(direction, ['L', 'R', 'D'])
                if direction == 'L':
                    x -= 1
                    alive = room_4()
                    if not alive:
                        game_restart()
                        continue
                    win = check_objective()
                    if win: break
                    update_map(x, y)
                    print("You are in the fourth room. You can only go down.")
                    y += 1
                    alive = room_7()
                    if not alive:
                        game_restart()
                        continue
                    win = check_objective()
                    if win: break
                    update_map(x, y)
                    print("You are in the seventh room. You can only go right.")
                    x += 1
                    alive = room_8()
                    if not alive:
                        game_restart()
                        continue
                    win = check_objective()
                    if win: break
                    update_map(x, y)
                    print("You are in the eighth room. You can only go right.")
                    x += 1
                    alive = room_9()
                    if not alive:
                        game_restart()
                        continue
                    win = check_objective()
                    if win: break
                    update_map(x, y)
                    print("You are in the ninth room. You can only go up.")
                    y -= 1
                    alive = room_6()
                    if not alive:
                        game_restart()
                        continue
                    win = check_objective()
                    if win: break
                    update_map(x, y)
                    print("You are in the sixth room. You can only go up.")
                    alive = room_3()
                    if not alive:
                        game_restart()
                        continue
                    win = check_objective()
                    if win: break
                elif direction == 'R':
                    x += 1
                    alive = room_6()
                    if not alive:
                        game_restart()
                        continue
                    win = check_objective()
                    if win: break
                    update_map(x, y)
                    direction = input("You are in the sixth room. Do you want to go up or down? (U/D)")
                    direction = error_trap(direction, ['U', 'D'])
                    if direction == 'D':
                        y += 1
                        alive = room_9()
                        if not alive:
                            game_restart()
                            continue
                        win = check_objective()
                        if win: break
                        update_map(x, y)
                        direction = input("You are in the ninth room. Do you want to go up to the top right corner or left? (U/L)")
                        direction = error_trap(direction, ['U', 'L'])
                        if direction == 'U':
                            y -= 2
                            alive = room_3()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                            update_map(x, y)
                            print("You are in the third room. You head to the middle room in the bottom row.")
                            x -= 1
                            y += 2
                            alive = room_8()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                            update_map(x, y)
                            print("You are in the eighth room. You can only go left.")
                            x -= 1
                            alive = room_7()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                            update_map(x, y)
                            print("You are in the seventh room. You can only go up.")
                            y -= 1
                            alive = room_4()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                            update_map(x, y)
                else:
                    y += 1
                    alive = room_8()
                    if not alive:
                        game_restart()
                        continue
                    win = check_objective()
                    if win: break
                    update_map(x, y)
                    direction = input("You are in the eighth room. Do you want to go left or right? (L/R)\n--> ")
                    direction = error_trap(direction, ['L', 'R'])
                    if direction == 'L':
                        x -= 1
                        alive = room_7()
                        if not alive:
                            game_restart()
                            continue
                        win = check_objective()
                        if win: break
                        update_map(x, y)
                        direction = input("You are in the seventh room. Do you want to go up or right to the bottom right corner? (U/R)\n--> ")
                        direction = error_trap(direction, ['U', 'R'])
                        if direction == 'R':
                            x += 2
                            alive = room_9()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                            update_map(x, y)
                            print("You are in the ninth room. You can only go up.")
                            y -= 1
                            alive = room_6()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                            print("You are in the sixth room. You can only go left to the middle room in the left column of the map.")
                            x -= 2
                            alive = room_4()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                        else:
                            y -= 1
                            alive = room_4()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                            update_map(x, y)
                            print("You are in the fourth room. You can only go right to the middle room in the right column of the map.")
                            x += 2
                            alive = room_6()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                            update_map(x, y)
                            direction = input("You are in the sixth room. Do you want to go up or down? (U/D)\n-->")
                            direction = error_trap(direction, ['U', 'D'])
                            if direction == 'D':
                                y += 1
                                alive = room_9()
                                if not alive:
                                    game_restart()
                                    continue
                                win = check_objective()
                                if win: break
                                update_map(x, y)
                                print("You are in the ninth room. You can only go up to the top right corner.")
                                alive = room_3()
                                if not alive:
                                    game_restart()
                                    continue
                                win = check_objective()
                                if win: break
                            else:
                                y -= 1
                                alive = room_3()
                                if not alive:
                                    game_restart()
                                    continue
                                win = check_objective()
                                if win: break
                                update_map(x, y)
                                print("You are in the third room. You can only go down to the bottom right corner.")
                                alive = room_9()
                                if not alive:
                                    game_restart()
                                    continue
                                win = check_objective()
                                if win: break
                    else:
                        x += 1
                        alive = room_9()
                        if not alive:
                            game_restart()
                            continue
                        win = check_objective()
                        if win: break
                        update_map(x, y)
                        direction = input("You are in the ninth room. Do you want to go up or left to the bottom left corner (U/L)")
                        direction = error_trap(direction, ['U', 'L'])
                        if direction == 'L':
                            x -= 2
                            alive = room_7()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                            update_map(x, y)
                            print("You are in the seventh room. You can only go up.")
                            y -= 1
                            alive = room_4()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                            update_map(x, y)
                            print("You are in the fourth room. You can only go right to the middle room in the right column.")
                            x += 2
                            alive = room_4()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                        else:
                            y -= 1
                            alive = room_6()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                            update_map(x, y)
                            print("You are in the sixth room. You can only go left to the middle room in the left column.")
                            x -= 2
                            alive = room_4()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                            update_map(x, y)
                            print("You are in the fourth room. You can only go down.")
                            y += 1
                            alive = room_7()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
        else:
            y += 1
            alive = room_4()
            if not alive:
                game_restart()
                continue
            win = check_objective()
            if win: break
            update_map(x, y)
            direction = input("You are in the fourth room. Do you want to go right or down? (R/D)\n--> ")
            direction = error_trap(direction, ['R', 'D'])
            if direction == 'D':
                y += 1
                alive = room_7()
                if not alive:
                    game_restart()
                    continue
                win = check_objective()
                if win: break
                update_map(x, y)
                print("You are in the seventh room. You can only go right.")
                x += 1
                alive = room_8()
                if not alive:
                    game_restart()
                    continue
                win = check_objective()
                if win: break
                update_map(x, y)
                direction = input("You are in the eighth room. Do you want to go right or up? (R/U)\n--> ")
                direction = error_trap(direction, ['R', 'U'])
                if direction == 'U':
                    y -= 1
                    alive = room_5()
                    if not alive:
                        game_restart()
                        continue
                    win = check_objective()
                    if win: break
                    update_map(x, y)
                    direction = input("You are in the fifth room. Do you want to go right or up (R/U)\n--> ")
                    direction = error_trap(direction, ['R', 'U'])
                    if direction == 'R':
                        x += 1
                        alive = room_6()
                        if not alive:
                            game_restart()
                            continue
                        win = check_objective()
                        if win: break
                        update_map(x, y)
                        direction = input("You are in the sixth room. Do you want to go up or down? (U/D)\n--> ")
                        direction = error_trap(direction, ['U', 'D'])
                        if direction == 'U':
                            y -= 1
                            alive = room_3()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                            update_map(x, y)
                            direction = input("You are in the third room. Do you want to go left or down to the bottom right corner? (L/D)\n--> ")
                            direction = error_trap(direction, ['L', 'D'])
                            if direction == 'L':
                                x -= 1
                                alive = room_2()
                                if not alive:
                                    game_restart()
                                    continue
                                win = check_objective()
                                if win: break
                                update_map(x, y)
                                print("You are in the second room. You head to the bottom right corner.")
                                alive = room_9()
                                if not alive:
                                    game_restart()
                                    continue
                                win = check_objective()
                                if win: break
                            else:
                                y += 2
                                alive = room_9()
                                if not alive:
                                    game_restart()
                                    continue
                                win = check_objective()
                                if win: break
                                update_map(x, y)
                                print("You are in the ninth room. You head to the middle room in the top row.")
                                alive = room_9()
                                if not alive:
                                    game_restart()
                                    continue
                                win = check_objective()
                                if win: break
                        else:
                            y += 1
                            alive = room_9()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                            update_map(x, y)
                            print("You are in the ninth room. You can only go to the top right corner.")
                            y -= 2
                            alive = room_3()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                            update_map(x, y)
                            print("You are in the third room. You can only go left.")
                            alive = room_2()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                    else:
                        y -= 1
                        alive = room_2()
                        if not alive:
                            game_restart()
                            continue
                        win = check_objective()
                        if win: break
                        update_map(x, y)
                        print("You are in the second room. You can only go right.")
                        x += 1
                        alive = room_3()
                        if not alive:
                            game_restart()
                            continue
                        win = check_objective()
                        if win: break
                        update_map(x, y)
                        print("You are in the third room. You can only go down.")
                        y += 1
                        alive = room_6()
                        if not alive:
                            game_restart()
                            continue
                        win = check_objective()
                        if win: break
                        update_map(x, y)
                        print("You are in the sixth room. You can only go down.")
                        alive = room_9()
                        if not alive:
                            game_restart()
                            continue
                        win = check_objective()
                        if win: break
                else:
                    x += 1
                    alive = room_9()
                    if not alive:
                        game_restart()
                        continue
                    win = check_objective()
                    if win: break
                    update_map(x, y)
                    print("You are in the ninth room. You can only go up.")
                    y -= 1
                    alive = room_6()
                    if not alive:
                        game_restart()
                        continue
                    win = check_objective()
                    if win: break
                    update_map(x, y)
                    direction = input("You are in the sixth room. Do you want to go left or up? (L/U)")
                    direction = error_trap(direction, ['L', 'U'])
                    if direction == 'L':
                        x -= 1
                        alive = room_5()
                        if not alive:
                            game_restart()
                            continue
                        win = check_objective()
                        if win: break
                        update_map(x, y)
                        print("You are in the fifth room. You can only go up.")
                        y -= 1
                        alive = room_2()
                        if not alive:
                            game_restart()
                            continue
                        win = check_objective()
                        if win: break
                        update_map(x, y)
                        print("You are in the second room. You can only go right.")
                        alive = room_3()
                        if not alive:
                            game_restart()
                            continue
                        win = check_objective()
                        if win: break
                    else:
                        y -= 1
                        alive = room_3()
                        if not alive:
                            game_restart()
                            continue
                        win = check_objective()
                        if win: break
                        update_map(x, y)
                        print("You are in the third room. You can only go left.")
                        x -= 1
                        alive = room_2()
                        if not alive:
                            game_restart()
                            continue
                        win = check_objective()
                        if win: break
                        update_map(x, y)
                        print("You are in the second room. You can only go down.")
                        alive = room_5()
                        if not alive:
                            game_restart()
                            continue
                        win = check_objective()
                        if win: break
            else:
                x += 1
                alive = room_5()
                if not alive:
                    game_restart()
                    continue
                win = check_objective()
                if win: break
                update_map(x, y)
                direction = input("You are in the fifth room. Do you want to go right, up, or down? (R/U/D)\n--> ")
                direction = error_trap(direction, ['R', 'U', 'D'])
                if direction == 'R':
                    x += 1
                    alive = room_6()
                    if not alive:
                        game_restart()
                        continue
                    win = check_objective()
                    if win: break
                    update_map(x, y)
                    direction = input("You are in the sixth room. Do you want to go up or down? (U/D)\n--> ")
                    direction = error_trap(direction, ['U', 'D'])
                    if direction == 'U':
                        y -= 1
                        alive = room_3()
                        if not alive:
                            game_restart()
                            continue
                        win = check_objective()
                        if win: break
                        update_map(x, y)
                        direction = input("You are in the third room. Do you want to go left or down to the bottom right corner? (L/D)\n--> ")
                        direction = error_trap(direction, ['L', 'D'])
                        if direction == 'L':
                            x -= 1
                            alive = room_2()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                            update_map(x, y)
                            print("You are in the second room. You head down to the bottom right corner.")
                            x += 1
                            y += 2
                            alive = room_9()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                            update_map(x, y)
                            print("You are in the ninth room. You can only go left.")
                            x -= 1
                            alive = room_8()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                            update_map(x, y)
                            print("You are in the eighth room. You can only go left.")
                            alive = room_7()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                        else: 
                            y += 2
                            alive = room_9()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                            update_map(x, y)
                            print("You are in the ninth room. You can only go left.")
                            x -= 1
                            alive = room_8()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                            update_map(x, y)
                            print("You are in the eighth room. You can only go left.")
                            x -= 1
                            alive = room_7()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                            update_map(x, y)
                            print("You are in the seventh room. You head to the middle room in the top row.")
                            alive = room_2()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                    else:
                        y += 1
                        alive = room_9()
                        if not alive:
                            game_restart()
                            continue
                        win = check_objective()
                        if win: break
                        update_map(x, y)
                        direction = input("You are in the ninth room. Do you want to go left or up to the top right corner? (L/U)\n--> ")
                        direction = error_trap(direction, ['L', 'U'])
                        if direction == 'L':
                            x -= 1
                            alive = room_8()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                            update_map(x, y)
                            print("You are in the eighth room. You can only go left.")
                            x -= 1
                            alive = room_7()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                            update_map(x, y)
                            print("You are in the seventh room. You can only go to the top right corner")
                            x += 2
                            y -= 2
                            alive = room_3()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                            update_map(x, y)
                            print("You are in the third room. You can only go left.")
                            alive = room_2()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                        else:
                            y -= 2
                            alive = room_3()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                            print("You are in the third room. You can only go left.")
                            x -= 1
                            alive = room_2()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                            print("You are in the second room. You can only go down to the middle room in the bottom row.")
                            y += 2
                            alive = room_8()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                            print("You are in the eighth room. You can only go left.")
                            alive = room_7()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                elif direction == 'U':
                    y -= 1
                    alive = room_2()
                    if not alive:
                        game_restart()
                        continue
                    win = check_objective()
                    if win: break
                    update_map(x, y)
                    print("You are in the second room. You can only go right.")
                    x += 1
                    alive = room_3()
                    if not alive:
                        game_restart()
                        continue
                    win = check_objective()
                    if win: break
                    update_map(x, y)
                    print("You are in the third room. You can only go down.")
                    y += 1
                    alive = room_6()
                    if not alive:
                        game_restart()
                        continue
                    win = check_objective()
                    if win: break
                    update_map(x, y)
                    print("You are in the sixth room. You can only go down.")
                    y += 1
                    alive = room_9()
                    if not alive:
                        game_restart()
                        continue
                    win = check_objective()
                    if win: break
                    update_map(x, y)
                    print("You are in the ninth room. You can only go left.")
                    x -= 1
                    alive = room_8()
                    if not alive:
                        game_restart()
                        continue
                    win = check_objective()
                    if win: break
                    update_map(x, y)
                    print("You are in the eighth room. You can only go left.")
                    x -= 1
                    alive = room_7()
                    if not alive:
                        game_restart()
                        continue
                    win = check_objective()
                    if win: break
                else:
                    y += 1
                    alive = room_8()
                    if not alive:
                        game_restart()
                        continue
                    win = check_objective()
                    if win: break
                    update_map(x, y)
                    direction = input("You are in the eighth room. Do you want to go right or left? (R/L)\n--> ")
                    direction = error_trap(direction, ['R', 'L'])
                    if direction == 'R':
                        x += 1
                        alive = room_9()
                        if not alive:
                            game_restart()
                            continue
                        win = check_objective()
                        if win: break
                        update_map(x, y)
                        direction = input("You are in the ninth room. Do you want to go left to the bottom left corner or up? (L/U)")
                        if direction == 'L':
                            x -= 2
                            alive = room_7()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                            update_map(x, y)
                            print("You are in the seventh room. You head to the middle room in the right column.")
                            x += 2
                            y -= 1
                            alive = room_6()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                        else:
                            y -= 1
                            alive = room_6()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                            update_map(x, y)
                            print("You are in the sixth room. You head to the bottom left corner.")
                            x -= 2
                            y += 1
                            alive = room_7()
                            if not alive:
                                game_restart()
                                continue
                            win = check_objective()
                            if win: break
                    else:
                        x -= 1
                        alive = room_7()
                        if not alive:
                            game_restart()
                            continue
                        win = check_objective()
                        if win: break
                        update_map(x, y)
                        print("You are in the seventh room. You can only go to the bottom right corner.")
                        x += 2
                        alive = room_9()
                        if not alive:
                            game_restart()
                            continue
                        win = check_objective()
                        if win: break
                        update_map(x, y)
                        print("You are in the ninth room. You can only go up.")
                        y -= 1
                        alive = room_6()
                        if not alive:
                            game_restart()
                            continue
                        win = check_objective()
                        if win: break
                        update_map(x, y)
                        print("You are in the sixth room. You can only go up.")
                        y -= 1
                        alive = room_3()
                        if not alive:
                            game_restart()
                            continue
                        win = check_objective()
                        if win: break
                        update_map(x, y)
                        print("You are in the third room. You can only go left.")
                        alive = room_2()
                        if not alive:
                            game_restart()
                            continue
                        win = check_objective()
                        if win: break
    if role == 'A' and alive:
        print("You find some old clay pots. Dig successful!")
    elif role == 'L' and alive:
        print("You find some gold and jewels in a big chest. Looks like leaving the group was the right decision after all.")
    elif role == 'T' and alive:
        print("You found some arrows and spearheads that would look pretty nice on your mantel. You missed your tour, but the souvenoirs make up for it, right?")
    time.sleep(0.5)
    print("Thanks for playing!")
    play_again = input("Do you want to play again? (Y/N)\n--> ")
    play_again = error_trap(play_again, ['Y', 'N'])
    if play_again == 'Y':
        alive = True
        while len(objectives) > 0:
            i = random.randint(0, 2)
            j = random.randint(0, 2)
            if rooms["room{}{}".format(i, j)] != "": continue
            else: rooms["room{}{}".format(i, j)] = objectives.pop()
        x = 0
        y = 0
        room_grid = room_grid = [[space, fill, fill], [fill, fill, fill], [fill, fill, fill]]
        room_cell_row1 = "{}\n{}{}{}|\n{}{}{}|\n{}{}{}|\n{}{}{}|".format(row, room_grid[0][0], room_grid[0][1], room_grid[0][2], room_grid[0][0], room_grid[0][1], room_grid[0][2], room_grid[0][0], 
        room_grid[0][1], room_grid[0][2], room_grid[0][0], room_grid[0][1], room_grid[0][2])
        room_cell_row2 = "{}\n{}{}{}|\n{}{}{}|\n{}{}{}|\n{}{}{}|".format(row, room_grid[1][0], room_grid[1][1], room_grid[1][2], room_grid[1][0], room_grid[1][1], room_grid[1][2], room_grid[1][0], 
        room_grid[1][1], room_grid[1][2], room_grid[1][0], room_grid[1][1], room_grid[1][2])
        room_cell_row3 = "{}\n{}{}{}|\n{}{}{}|\n{}{}{}|\n{}{}{}|".format(row, room_grid[2][0], room_grid[2][1], room_grid[2][2], room_grid[2][0], room_grid[2][1], room_grid[2][2], room_grid[2][0], 
        room_grid[2][1], room_grid[2][2], room_grid[2][0], room_grid[2][1], room_grid[2][2])
        continue
    else: break
