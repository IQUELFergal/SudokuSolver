# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import methods
import sudoku as sk

def main():
    print("Sudoku to solve :")
    sudoku = sk.Sudoku(r"C:\Users\ferga\Downloads\grid.txt")
    print(sudoku)
    subGrid00 = sudoku.getSubGrid(0, 0)
    print(subGrid00)
    print(sudoku.checkColumn(0, 8))
    print(sudoku.checkRow(0, 5))
    print(sudoku.checkSubGrid(0,0,4))
    emptySubGrid = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]
    sudoku.setSubGrid(1,1,emptySubGrid)
    print(sudoku)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
