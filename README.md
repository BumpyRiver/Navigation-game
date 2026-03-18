Navigation Game

A command-line grid-based navigation game where the player must locate a key and reach the exit.


Gameplay

The game is played on a 10×10 grid with alphanumeric coordinates (e.g. A1, B2).

Each turn begins by rolling a dice (Enter to roll, Q to quit).

After rolling, the player moves using:

  W, A, S, D for movement
  
  B to go back to the original position
  
  Q to quit

Once all moves are used, the player must confirm their position (Enter) or go back (B).


Objectives

Find the key

Reach the exit (E) to win

The game displays the number of turns taken upon completion


Special Spaces

B (Boost): One-time use; adds +6 to the next dice roll

X (X-ray): One-time use; reveals the coordinates of the key


Additional Features

Movement preview system before confirmation

Input validation (invalid and out-of-bounds moves do not consume turns)

Replay option after completing the game


Customization

Board size can be modified by changing the row and column values in the code
