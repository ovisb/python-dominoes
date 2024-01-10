import random

import pytest

from python_dominoes.dominoes import (
    generate_dominoes,
    shuffle_dominoes,
    split_dominoes,
    find_highest_domino,
)


@pytest.fixture
def dominoes():
    random.seed(0)
    dom = generate_dominoes()
    random.shuffle(dom)
    return dom


def test_generate_dominoes():
    assert len(generate_dominoes()) == 28


def test_random(dominoes):
    random.seed(0)
    dom = generate_dominoes()
    shuffle_dominoes(dom)
    assert dom == dominoes


def test_split_dominoes(dominoes):
    expected = [
        [0, 3],
        [2, 3],
        [1, 4],
        [2, 6],
        [0, 5],
        [0, 0],
        [1, 1],
    ]
    assert split_dominoes(dominoes, 0, 7) == expected


def test_find_highest_domino(dominoes):
    player = dominoes[:7]
    assert find_highest_domino(player) == [1, 1]
