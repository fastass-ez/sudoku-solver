print("█▀▀ █░░█ █▀▀▄ █▀▀█ █░█ █░░█   █▀▀ █▀▀█ █░░ ▀█░█▀ █▀▀ █▀▀█")
print("▀▀█ █░░█ █░░█ █░░█ █▀▄ █░░█   ▀▀█ █░░█ █░░ ░█▄█░ █▀▀ █▄▄▀")
print("▀▀▀ ░▀▀▀ ▀▀▀░ ▀▀▀▀ ▀░▀ ░▀▀▀   ▀▀▀ ▀▀▀▀ ▀▀▀ ░░▀░░ ▀▀▀ ▀░▀▀")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("")
print("Rules:")
print("Enter every row of a valid and unsolved 9x9 sudoku in a sequential order")
print(" with 0 representing a blank and should have spaces after every input.")
print("Example :- (Enter 1st row -  8 0 3 0 0 0 3 2 0 )")
print("")

a = input("Enter 1st row - ").split()
b = input("Enter 2nd row - ").split()
c = input("Enter 3rd row - ").split()
d = input("Enter 4th row - ").split()
e = input("Enter 5th row - ").split()
f = input("Enter 6th row - ").split()
g = input("Enter 7th row - ").split()
h = input("Enter 8th row - ").split()
i = input("Enter 9th row - ").split()

a = list(map(int, a))
b = list(map(int, b))
c = list(map(int, c))
d = list(map(int, d))
e = list(map(int, e))
f = list(map(int, f))
g = list(map(int, g))
h = list(map(int, h))
i = list(map(int, i))

puzzle = [a,b,c,d,e,f,g,h,i]
print("")
print("===============================")
print("")
#unsolved showcase
def print_board(board):
    for i in range(len(board[0])):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
        for j in range(len(board[0])):
            if j % 3 ==0 and j != 0:
                print(" | ", end = "")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end = "")
print("   |Unsolved Puzzle|")
print_board(puzzle)
print("")
print("===============================")
print("")
#finding empty spots
def find_zero(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return(i,j)
    return None            
          
#checking every block
def if_true(board, value, position):

    #checking row
    for i in range(len(board[0])):
        if board[position[0]][i] == value and position[1] != i:
            return False

    #checking column
    for i in range(len(board)):
        if board[i][position[1]] == value and position[0] !=i:
            return False

    #checking 3x3 grid
    x_box = position[1] // 3
    y_box = position[0] // 3

    for i in range(y_box*3,y_box*3 + 3):
        for j in range(x_box*3,x_box*3 + 3):
            if board[i][j] == value and (i, j) != position:
                return False
    return True

#backtracking
def solve(board):
    find = find_zero(board)
    if not find:
        return True
    else:
        row, column = find

    for i in range(1,10):
        if if_true(board, i, (row, column)):
            board[row][column] = i
            if solve(board):
                return True
            board[row][column] = 0
    return False 

solve(puzzle)
print("    |Solved Puzzle|")
print_board(puzzle)
print("===============================")
print("Enter anything to Close Window.")
ggwp = input()

