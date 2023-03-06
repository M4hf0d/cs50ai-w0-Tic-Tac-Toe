EMPTY = None


K = [["X", "C", "X"],
     ["A", "O", "M"],
     ["X", "Z", EMPTY]]
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (EMPTY in board[0] or board[1] or board[2]) and not winner(board) :
        return False
    else :
       return True
    
def winner(board):
     v = 0
     for v in range(3):
          if all(i ==board[v][0] for i in  board[v]) : #checking lines
               return board[v][0]
          if all([board[0][v],board[1][v],board[2][v]]):#checking columns
               return board[0][v]
     if (all([board[0][0],board[1][1],board[2][2]])) or (all([board[0][2],board[1][1],board[2][0]])): #chcking diagonals
      return board[1][1]
     else: 
         return None


print(terminal(K))