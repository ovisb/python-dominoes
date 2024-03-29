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

11 Jan 2024
- Implemented the following two requirements
  - A player cannot add a domino to the end of the snake if it doesn't contain the matching number.
  - The orientation of the newly added domino ensures that the matching numbers are neighbors.

12 Jan 2024
- Implemented a scoring based algorithm for taking the decision about what piece the computer needs to move and in what location, left or right, 
and having it's decision validated before going forward with the move.

15 Jan 2024
- refactored into classes