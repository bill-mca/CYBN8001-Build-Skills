# This global variable is a list that describes all the
# possible winning cominations. items are list of tuples 
# of indices. Each tuple refers to a cell on the 3x3 
# tic-tac-toe game board as defined below.

_winning_combos = [
    ## Horizontal rows:
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    ## Vertical rows:
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    ## Diagonals
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
    ]

# A dictionary of names for each of the cells.
# The keys are names of cells that players can enter 
# when asked to choose a cell. The values are tuples 
# specifying the index of a cell in the game board.
# e.g. The left cell of the middle row (ML) is 
# board[1][0]
_cell_names = {
    # Top row:
    'TL' : (0, 0),
    'TM' : (0, 1),
    'TR' : (0, 2),
    # Middle row:
    'ML' : (1, 0),
    'MM' : (1, 1),
    'MR' : (1, 2),
    # Bottom Row
    'BL' : (2, 0),
    'BM' : (2, 1),
    'BR' : (2, 2)
    }

#class board():
#    def __init__(self):
#        self.values = [[" " for _ in range(3)] for _ in range(3)]
#
#    def __getitem__(self, x, y = None):
#        if isinstance(x, tuple):
#            return self.values[x[0]][x[1]]
#        elif y is None:
#            return self.values[x]
#        else:
#            return self.values[x][y]
#
#    def __str__(self):
#        out = ''
#        for row in self.values:
#            out.append(' | '.join(row))
#            out.append('\n', '-' *10)
#        return out

def _get_cell(board, x, y=None):
    """
    A workaround for easily indexing the nested list
    that is the tic-tac-toe board.
    
    The function takes a 3x3 nested list as its first argument
    The second argument can be a tuple of form (row, col).
    The second argument can also be an integer indicating the row.
    The third argument is optional and is used as the column index. 
    """
    # First check if the user is using a tuple to index 
    # the board.
    if type(x) == tuple:
        return board[x[0]][x[1]]
    # Otherwise, assume that x and y are integers
    else:
        # TODO: the below assertion will be unhelpful if the 
        # user specifies a value for x but no value for y
        assert type(x) is int and type(y) is int, 'Provided row ' 
        'and collumn indices are not integers. Please provide integers.'
        return board[x][y]
            
def _display_board(board):
    """Prints the given game board to the STDOUT."""
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

def _ttt_help():
    """Prints some information about how to play the game
    to the STDOUT"""
    _cell_names_keys = _cell_names.keys()
    print('\nPlayers take turns placing their symbol on the board '
          'If either player completes 3 in a row they win the game. '
          'The game ends in a draw if the board is filled completely. '
          '\nWhen it is your turn, indicate which cell you '
          'would like to select using two integers (row col).'
          ' for example entering 1 0 returns the first cell of the '
          'second row. Alternatively you may enter the letter code of your'
          ' chosen cell as per the below schema:') 
    print('-------------\n'
          '{0} | {1} | {2}\n'
          '-------------\n'
          '{3} | {4} | {5}\n'
          '-------------\n'
          '{6} | {7} | {8}\n'
          '-------------\n'.format(*_cell_names_keys))

def tic_tac_toe():
    """
    An interactive game of tic-tac-toe.

    This function allows two human players to compete
    at the traditional game of tic-tac-toe. Calling the
    function starts the game. Player 'X' moves first.
    The state of the game board is shown at the start of
    each turn. Players are asked to choose an empty cell.
    user input is sanitized before being entered onto the
    board. The automatically game ends when either player
    completes 3-in-a-row or all cells are filled.

    Parameters
    ----------
    The function does not take any parameters.

    Returns
    ----------
    String
        The id of the winning player. This can be either
        'X', 'O' or ' ' in case of a draw.

    """
    # The game board is a nested list of 
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    # The count variable tracks how many turns have been 
    # Played
    count = 0
    winner = None
    # The following line is just to prevent multiple redundant
    # calls of the .keys() function.
    _cell_names_keys = list(_cell_names.keys())
    
    print("Welcome to Tic Tac Toe!")
    print("Enter '?' at anytime for help")

    # All interactive gameplay occurs within this while loop.
    # The game ends after 9 turns (when all cells are filled)
    # or when a player makes a winning move.
    while count < 9:
        # The active player depends on which turn. 'X' always
        # goes first.
        player = players[count % 2]
        
        # Show the current state of the game board and prompt the 
        # current player to choose their next move.
        _display_board(board)
        move = input(f"Player {player}, enter your move: ")
        
        # If the user specified a cell using its name
        # set the cell index accordingly.
        # The use of .upper() means user input is not case 
        # sensitive.
        if move.upper() in _cell_names_keys:
            #print('Thanks, you entered ' + move)
            row, col = _cell_names[move.upper()]
        else:
            # else assume that the user entered input as a pair of 
            # integers separated by a space.
            tmp_move = move.split()
            try:
                # try to assign the cell index to test if the user
                # did enter a pair of integers.
                row, col = int(tmp_move[0]), int(tmp_move[1])
                # And try indexing to make sure the input is valid 
                board[row][col]
            except ValueError:
                # The user entered invalid input. 
                # So, show them the help information.
                print('Sorry, That input is not valid.')
                _ttt_help()
                # start this player's turn over again. 
                continue
            except IndexError:
                print('Please enter either 0, 1 or 2. Enter ? '
                      'for more help.')
                continue
                
        # The following if/else code executes the move if the chosen
        # cell is empty. Otherwise, it restarts the player's turn.
        if board[row][col] == " ":
            # For an empty entry, fill it with the player's marker.
            board[row][col] = player
            # the turn counter only increases when a cell is filled
            count += 1
            #_display_board(board)
        else:
            print("That cell is already taken. Try again!")
            # start this player's turn over again.
            continue
        
        # The following loop checks to see if the most recent move
        # was a winning move. A list of possible winning combinations
        # is checked against the current state of the game board.
        for combo in _winning_combos:
            # If all the cells referenced by this combo contain the 
            # current player's ID then they have won.
            if all([_get_cell(board, index) == player for index in combo]):
                winner = player
                #print(f'Winner: {winner}')

        # As the last step on each turn, check if the player won.
        # If the player won, end the game by breaking the game loop.
        if not winner is None:
            break

    # Finally, state the outcome of the game
    print('\n\n')
    if winner is None:
        winner = ' '
        print('Well played Player X and Player O. '
              'The game ended in a draw!')
    else:
        print(f'Congratulations Player {player}, you\'re a winner!\n')     
    _display_board(board)
    
    # TODO: write a function that allows players to play a 
    # tournament or a best-of-three by keeping score of how many
    # wins a player has had.
    return(winner)

if __name__ == "__main__":
    tic_tac_toe()