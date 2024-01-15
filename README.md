# EDU project

## Project

This is _Dominoes_ project that is part of Hyperskill platform from Jetbrains Academy.

'Python Core' track

## Technologies and tools used

- Python 3.12
- pytest
- mypy
- isort
- black
- flake8
- make

## Project description

This is a console _Dominoes_ game, played between player and computer.

You have to try to beat the computer using the following rules:
- if you manage to place all your domino pieces on the snake before the computer, you won.
- if the computer does the same before you, you lost.
- if both still have pieces and the stock empty, it's a draw. 

Game rules for placing domino piece:
- When the game starts you will see all your pieces and some number before each.
- If you input a negative number, it will try to place that piece to the left of the snake
- If you input a positive number, it will try to place that piece to the right of the snake
- If you go out of range, or input a string/text etc, you will get an Invalid error message prompting you to retry.
- Also when placing a piece either in left or right, you have to take into consideration the following:
  - The move will be valid if the snake piece and your piece are neighbours
  - For example if you have a hand like this
  ```
    Your pieces: 
    1:[0, 2]
    2:[1, 5]
    3:[0, 6]
    4:[1, 3]
    5:[2, 3]
    6:[0, 5]
    7:[4, 6]
    ```
  
    With the snake piece ``[2, 5]``
    - If i would like to move ``[0,2]`` to the right of the snake, the move would not go through. as there is no number ``5`` in ``[0, 2]`` piece.
    - However, adding piece ``[1, 5]`` would be fine.
    - Note: there will be a change to the above piece before being added to the snake, because it is not yet a matching neighbour, it's numbers will be swapped before piece will be placed on the snake.
    - e.g after placement snake will look like ``[2,5] [5, 1]``
    

Have fun!

#### Sample game example
Note : ```<``` is used for command line input
```
Stock size: 14
Computer pieces: 6

[1, 1] 

Your pieces: 
1:[0, 2]
2:[1, 5]
3:[0, 6]
4:[1, 3]
5:[2, 3]
6:[0, 5]
7:[4, 6]

Status: It's your turn to make a move. Enter your command.
< 1
Illegal move. Please try again.
< 2
======================================================================
Stock size: 14
Computer pieces: 6

[1, 1] [1, 5] 

Your pieces: 
1:[0, 2]
2:[0, 6]
3:[1, 3]
4:[2, 3]
5:[0, 5]
6:[4, 6]

Status: Computer is about to make a move. Press Enter to continue...
<
======================================================================
Stock size: 14
Computer pieces: 5

[4, 1] [1, 1] [1, 5] 

Your pieces: 
1:[0, 2]
2:[0, 6]
3:[1, 3]
4:[2, 3]
5:[0, 5]
6:[4, 6]

Status: It's your turn to make a move. Enter your command.
< -6
======================================================================
Stock size: 14
Computer pieces: 5

[6, 4] [4, 1] [1, 1] [1, 5] 

Your pieces: 
1:[0, 2]
2:[0, 6]
3:[1, 3]
4:[2, 3]
5:[0, 5]

Status: Computer is about to make a move. Press Enter to continue...
<
======================================================================
Stock size: 14
Computer pieces: 4

[3, 6] [6, 4] [4, 1] [1, 1] [1, 5] 

Your pieces: 
1:[0, 2]
2:[0, 6]
3:[1, 3]
4:[2, 3]
5:[0, 5]

Status: It's your turn to make a move. Enter your command.
<
```

#### Poetry project install steps

Install everything (main + dev packages except optional groups)

```sh
peotry install
```

Install main packages only

```sh
peotry install --only main

```

If you need pre-commit

```sh
poetry install --with commit
```

If you decided to install pre-commit you can install .pre-commit files in your repo

```sh
peotry run pre-commit install -t pre-commit
poetry run pre-commit install -t pre-push
```

If the files are git staged, you can trigger pre-commit manually

```sh
poetry run pre-commit run --all-files
poetry run pre-commit run --hook-stage push -v
```

#### Makefile

Added 'Makefile' to make it easy to validate files
Check bellow command on usage

```sh
make help
```
