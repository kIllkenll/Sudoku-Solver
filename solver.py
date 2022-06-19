import pyautogui as pg 
import numpy as np


def possible(grid, x, y, n):
    for i in range(0, 9):
        if grid[i][x] == n and i != y: # Checks for number (n) in X columns
            return False

    for i in range(0, 9):
        if grid[y][i] == n and i != x: # Checks for number (n) in X columns
            return False

    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for X in range(x0, x0 + 3):
        for Y in range(y0, y0 + 3):  # Checks for numbers in box(no matter the position, it finds the corner)
            if grid[Y][X] == n:
                return False    
    return True


def insertWeb(grid):
    insert(grid)

    

def insert(matrix):
    final = []
    str_fin = []
    for i in range(9):
        final.append(matrix[i])

    for lists in final:
        for num in lists:
            str_fin.append(str(num))

    counter = []

    for num in str_fin:
        pg.press(num)
        pg.hotkey('right')
        counter.append(num)
        if len(counter)%9 == 0:
            pg.hotkey('down')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find


    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            if solve(bo):
                return True
            
            bo[row][col] = 0
    #insert(bo)
    return False


def solveWeb(grid):
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(grid, x, y, n):
                        grid[y][x] = n
                        solveWeb(grid)
                        grid[y][x] = 0
                return
    insert(grid)


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo)):
            if bo[i][j] == 0:
                return (i,j)

    return None
#solve()