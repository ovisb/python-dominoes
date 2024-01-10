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

Have fun!

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
