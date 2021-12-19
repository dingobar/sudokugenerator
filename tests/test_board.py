from typing import Callable, Tuple
import pytest
import numpy as np
from models.position import Position

from services.board_service import Board


@pytest.fixture
def sut():
    return Board()


@pytest.mark.parametrize(
    "section",
    [(x, y) for x in range(9) for y in range(9)],
)
def test_board_initialized(sut: Board, section: Tuple[int, int]):
    func: Callable[[Position]] = lambda var: var.x == section[0] and var.y == section[1]
    position = next(filter(func, sut.positions), None)

    expected = (np.floor(position.x / 3.0), np.floor(position.y / 3.0))

    assert position.section == expected


def test_validate_same_number_in_section_then_fail(sut: Board):
    positions = sut.positions
    sut.insert_number(positions[0], 1)
    assert sut.validate(positions[0])
    sut.insert_number(positions[10], 1)
    assert not sut.validate(positions[10])


def test_validate_same_number_in_cross_then_fail(sut: Board):
    positions = sut.positions
    sut.insert_number(positions[0], 1)
    assert sut.validate(positions[0])
    sut.insert_number(positions[9], 1)
    assert not sut.validate(positions[9])
