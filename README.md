TicTacToe Game with AI Opponent
A simple implementation of the classic TicTacToe game where you play against an AI.

Description
This game is a classic 3x3 TicTacToe where you, as the player, are up against an AI opponent. The board is represented by a grid of numbers from 0 to 8, and the player picks a number to place their move. The AI opponent then calculates its move based on the current state of the board.

Features
Simple command-line interface.
AI opponent that calculates its move based on the state of the board.
Game ends when there's a winner or the board is full.
Requirements
Python 3.x
pandas
numpy
You can install the required libraries using pip:

Copy code
pip install pandas numpy
How to Play
Run the script in your terminal or command prompt.
The board will be displayed, and the AI will make the first move.
You will then be prompted to pick a number between 0-8 to place your 'X'.
The game continues until there's a winner or the board is full.
Limitations
The current AI implementation is based on predefined winning board states and doesn't necessarily pick the optimal move.

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License
MIT

