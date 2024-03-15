# Assignment 1

[Read me on GitHub for neater formatting](https://github.com/bill-mca/CYBN8001-Build-Skills/blob/main/task-1/Assignment1.md)

## Task 1: Create an Artwork

I chose to draw the Koch snowflake fractal as pictured below.

![KochSnowflake.png](https://github.com/bill-mca/CYBN8001-Build-Skills/blob/main/task-1/koch_snowflake.png?raw=true)

The idea for the snowflake came to me soon after the assignment was set. I really wanted to draw a fractal as it is a good way to demonstrate the power of programming. Because of the elaborate detail and precision of the completed snowflake it would not be possible for most people to draw without machine assistance. 
My algorithm for the snowflake employed functional recursion. Because of my training as a biologist I am intrigued by functional recursion where functions reproduce themselves with slight modifications. In the case of this snowflake image there were 6 generations of recursive algorithms. The recursive function spawned 4095 child processes. Each of the child processes generated was specialised on drawing a small pat of the whole artwork. 

## Task 2: Play a Game

### Coder's Journey

idea -> strategy

strategy -> algorithm

algorithm -> pseudocode

### Code
The code for my tic-tac-toe game is attatched to this submission and [available on GitHub](https://github.com/bill-mca/CYBN8001-Build-Skills/blob/main/task-1/tic-tac-toe.py).

### AI tic-tac-toe player
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

### Lessons Learnt
 - The coder's journey framework doesn't feel natural to me. For the tasks set in this assignment, I had an intition of how to complete the task immediately. From this intuition I always have a strong urge to check whether my hunch is correct. I didn't sit down and ponder how best to structure the code, i had a sense of what it should look like and an urge to test if my hunch was right.
 -  My experience from past programming means that I can say with a far degree of confidence that a certain approach to solving the problem will be achievable. I'm grateful for the fundamental grounding that my undergraduate education gave me.
 -  I realise that my career since leaving university has taught me that programming is a useless skill but that, in this environment, it should be valued.
 - Having said all this, I need to get more strategic in my approach to coding. For the maker project that I have in mind, I'll need to carefully plan out where the most technically difficult parts are and, especially, identify which challenging parts are path dependancies for the wider project. 
 - I get transfixed at times when coding. It is important to have a routine established where I can break out of the trance and look at the bigger picture. This will be especially important for the build journey assignment which requires me to constantly reflect on the process and my progress towards the goal.
 - Like everyone else in the course, I struggled with indentation issues! I think now that I have a consistent workflow with one dedicated IDE I should be ok.

## Acknowledgements
 - Thanks to Tiarnee and Anthony for the discussions about optimal tic-tac-toe algorithms. It was really fun working through that with you guys.
 - Thanks to Muhammed Asfour for taking such a principled approach to the axi-draw. Your bold effort to  figure out the calibration and scaling taught me a lot about how it works and showed me a way to get around its limitations.
 - Thanks to Amanda whose enthusiasm for coding meant that she was around to offer encouragement and advice almost everytime I went to work on the axi-draw!