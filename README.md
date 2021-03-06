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
<img src="/Images/Othello_Game_Start_Player_Turn.png" height="400">

*Note*: All possible valid moves will be outlined on the game board for a player. A live scoreboard is also provided.

### Computer Turn:
<img src="/Images/Othello_Computer_Turn.png" height="400">

*Note*: There will be a slight delay (2 seconds) before the AI places a piece on the board to simulate the AI "thinking".

### Game Over:
<img src="/Images/Othello_Game_Over.png" height="400">

### Game Over - Record Score
<img src="/Images/Othello_Record_Score.png" height="400">

*Note*: The current implementation will wait 2 seconds after the game is over to prompt the player to write their name, so that the gameplay score can be retained in a filed named `scores.txt`.
