# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import methods
import sudoku as sk


def init() -> int:
    sudoku = sk.Sudoku()

    matrix = sk.Sudoku(None)
    matrix.showGrid(matrix.getM("Matrix"), "Grille")
    matrix.showGrid(matrix.getM("M1"), "M1")
    matrix.showGrid(matrix.getM("M2"), "M2")
    matrix.showGrid(matrix.getM("M4"), "M4")
    matrix.showGrid(matrix.getM("M3"), "M3")
    matrix.showGrid(matrix.getM("M9"), "M9")
    return 0


def main():
    print("test")
    init()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
