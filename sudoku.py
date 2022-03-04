import numpy as np


class Sudoku:

    def __init__(self, txt=None):
        self.Matrix = np.empty((9, 9)).astype(int)

        if txt:
            file = open('grid.txt', 'r')
            lines = file.readlines()
            file.close()

            y = 0
            for line in lines:
                x = 0
                for char in range(len(line) - 1):
                    self.set(x, y, line[char])
                    x += 1
                y += 1

        else:
            for i in range(9):
                self.set(np.random.randint(0, 3), np.random.randint(0, 9), i + 1)
                self.set(np.random.randint(3, 6), np.random.randint(0, 9), i + 1)
                self.set(np.random.randint(6, 9), np.random.randint(0, 9), i + 1)

    def __del__(self):
        print("Clear the board")

    def get(self, x, y):
        return self.Matrix[x, y]

    def set(self, x, y, value):
        self.Matrix[x, y] = value
        self.setM(x, y, value)

    def getM(self, M):
        if M == "Matrix":
            return self.Matrix
        elif M == "M1":
            return self.M1
        elif M == "M2":
            return self.M2
        elif M == "M3":
            return self.M3
        elif M == "M4":
            return self.M4
        elif M == "M5":
            return self.M5
        elif M == "M6":
            return self.M6
        elif M == "M7":
            return self.M7
        elif M == "M8":
            return self.M8
        elif M == "M9":
            return self.M9
        else:
            return False

    def identM(self, x, y):
        if 0 <= y < 3:
            if 0 <= x < 3:
                return "M1"
            elif 3 <= x < 6:
                return "M4"
            else:
                return "M7"
        elif 3 <= y < 6:
            if 0 <= x < 3:
                return "M2"
            elif 3 <= x < 6:
                return "M5"
            else:
                return "M8"
        else:
            if 0 <= x < 3:
                return "M3"
            elif 3 <= x < 6:
                return "M6"
            else:
                return "M9"

    def setM(self, x, y, value):
        if self.identM(x, y) == "M1":
            for i in self.M1:
                self.M1[x % 3, y % 3] = value
        elif self.identM(x, y) == "M2":
            for i in self.M2:
                self.M2[x % 3, y % 3] = value
        elif self.identM(x, y) == "M3":
            for i in self.M3:
                self.M3[x % 3, y % 3] = value

        elif self.identM(x, y) == "M4":
            for i in self.M4:
                self.M4[x % 3, y % 3] = value
        elif self.identM(x, y) == "M5":
            for i in self.M5:
                self.M5[x % 3, y % 3] = value
        elif self.identM(x, y) == "M6":
            for i in self.M6:
                self.M6[x % 3, y % 3] = value

        elif self.identM(x, y) == "M7":
            for i in self.M7:
                self.M7[x % 3, y % 3] = value
        elif self.identM(x, y) == "M8":
            for i in self.M8:
                self.M8[x % 3, y % 3] = value
        elif self.identM(x, y) == "M9":
            for i in self.M9:
                self.M9[x % 3, y % 3] = value

    def showGrid(self, grid, name):
        if len(grid) == 3:
            print("~~|" + name + "|~~")
            count = 0
            map = "\n"
            for i in range(len(grid)):
                map += str(grid[i, 0]) + " | " + str(grid[i, 1]) + " | " + str(grid[i, 2])
                if count > 1:
                    map += "\n"
                else:
                    map += "\n- - - - -\n"
                    count += 1
            map2 = map.replace("0", " ")
            print(map2)
        elif len(grid) == 9:
            print("~~~~|" + name + "|~~~~")
            count = 1
            map = "\n"
            for i in range(len(grid)):
                map += str(grid[i, 0]) + " " + str(grid[i, 1]) + " " + str(grid[i, 2]) + " | " \
                       + str(grid[i, 3]) + " " + str(grid[i, 4]) + " " + str(grid[i, 5]) + " | " + str(grid[i, 6]) \
                       + " " + str(grid[i, 7]) + " " + str(grid[i, 8])
                if count > 7:
                    map += "\n"
                elif (count % 3) == 0:
                    map += "\n- - - - - - - - - - -\n"
                else:
                    map += "\n"
                count += 1
            map2 = map.replace("0", " ")
            print(map2)

        else:
            print("No match found")

    def checkLine(self, x, y, value):
        mem = False
        for i in range(9):
            if self.get(i, y) == value:
                mem = True
        return mem

    def checkRow(self, x, y, value):
        mem = False
        for i in range(9):
            if self.get(x, i) == value:
                mem = True
        return mem

    def checkM(self, x, y, value):
        mem = False
        if self.identM == self.M1:
            for i in self.M1:
                for j in i:
                    if j == value:
                        mem = True
            return mem
        elif self.identM == self.M2:
            for i in self.M2:
                for j in i:
                    if j == value:
                        mem = True
            return mem
        elif self.identM == self.M3:
            for i in self.M3:
                for j in i:
                    if j == value:
                        mem = True
            return mem
        elif self.identM == self.M4:
            for i in self.M4:
                for j in i:
                    if j == value:
                        mem = True
            return mem
        elif self.identM == self.M5:
            for i in self.M5:
                for j in i:
                    if j == value:
                        mem = True
            return mem
        elif self.identM == self.M6:
            for i in self.M6:
                for j in i:
                    if j == value:
                        mem = True
            return mem
        elif self.identM == self.M7:
            for i in self.M7:
                for j in i:
                    if j == value:
                        mem = True
            return mem
        elif self.identM == self.M8:
            for i in self.M8:
                for j in i:
                    if j == value:
                        mem = True
            return mem
        elif self.identM == self.M9:
            for i in self.M9:
                for j in i:
                    if j == value:
                        mem = True

        if mem:
            return True
        else:
            return False

