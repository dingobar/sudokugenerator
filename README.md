# Sudoku Generator

Just a small hobby project that generates a solved sudoku board.

The only dependency is `numpy`.

## Usage

```py
from sudokugenerator import SudokuGenerator

SudokuGenerator.generate()  # Create a random solved sudoku board as a np.array
SudokuGenerator.generate("foo")  # Use a hashable seed for reproducible boards
```

## Run tests

Run this is a python 3.x venv.

```
pip install -r requirements.txt
python3 -m pytest tests
```

## Ideas

- Remove numbers to create solvable sudoku that is not already filled in
- Measure of board difficulty
- Performance tuning using threading
- Publish to PyPi
