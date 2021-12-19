import pytest
from models.position import Position


@pytest.fixture
def sut():
    return Position(x=1, y=1, section=(0, 0))


def test_reset_possibilities(sut: Position):
    sut.possibilities.pop(0)
    assert sut.possibilities == [2, 3, 4, 5, 6, 7, 8, 9]


def test_as_tuple(sut: Position):
    result = sut.as_tuple()
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert result == (1, 1)
