# Three mutually Independet lists
board = [['_'] * 3 for i in range(3)] 
board[1][2] = 'X'
board[1][1] = '0'
board[0][2] = 'X'
board[0][0] = '0'
board[2][1] = 'X'
print(board)