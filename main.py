import methods as m
import sudoku as s
import time


def main(useAC3: bool, useDegHeur: bool, sudokuPath):
    start_time = time.time()
    print("Sudoku to solve :")
    sudoku = s.Sudoku(sudokuPath)
    print(sudoku)
    startAssignment = m.createStartAssignment(sudoku)
    print("Solving...\n")
    solvedSudoku = m.backtrackingSearch(sudoku, startAssignment, useAC3, useDegHeur)
    print("Solved sudoku :\n" + str(solvedSudoku))
    print(f"\nElapsed time : {time.time() - start_time} s")


if __name__ == '__main__':
    main(True, True, r"C:\Users\ferga\Downloads\grid.txt")
