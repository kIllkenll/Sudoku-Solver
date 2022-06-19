from tkinter import*
from solver import solve, insert,solveWeb,insertWeb
import time
root = Tk()
errLabel = Label(root, text="", fg="red")
errLabel.grid(row=15, column=1, columnspan=10, pady=5)
solvedLabel = Label(root, text="", fg="green")
solvedLabel.grid(row=15, column=1, columnspan=10, pady=5)
board = []

def main():
    root.geometry("424x550")
    root.configure(background="white")
    root.title("Sudoku Solver")

    draw9x9Grid()
    root.mainloop()

def validateNum(P):
    out = (P.isdigit() or P =="") and len(P) < 2
    return out

reg = root.register(validateNum)
cells = {}
def draw3x3Grid(row, column, bgcolor):
    for i in range(3):
        for j in range(3):
            e = Entry(root, width=5, bg=bgcolor, justify="center",validate="key",validatecommand=(reg, "%P") )
            e.grid(row=row+i+1, column=column+j+1, sticky='nsew',padx=1,pady=1,ipady=5)
            cells[(row+i+1, column+j+1)] = e


finishedWeb = False
def draw9x9Grid():
    color = "#D0ffff"
    for rowNo in range(1,10,3):
        for colNo in range(0,9,3):
            draw3x3Grid(rowNo, colNo, color)
            if color == "#D0ffff":
                color = "#ffffd0"
            else:
                color = "#D0ffff"

def clearValues():
    errLabel.configure(text="")
    solvedLabel.configure(text="")
    for row in range(2,11):
        for col in range(1,10):
            cell = cells[(row, col)]
            cell.delete(0,"end")
def startSolve():
    if finishedWeb == True:
       solvedLabel.configure("Solved")
       for row in range(2,11):
            for col in range(1,10):
                cells[(row, col)].delete(0,"end")
                cells[(row, col)].insert(0, board[row-2][col-1])   
            
    else:
        getValues()
        updateValues(board)
    
def getValues():
    errLabel.configure(text="")
    solvedLabel.configure(text="")
    for row in range(2,11):
        rows = []
        for col in range(1,10):
            val = cells[(row, col)].get()
            if val == "":
                rows.append(0)
            else:
                rows.append(int(val))
        board.append(rows)

def justUpdate():
    for row in range(2,11):
            for col in range(1,10):
                cells[(row, col)].delete(0,"end")
                cells[(row, col)].insert(0, board[row-2][col-1])

def solveOnWeb():
    #print9(6b5oard)
    #startSolve()
    finishedWeb = True
    getValues()
    solve(board)
    time.sleep(2)
    insertWeb(board)
    time.sleep(3)
    justUpdate()
    
    # solveWeb(board)


btn = Button(root, command=startSolve, text="Solve", width = 10)
btn.grid(row = 20, column=1, columnspan=5,pady=20)

btn = Button(root, command=solveOnWeb, text="Web Solver", width = 10)
btn.grid(row = 20, column=3, columnspan=5,pady=20)

btn = Button(root, command=clearValues, text="Clear", width = 10)
btn.grid(row = 20, column=5, columnspan=5,pady=20)



def updateValues(board):
        sol = solve(board)
        if sol == True:
            for row in range(2,11):
                for col in range(1,10):
                    cells[(row, col)].delete(0,"end")
                    cells[(row, col)].insert(0, board[row-2][col-1])
            solvedLabel.configure("Solved")
            
        else:
            errLabel.configure(text="No solution exist")
if __name__ == '__main__':
    main()