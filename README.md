# Sudoku Generator

Just a small hobby project.

## Usage

```py
from sudokugenerator import SudokuGenerator

SudokuGenerator.generate()  # Create a random solved sudoku board as a np.array
SudokuGenerator.generate("foo")  # Use a hashable seed for reproducible boards
```

## Ideas

- Remove numbers to create solvable sudoku that is not already filled in
- Measure of board difficulty
- Performance tuning using threading
- Publish to PyPi
