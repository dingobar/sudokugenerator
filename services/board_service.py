from typing import List, Tuple
import numpy as np
from numpy.typing import ArrayLike

from interfaces.board_interface import BoardInterface

from models.position import Position


EMPTY = 0
BOARDSIZE = 9


class Board(BoardInterface):
    def __init__(self) -> None:
        _initial_board = np.zeros((BOARDSIZE, BOARDSIZE), dtype="int")
        self._board = _initial_board
        _positions = []
        for i in range(BOARDSIZE):
            for j in range(BOARDSIZE):
                _positions.append(
                    Position(x=i, y=j, section=self.__section_id_from_coordinates((i, j)))
                )
        self._positions = _positions

    def __section_id_from_coordinates(self, coordinates: Tuple[int, int]) -> int:
        return (np.floor(coordinates[0] / 3.0), np.floor(coordinates[1] / 3.0))

    @property
    def positions(self) -> List[Position]:
        return self._positions

    def insert_number(self, position: Position, value: int) -> None:
        self._board[position.as_tuple()] = value

    def reset_number(self, position: Position) -> None:
        self._board[position.as_tuple()] = EMPTY

    def validate(self, position: Position) -> bool:
        return self.__section_is_valid(position) and self.__cross_is_valid(position)

    def __get_section_array(self, section: Tuple[int, int]) -> ArrayLike:
        section_array = self._board[
            section[0] * 3 : section[0] + 3, section[1] * 3 : section[1] + 3
        ]
        return section_array

    def _get_cross_arrays(self, position: Position) -> Tuple[ArrayLike, ArrayLike]:
        cross_array_row = self._board[:, position.y]
        cross_array_column = self._board[position.x, :]
        return (cross_array_row, cross_array_column)

    def __cross_is_valid(self, position: Position):
        row, column = self._get_cross_arrays(position)
        row_violations = any(np.bincount([int(n) for n in row if n != 0]) > 1)
        column_violations = any(np.bincount([int(n) for n in column if n != 0]) > 1)
        return not (row_violations or column_violations)

    def __section_is_valid(self, position) -> bool:
        section: ArrayLike = self.__get_section_array(position.section)
        problems = np.bincount([int(n) for n in section.flatten() if n != 0]) > 1
        if len(problems) > 0:
            return not any(problems)
        return True  # All values were empty

    def to_array(self) -> ArrayLike:
        return self._board

    def __str__(self) -> str:
        return str(self._board)
