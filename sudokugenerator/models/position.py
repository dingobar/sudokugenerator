from typing import List, Tuple
from pydantic import BaseModel
import numpy as np


class Position(BaseModel):
    x: int
    y: int
    section: Tuple[int, int]
    possibilities: List[int] = list(np.array(range(9)) + 1)

    def as_tuple(self) -> Tuple[int, int]:
        return (self.x, self.y)

    def reset_possibilities(self) -> None:
        self.possibilities = list(np.array(range(9)) + 1)

    def __str__(self) -> str:
        return f"[X: {self.x}, Y: {self.y}, section {self.section}]"
