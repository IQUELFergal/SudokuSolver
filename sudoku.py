import os
import random


class Sudoku:

    # Constructeur de sudoku
    def __init__(self, filePath: str = None):
        self.grid = [[0 for x in range(9)] for y in range(9)]
        self.domains = [[[1, 2, 3, 4, 5, 6, 7, 8, 9] for x in range(9)] for y in range(9)]
        if filePath == "random":
            self.createRandomSudokuGrid()
        elif os.path.exists(filePath):
            self.loadFile(filePath)
        else:
            try:
                raise Exception("Error: No such file or directory :", filePath)
            finally:
                print("Error: No such file or directory :", filePath)

    # Initialise le sudoku grace au fichier dont l'adresse est fournie
    def loadFile(self, filePath: str) -> None:
        file = open(filePath, 'r')
        lines = file.readlines()
        file.close()
        for x in range(0, len(lines)):
            for y in range(0, len(lines[x])):
                if lines[x][y] != "\n":
                    self.assign(int(lines[y][x]), x, y)

    def createRandomSudokuGrid(self):
        print("Generating random sudoku grid")
        solvedGrids = [[[7, 9, 6, 2, 4, 5, 3, 1, 8],
                        [1, 5, 4, 7, 3, 8, 9, 2, 6],
                        [8, 2, 3, 6, 1, 9, 7, 4, 5],
                        [9, 6, 7, 1, 8, 4, 5, 3, 2],
                        [2, 3, 1, 9, 5, 7, 6, 8, 4],
                        [5, 4, 8, 3, 2, 6, 1, 9, 7],
                        [4, 8, 9, 5, 7, 3, 2, 6, 1],
                        [6, 1, 5, 8, 9, 2, 4, 7, 3],
                        [3, 7, 2, 4, 6, 1, 8, 5, 9]],

                       [[4, 8, 3, 9, 2, 1, 6, 5, 7],
                        [9, 6, 7, 3, 4, 5, 8, 2, 1],
                        [2, 5, 1, 8, 7, 6, 4, 9, 3],
                        [5, 4, 8, 1, 3, 2, 9, 7, 6],
                        [7, 2, 9, 5, 6, 4, 1, 3, 8],
                        [1, 3, 6, 7, 9, 8, 2, 4, 5],
                        [3, 7, 2, 6, 8, 9, 5, 1, 4],
                        [8, 1, 4, 2, 5, 3, 7, 6, 9],
                        [6, 9, 5, 4, 1, 7, 3, 8, 2]],

                       [[8, 4, 7, 9, 1, 5, 3, 2, 6],
                        [1, 9, 6, 8, 2, 3, 4, 7, 5],
                        [5, 2, 3, 4, 6, 7, 9, 1, 8],
                        [7, 1, 4, 6, 5, 9, 2, 8, 3],
                        [9, 8, 5, 3, 7, 2, 1, 6, 4],
                        [6, 3, 2, 1, 8, 4, 7, 5, 9],
                        [4, 7, 8, 2, 9, 6, 5, 3, 1],
                        [2, 6, 9, 5, 3, 1, 8, 4, 7],
                        [3, 5, 1, 7, 4, 8, 6, 9, 2]],

                       [[2, 7, 1, 6, 4, 9, 3, 8, 5],
                        [5, 3, 9, 8, 2, 1, 6, 4, 7],
                        [4, 6, 8, 5, 3, 7, 1, 2, 9],
                        [1, 5, 3, 4, 7, 8, 9, 6, 2],
                        [7, 8, 6, 2, 9, 3, 4, 5, 1],
                        [9, 4, 2, 1, 6, 5, 7, 3, 8],
                        [3, 1, 5, 9, 8, 6, 2, 7, 4],
                        [8, 2, 7, 3, 1, 4, 5, 9, 6],
                        [6, 9, 4, 7, 5, 2, 8, 1, 3]]]

        randomGrid = solvedGrids[random.randint(0, len(solvedGrids) - 1)]

        # On inverse des lignes de 3*9 cases
        shuffleCountHorizontally = random.randint(5, 20)
        for i in range(shuffleCountHorizontally):
            firstRowIndexToShuffle = random.randint(0, 2)
            secondRowIndexToShuffle = random.randint(0, 2)
            if firstRowIndexToShuffle != secondRowIndexToShuffle:
                # On sauvegarde la 2nd ligne
                secondRow = [[0 for x in range(9)] for y in range(3)]
                for y in range(3):
                    for x in range(9):
                        secondRow[y][x] = randomGrid[secondRowIndexToShuffle * 3 + y][x]
                # On copie la 1ere line sur la 2nd ligne
                for y in range(3):
                    for x in range(9):
                        randomGrid[secondRowIndexToShuffle * 3 + y][x] = randomGrid[firstRowIndexToShuffle * 3 + y][x]
                # On copie la sauvegarde de la 2nd ligne sur la 1ere ligne
                for y in range(3):
                    for x in range(9):
                        randomGrid[firstRowIndexToShuffle * 3 + y][x] = secondRow[y][x]

        shuffleCountVertically = random.randint(5, 20)
        for i in range(shuffleCountVertically):
            firstColumnIndexToShuffle = random.randint(0, 2)
            secondColumnIndexToShuffle = random.randint(0, 2)
            if firstColumnIndexToShuffle != secondColumnIndexToShuffle:
                secondColumn = [[0 for x in range(3)] for y in range(9)]
                # On sauvegarde la 2nd row
                secondRow = [[0 for x in range(3)] for y in range(9)]
                for y in range(3):
                    for x in range(9):
                        secondRow[x][y] = randomGrid[x][secondColumnIndexToShuffle * 3 + y]
                # On copie le 1er row sur le 2nd row
                for y in range(3):
                    for x in range(9):
                        randomGrid[x][secondColumnIndexToShuffle * 3 + y] = randomGrid[x][
                            firstColumnIndexToShuffle * 3 + y]
                # On copie la sauvegarde du 2nd row sur le 1er row
                for y in range(3):
                    for x in range(9):
                        randomGrid[x][firstColumnIndexToShuffle * 3 + y] = secondRow[x][y]

        # On enleve des valeurs aleatoirement
        removeCount = random.randint(20, 40)
        removedPosList =[]
        while len(removedPosList) < removeCount:
            x, y = random.randint(0, 8), random.randint(0, 8)
            if (x, y) not in removedPosList:
                removedPosList.append((x, y))
                randomGrid[x][y] = 0

        # On transpose la matrice si flip est vrai
        flip = bool(random.randint(0, 1))
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                if flip:
                    self.assign(randomGrid[x][y], x, y)
                else:
                    self.assign(randomGrid[y][x], x, y)

    # Transforme le sudoku est string pour l'afficher
    def __str__(self):
        result = ""
        for x in range(len(self.grid)):
            line = ""
            for y in range(len(self.grid[x])):
                line += str(self.grid[y][x])
                line += " "
                if y in [2, 5]:
                    line += "| "
            result += (line + "\n")
            if x in [2, 5]:
                result += ("------+-------+------" + "\n")
        return result

    # Renvoie la valeur de la variable à la position donnée
    def getValue(self, x: int, y: int) -> int:
        return self.grid[x][y]

    # Renvoie le domaine de la variable à la position donnée
    def getDomain(self, x: int, y: int) -> list[int]:
        return self.domains[x][y]

    # Permet d'assigner une variable
    def assign(self, value, x: int, y: int) -> None:
        self.grid[x][y] = value
        if value != 0:
            self.domains[x][y] = []

    # Permet de reinitialiser une variable
    def unassign(self, domain, x: int, y: int) -> None:
        self.grid[x][y] = 0
        self.domains[x][y] = domain

    # Supprime la valeur Value du domaine de la variable en position x, y
    def removeFromDomain(self, value: int, x: int, y: int):
        self.domains[x][y].remove(value)

    # Renvoie la position de la sous-grille contenant la position donnée
    def getSubGridPosAt(self, x: int, y: int) -> tuple[int, int]:
        m = n = i = j = 0
        for i in range(3):
            if x < 3 * (i + 1):
                m = i
                break

        for j in range(3):
            if y < 3 * (j + 1):
                n = j
                break

        return (m, n)

    # Renvoie la liste de toutes les positions non assignées associées à la position donnée
    def getUnassignedNeighborPos(self, x: int, y: int) -> list[tuple[int, int]]:
        neighborPosList = self.getNeighborPos(x, y)
        unassignedNeighborPos = []

        for pos in neighborPosList:
            if self.getValue(pos[0], pos[1]) == 0:
                unassignedNeighborPos.append((pos[0], pos[1]))

        return unassignedNeighborPos

    # Renvoie la liste de toutes les positions associées à la position donnée (ligne, colonne, sous-grille)
    def getNeighborPos(self, x: int, y: int) -> list[tuple[int, int]]:
        neighborPos = []
        # Ligne et colonne
        for k in range(9):
            if k != x:
                neighborPos.append((k, y))
            if k != y:
                neighborPos.append((x, k))

        # Sous grille
        subGridPos = self.getSubGridPosAt(x, y)
        for i in range(3):
            for j in range(3):
                if [3 * subGridPos[0] + i, 3 * subGridPos[1] + j] not in neighborPos:
                    neighborPos.append((3 * subGridPos[0] + i, 3 * subGridPos[1] + j))

        neighborPos.remove((x, y))

        return neighborPos

    # Renvoie True si toutes les contraintes sont respectées, sinon False
    def checkConstraints(self, value: int, x: int, y: int) -> bool:
        return self.checkColumn(value, x, y) and self.checkRow(value, x, y) and self.checkSubGrid(value, x, y)

    # Renvoie True si la ligne ne contient pas deja value à un autre emplacement, sinon retourne False
    def checkRow(self, value: int, x: int, y: int) -> bool:
        for i in range(len(self.grid)):
            if self.getValue(i, y) == value and i != x:
                return False
        return True

    # Renvoie True si la colonne ne contient pas value à un autre emplacement, sinon retourne False
    def checkColumn(self, value: int, x: int, y: int) -> bool:
        for i in range(len(self.grid[x])):
            if self.getValue(x, i) == value and i != y:
                return False
        return True

    # Renvoie True si la sous grille en 3x3 ne contient pas deja value à un autre emplacement, sinon retourne False
    def checkSubGrid(self, value: int, x: int, y: int) -> bool:
        (m, n) = self.getSubGridPosAt(x, y)
        for i in range(3):
            for j in range(3):
                row, col = 3 * m + i, 3 * n + j
                if self.getValue(row, col) == value and (row != x or col != y):
                    return False
        return True
