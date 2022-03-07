from typing import Tuple


class Sudoku:

    # Constructeur de sudoku
    def __init__(self, filePath: str = None):
        self.grid = [[0 for x in range(9)] for y in range(9)]
        self.domains = [[[1, 2, 3, 4, 5, 6, 7, 8, 9] for x in range(9)] for y in range(9)]
        if filePath:
            self.loadFile(filePath)

    # Initialise le sudoku grace au fichier dont l'adresse est fournie
    def loadFile(self, filePath: str) -> None:
        file = open(filePath, 'r')
        lines = file.readlines()
        file.close()
        for x in range(0, len(lines)):
            for y in range(0, len(lines[x])):
                if lines[x][y] != "\n":
                    self.assign(int(lines[y][x]), x, y)

    # Transforme le sudoku est string pour l'afficher
    def __str__(self):
        result = ""
        for x in range(len(self.grid)):
            line = ""
            for y in range(len(self.grid[x])):
                line += str(self.grid[y][x])
                if y in [2, 5]:
                    line += "|"
            result += (line + "\n")
            if x in [2, 5]:
                result += ("---+---+---" + "\n")
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

    # Renvoie True si la colonne ne contient pas deja value à un autre emplacement, sinon retourne False
    def checkRow(self, value: int, x: int, y: int) -> bool:
        for i in range(len(self.grid[y])):
            if self.getValue(i, y) == value and i != x:
                return False
        return True

    # Renvoie True si la ligne ne contient pas value à un autre emplacement, sinon retourne False
    def checkColumn(self, value: int, x: int, y: int) -> bool:
        for i in range(len(self.grid)):
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
