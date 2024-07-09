def isSafe(board, row, col, N):
    #check in rows
    for i in range(0,row):
        if board[i][col]==1:
            return False
        
    #checking diagonals left
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1 
    #checking diagonals right
    i,j =row,col
    while i>=0 and j< N:
        if board[i][j]==1:
            return False
        i-=1
        j+=1
    
    return True
def solveQueens(board, row, N):
    if row==N:
        return True
    for col in range(0,N):
        if(isSafe(board, row, col, N)):
            board [row][col]=1 
            if solveQueens(board, row + 1, N):
                return True
            board [row][col]=0 #backtracking if no safe spots
    return False
def NQueens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    solveQueens(board,0, N)
    print(board)

if __name__== "__main__":
    NQueens(8)

