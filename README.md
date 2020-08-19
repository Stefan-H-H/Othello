# Othello

## Software Requirements:
In order to run and play the Othello game, you must download the latest version of Processing which can be found here:
https://processing.org/download/

Please also note an add-on installation called "Python Mode" is necessary to enable a Python version of Processing used to run the game. Please follow the following instructions: https://py.processing.org/tutorials/gettingstarted/

## How to Play:
To play the game, you will need to download the Othello directory, then open the othello_game_controller.pyde file once you have installed Processing and performed the required configuration mentioned above.

Official Othello Game Rules may be referenced here: https://www.ultraboardgames.com/othello/game-rules.php


## Game Play Screenshots:

### Game Start:
![Game Start] (/Images/Othello_Game_Start_Player_Turn.png)

*Note*: All possible valid moves will be outlined on the game board for a player. A live scoreboard is also provided.

### Computer Turn:
![Computer turn](/Images/Othello_Computer_Turn.png)

*Note*: There will be a slight delay (2 seconds) before the AI places a piece on the board to simulate the AI "thinking".

### Game Over:
![Game Over](/Images/Othello_Game_Over)

### Game Over - Record Score
![Game Over](/Images/Othello_Record_Score)

*Note*: The current implementation will wait 2 seconds after the game is over to prompt the player to write their name, so that the gameplay score can be retained in a filed named `scores.txt`.
