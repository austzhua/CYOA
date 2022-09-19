#/usr/bin/env/python3
'''
Introduction
CYOA game

Name: Austin Zhuang
Date: 1/14/21

Version 2
Version Notes: Use string formatting to create the map and create comments in main for the structure of the game
'''

#imported modules
import time

#global variables
global row, space, fill, grid, cell_row1, cell_row2, cell_row3, role
row = "+ - - - - + - - - - + - - - - +"
space = "|         "
fill = "| ||||||| "
grid = [[space, fill, fill], [fill, fill, fill], [fill, fill, fill]]
cell_row1 = "{}\n{}{}{}|\n{}{}{}|\n{}{}{}|\n{}{}{}|".format(row, grid[0][0], grid[0][1], grid[0][2], grid[0][0], grid[0][1], grid[0][2], grid[0][0], 
grid[0][1], grid[0][2], grid[0][0], grid[0][1], grid[0][2])
cell_row2 = "{}\n{}{}{}|\n{}{}{}|\n{}{}{}|\n{}{}{}|".format(row, grid[1][0], grid[1][1], grid[1][2], grid[1][0], grid[1][1], grid[1][2], grid[1][0], 
grid[1][1], grid[1][2], grid[1][0], grid[1][1], grid[1][2])
cell_row3 = "{}\n{}{}{}|\n{}{}{}|\n{}{}{}|\n{}{}{}|".format(row, grid[2][0], grid[2][1], grid[2][2], grid[2][0], grid[2][1], grid[2][2], grid[2][0], 
grid[2][1], grid[2][2], grid[2][0], grid[2][1], grid[2][2])
#functions
def init_map():
    global cell_row1, cell_row2, cell_row3
    print(cell_row1)
    print(cell_row2)
    print(cell_row3)
    print(row)

def update_map(a, b):
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

'''
Print the initial map
Give the player the option to go forwards or right
IF they go right
    Do the room 4 challenge
    Give the player the option to go forwards, backwards, or left
    IF they go backwards
        Do room 1
    ELSE IF they go forwards
        Do room 7 challenge
    ELSE
        Do room 5
ELSE
    Do the room 2 challenge
    Give the player the option to go forwards, backwards, or right
    IF they go backwards
        Do room 1
    ELSE IF they go forwards
        Do room 3 challenge
    ELSE
        Do room 5 challenge
Go through every possibility in this way
'''