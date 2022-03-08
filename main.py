import methods as m
import sudoku as s
import time
import sys


def main(useAC3: bool, useDegHeur: bool, sudokuPath):
    start_time = time.time()
    print("\nSudoku to solve :")
    sudoku = s.Sudoku(sudokuPath)
    print(sudoku)
    startAssignment = m.createStartAssignment(sudoku)
    print("Solving...\n")
    solvedSudoku = m.backtrackingSearch(sudoku, startAssignment, useAC3, useDegHeur)
    print("Solved sudoku :\n" + str(solvedSudoku))
    print(f"Elapsed time : {time.time() - start_time} s")


if __name__ == '__main__':
    list_arg = sys.argv
    # print(sys.argv[0])
    # main(bool(sys.argv[1]), bool(sys.argv[2]), sys.argv[3])
    # if sys.argv[3]!= None:
    # main(True, True, r"C:\Users\ferga\Downloads\grid.txt")
    # else:
    # main(True, True, None)
    main(bool(sys.argv[1]), bool(sys.argv[2]), sys.argv[3])
