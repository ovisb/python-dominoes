import random

import pytest

from python_dominoes.domino import Domino


@pytest.fixture
def setup_domino():
    domino = Domino(1, 2)
    return domino


@pytest.fixture
def setup_two_domino():
    d1 = Domino(1, 1)
    d2 = Domino(2, 1)
    return d1, d2


def test_create_domino(setup_domino):
    assert setup_domino == Domino(1, 2)


def test_swap(setup_domino):
    setup_domino.swap()
    assert setup_domino == Domino(2, 1)


def test_eq(setup_two_domino):
    d1, d2 = setup_two_domino
    assert d1 != d2


def test_gt(setup_two_domino):
    d1, d2 = setup_two_domino
    assert d2 > d1


def test_str(setup_domino):
    assert str(setup_domino) == "[1, 2]"


def test_repr(setup_domino):
    assert repr(setup_domino) == "Domino(first_number=1, second_number=2)"
