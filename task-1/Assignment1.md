# Assignment 1

[Read me on GitHub instead!!](https://github.com)

## Artwork

I chose to draw the Koch snowflake fractal as pictured below.

[KochSnowflake.png](


## AI tic-tac-toe player
The following is a strategy to modify my [tic-tac-toe.py](https://github.com/bill-mca/CYBN8001-Build-Skills/blob/main/task-1/tic-tac-toe.py) code.
Editing the my tic-tac-toe.py code to introduce an AI player I would start by adding a prompt at the start of the game that allows the players to specify whether 'X', 'O', both or neither should be controlled by AI. This would be saved to a list `ai_players`

The following line in the tic-tac-toe function would need to be changed to intorduce AI:
`move = input(f"Player {player}, enter your move: ")` 
This line would be replaced with an if statement that checks whether the current player is controlled by ai (`if player in ai_players:`).

If the player is controlled by ai, I would call a function that decides on the optimal move for the player based on the state of the board. 

Below is pseudocode for a function that decides on the optimal move for an AI player based on the state of the board. My ai player is rational, is trying to win the game and prefers drawing to losing.

```
Function _ai_move(player, board)
    # First, try to win with this move:
    for combo in winning_combos:
        if player occupies two cells in combo AND opponent occupies zero cells in combo:
            return index of the empty cell

    # second, block the opponent from winning if necessary:
    for combo in winning_combos:
        if opponent occupies two cells in combo AND player occupies zero cells in combo:
            return index of the empty cell

    # Finally, if neither player can win this turn the optimal move is one that
    # maximises your oportunities to win in following turns:
    cell_scores = empty 3*3 nested list
    for row in cell_scores:
        for cell in row:
            if the cell is alredy occupied:
                cell_scores[row][cell] = -1
                continue to the next iteration of the for loop 
            cell_winning_combos = subset of winning_combos that includes cell
            for combo in cell_winning_combos:
                if none of the cells of combo have the opponent's symbol:
                    increase cell_scores[row, cell] by 1
    # Often there will be 2 or 3 cells with the same high score.
    # In that case the ai can just randomly pick one as they are all
    # equally good moves.
    return the index of any of the highest values in cell_scores
```

Some work would also need to be done to efficiently tie this in with the code that follows as my code currently has several steps of user input sanitisation. This would be unnecessary and possibly throw errors or create infinite loops. This sanitisation code might help to debug the `_ai_move` function.

Finally, I would need to test the code by playing against the AI to make sure that the code doesn't break and that the AI always makes allowable and rational moves regardless of what moves the human player is making. I would also test that hen two ai players face each other the game always ends in a draw.

