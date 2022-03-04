import numpy as np


class Sudoku:

    def __init__(self, path_to_file: str = None):
        self.grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.domain = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        if path_to_file:
            self.loadFile(path_to_file)
        else:
            print("TODO : Build a random sudoku")

    def loadFile(self, path_to_file: str):
        file = open(path_to_file, 'r')
        lines = file.readlines()
        file.close()
        for x in range(0, len(lines)):
            for y in range(0, len(lines[x])):
                if lines[x][y] != "\n":
                    self.grid[x][y] = int(lines[x][y])

    def __str__(self):
        result = ""
        for x in range(len(self.grid)):
            line = ""
            for y in range(len(self.grid[x])):
                line += str(self.grid[x][y])
                if y in [2, 5]:
                    line += "|"
            result += (line + "\n")
            if x in [2, 5]:
                result += ("---+---+---" + "\n")
        return result

    def get(self, x: int, y: int) -> int:
        return self.grid[x][y]

    def set(self, x: int, y: int, value: int):
        self.grid[x][y] = value

    def getSubGrid(self, m: int, n: int) -> list[list[int]]:
        subGrid = [[0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]]
        for x in range(0, len(subGrid)):
            for y in range(0, len(subGrid[x])):
                subGrid[x][y] = self.grid[3 * m + x][3 * n + y]
        return subGrid

    def setSubGrid(self, m: int, n: int, subGrid: list[list[int]]):
        for x in range(0, len(subGrid)):
            for y in range(0, len(subGrid[x])):
                self.grid[3 * m + x][3 * n + y] = subGrid[x][y]

    def checkColumn(self, columnIndex: int, value: int) -> bool:
        mem = False
        for i in range(len(self.grid[0])):
            if self.grid[i][columnIndex] == value:
                mem = True
        return mem

    def checkRow(self, rowIndex: int, value: int) -> bool:
        mem = False
        for i in range(len(self.grid)):
            if self.grid[rowIndex][i] == value:
                mem = True
        return mem

    def checkSubGrid(self, m: int, n: int, value: int) -> bool:
        mem = False
        subGrid = self.getSubGrid(m, n)
        for x in range(0, len(subGrid)):
            for y in range(0, len(subGrid[x])):
                if self.grid[x][y] == value:
                    mem = True
        return mem
