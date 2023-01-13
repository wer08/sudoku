print("Sudoku")

# here enter a valid board, instead of mepty places enter 0
board = [
    [7,5,0,0,3,4,0,9,1],
    [0,0,0,0,7,0,0,5,6],
    [4,1,6,0,8,0,0,0,2],
    [5,6,0,3,0,0,7,0,4],
    [1,3,7,4,5,0,2,6,9],
    [0,8,4,7,9,6,0,0,0],
    [0,0,0,0,0,0,0,4,0],
    [8,0,0,0,0,0,5,2,0],
    [0,0,0,0,0,0,0,0,0]
]

def findEmpty(board):
    for row in range(9):
        for column in range(9):
            if board[row][column] == 0:
                return (row,column)
    return None

def valid(board, number, position):
    # check row
    for i in range(9):
        if board[position[0]][i] == number and position[1] != i:
            return False
    # check column
    for i in range(9):
        if board[i][position[1]] == number and position[0] != i:
            return False
    #check square
    sq = (position[0]//3,position[1]//3)

    for i in range(sq[0]*3,sq[0]*3 + 3):
        for j in range (sq[1]*3,sq[1]*3+3):
            if board[i][j] == number and (i,j) != position:
                return False
    
    return True

        

def solve(board):
    find = findEmpty(board)
    if not find:
        return True
    row,col = find

    for i in range(1,10):

        if valid(board, i, (row,col)):
            board[row][col] = i

            if solve(board):
                return True
            board[row][col] = 0

    return False
print(board)
solve(board)
print(board)


