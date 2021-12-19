import timeit


code_to_run = """\
from services.sudoku_generator_service import SudokuGenerator
SudokuGenerator.generate()
    """


if __name__ == "__main__":
    n = 1000
    result = timeit.timeit(stmt=code_to_run, number=n)
    print(f"Generated {n} sudokus, avg. time was {result/n}")
