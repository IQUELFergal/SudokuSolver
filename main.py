# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import methods as m
import sudoku as s
import time

def main(useAC3: bool, degH: bool):
    start_time = time.time()
    print("Sudoku to solve :")
    sudoku = s.Sudoku(r"C:\Users\ferga\Downloads\grid.txt")
    #initialAssignment = m.initAssignment(sudoku)
    print(sudoku)
    #sudoku_final = m.backtracking_search(sudoku, initialAssignment, useAC3, degH)
    print(f"\nElapsed time : {time.time() - start_time} s")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(True, True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
