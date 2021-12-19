import random
import time
from typing import Hashable, List
from interfaces.sudoku_generator_interface import SudokuGeneratorInterface
from models.position import Position

from services.board_service import Board

from log import logger


class SudokuGenerator(SudokuGeneratorInterface):
    @staticmethod
    def generate(random_seed: Hashable = None):
        if random_seed:
            random.seed(random_seed)
        else:
            random.seed(time.time_ns())
        board = Board()
        logger.debug("Starting")
        positions: List[Position] = board.positions
        # random.shuffle(positions)

        index: int = 0
        while index < len(positions):
            position = positions[index]

            # See if there are more possibilities at current index
            logger.debug(f"{position} Remaining possibilities {position.possibilities}")
            if len(position.possibilities) == 0:
                position.reset_possibilities()
                index -= 1
                logger.debug(f"{position} No more possibilities, reset and go back")
                continue

            # Try out a random suggestion
            suggestion_index: int = random.randint(0, len(position.possibilities) - 1)
            suggestion = position.possibilities.pop(suggestion_index)
            board.insert_number(position, suggestion)
            logger.debug(f"{position} Try {suggestion}")
            if not board.validate(position):
                board.reset_number(position)
                logger.debug(f"{position} Not valid")
                continue
            index += 1

        return board.to_array()
