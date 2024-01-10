10 Jan 2024
- Generate 28 distinct domino pairs
- Out of the 28 pairs, assign 7 each to player and computer
- Remaining 14 pairs are part of the remaining stock
- Find highest double pair, e.g `[5, 5], [6, 6] ..` between player and computer
- Remove the highest double from the 'winner' and have the other player start the game

10 Jan 2024
- Added game console interface
- Added main game loop
- Added user input validations
- Added the following game logic:
- Either player is able to select dominoes and move it, to either the left or right of the snake
- Currently, game winner will be chosen if either user or computer has no more dominoes left