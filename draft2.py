#/usr/bin/env/python3
'''
Introduction
Talk about what this program is about here

Name: Austin Zhuang
Date: 1/14/21

Version 1
Version Notes: Making the map and trying to update it
'''

#imported modules


#functions
def print_cell_row():
    print("+ - - - -", end = " ")

def print_row():
    for i in range(3):
        print_cell_row()
    print('+')

def print_cell_vert(unknown):
    if unknown:
        print("| |||||||", end = " ")
    else:
        print("|        ", end = " ")

def print_vert(unknown):
    for i in range(4):
        print_cell_vert(unknown)
        
#main
# for i in range(3):
#     print_row()
#     for j in range(4):
#         print_vert(True)
#         print('|')
# print_row()
