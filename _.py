# board = [0-9]
EMPTY = " "
X = "X"
O = "O"

def is_over_sym(board,x):
    for i in range(3):
        if board[i*3] == x and board [i*3+1] == x and board[i*3+2] == x:
            return 1
        elif board[i] == x and board[i+3] == x and board[i+6] == x:
            return 1
    if board[0] == x and board[4] == x and board[8] == x:
        return 1
    elif board[2] == x and board[4] == x and board[6] == x:
        return 1
    return 0

def find_winner(board):
    if is_over_sym(board,X) == 1:
        return 1
    if is_over_sym(board,O) == 1:
        return -1
    return 0

def count_empty(board):
    return sum([1 if elm == EMPTY else 0 for elm in board])

def minimax(board,maximizing):

    if find_winner(board) != 0:
        return find_winner(board)
    
    if maximizing:
        max_value = -2
        for i in range(len(board)):
            if board[i] == EMPTY:
                new_board = board.copy()
                new_board[i] = X
                new_value = minimax(new_board,False)
                if new_value > max_value:
                    max_value = new_value
        return max_value
    
    else:
        min_value = 2
        for i in range(len(board)):
            if board[i] == EMPTY:
                new_board = board.copy()
                new_board[i] = O
                new_value = minimax(new_board,True)
                if new_value < min_value:
                    min_value = new_value
        return min_value

def get_best_move(board,maximizing):
    
    if maximizing:
        max_value = -2
        best_move = None
        for i in range(len(board)):
            if board[i] == EMPTY:
                if best_move == None:
                    best_move = i
                new_board = board.copy()
                new_board[i] = X
                new_value = minimax(new_board,False)
                if new_value > max_value:
                    max_value = new_value
                    best_move = i
                print(i, new_value)
        return best_move
    
    else:
        min_value = 2
        best_move = None
        for i in range(len(board)):
            if board[i] == EMPTY:
                if best_move == None:
                    best_move = i
                new_board = board.copy()
                new_board[i] = O
                new_value = minimax(new_board,True)
                if new_value < min_value:
                    min_value = new_value
                    best_move = i
                print(i, new_value)
        return best_move
    
def print_board(board):
    for n in range(3):
        print(" | ".join(board[n*3:n*3+3]))
    print()
    
def main():
    board = [EMPTY for _ in range(9)]
    while True:
        movex = get_best_move(board,True)
        board[movex] = X
        print_board(board)

        if is_over_sym(board,X) == 1:
            return
        if count_empty(board) == 0:
            return

        moveo = int(input())
        board[moveo] = O
        print_board(board)

        if is_over_sym(board,O) == 1:
            return 
        if count_empty(board) == 0:
            return
        
main()