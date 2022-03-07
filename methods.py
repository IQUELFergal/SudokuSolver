import sudoku as Sudoku


# Renvoie un dictionnaire contenant chaque valeur initiale de la grille associée à sa position
def createStartAssignment(sudoku: Sudoku):
    assignment = {}
    for x in range(len(sudoku.grid)):
        for y in range(len(sudoku.grid[x])):
            value = sudoku.getValue(x, y)
            if value != 0:
                assignment[(x, y)] = value
    return assignment

# Renvoie le sudoku résolu
def backtrackingSearch(sudoku: Sudoku, startAssignment: dict, useAC3: bool, useDegHeur: bool) -> Sudoku:
    finalAssignment = recursiveBacktracking(sudoku, startAssignment, useAC3, useDegHeur)

    for pos in finalAssignment.keys():
        x, y = pos[0], pos[1]
        sudoku.grid[x][y] = finalAssignment.get(pos)

    return sudoku

# Renvoie un dictionnaire contenant chaque valeur de la grille associée à sa position
def recursiveBacktracking(sudoku: Sudoku, assignment: dict, useAC3: bool, useDegHeur: bool) -> dict:
    if len(assignment) == 81:
        return assignment

    positionList = MRV(sudoku)

    # Selection de la position avec degreeHeuristic
    if useDegHeur and len(positionList) > 1:
        position = degreeHeuristic(sudoku, positionList)
    else:
        position = positionList[0]

    domain = leastConstrainingValue(sudoku, position[0], position[1])

    # Pour chaque valeur du domaine
    for value in domain:
        # Si la valeur testée respecte les contraintes du sudoku
        if sudoku.checkConstraints(value, position[0], position[1]):
            # On met à jour le sudoku en lui assignant la valeur testée
            assignment[(position[0], position[1])] = value
            sudoku.assign(value, position[0], position[1])

            # AC3
            if useAC3:
                AC3(sudoku)

            # Recursivité
            result = recursiveBacktracking(sudoku, assignment, useAC3, useDegHeur)

            if result != {}:
                return result

            # Reset des valeurs
            del assignment[(position[0], position[1])]
            sudoku.unassign(domain, position[0], position[1])

    return {}


def MRV(sudoku: Sudoku) -> list:
    domain = 10
    positionList = []
    for x in range(len(sudoku.grid)):
        for y in range(len(sudoku.grid[x])):
            val = sudoku.getValue(x, y)
            if val == 0:
                domainLength = len(sudoku.domains[x][y])
                if domainLength == domain:
                    positionList.append((x, y))
                else:
                    domain = domainLength
                    positionList = [(x, y)]

    return positionList


# Retourne la position avec le plus de contraintes
def degreeHeuristic(sudoku: Sudoku, positions: list) -> tuple:
    maxConstraints = -1
    positionOfMaxConstraints = (-1, -1)
    for position in positions:
        x, y = position[0], position[1]
        constraints = len(sudoku.getUnassignedNeighborPos(x, y))
        if constraints > maxConstraints:
            maxConstraints = constraints
            positionOfMaxConstraints = (x, y)
    return positionOfMaxConstraints


def AC3(sudoku: Sudoku):
    queue = []
    for x in range(len(sudoku.grid)):
        for y in range(len(sudoku.grid[x])):
            val = sudoku.getValue(x, y)
            if val == 0:
                unassignedNeighborPosList = sudoku.getUnassignedNeighborPos(x, y)
                for neighborPos in unassignedNeighborPosList:
                    queue.append([(x, y), neighborPos])
    while len(queue):
        [xi, xj] = queue.pop()
        if removeInconsistentValues(sudoku, xi, xj):
            unassignedNeighborPosList = sudoku.getUnassignedNeighborPos(xi[0], xi[1])
            for xk in unassignedNeighborPosList:
                queue.append([xk, xi])


def removeInconsistentValues(sudoku: Sudoku, xi: tuple, xj: tuple) -> bool:
    remove = False
    xiDomain = sudoku.getDomain(xi[0], xi[1])
    xjDomain = sudoku.getDomain(xj[0], xj[1])

    for value in xiDomain:
        if len(xjDomain) > 0:
            if not any([value != n for n in xjDomain]):
                sudoku.removeFromDomain(value, xi[0], xi[1])
                remove = True

            return remove


def leastConstrainingValue(sudoku: Sudoku, x: int, y: int) -> list:
    neighborPosList = sudoku.getUnassignedNeighborPos(x, y)
    domain = sudoku.getDomain(x, y)
    orderedValues = []
    constraintsCount = {}

    # Association de son nombre de voisins à chaque valeur possible du domaine
    for value in domain:
        count = 0
        for neighborPos in neighborPosList:
            neighborDomain = sudoku.getDomain(neighborPos[0], neighborPos[1])
            if value in neighborDomain:
                count += 1
        constraintsCount[value] = count

    # Transformation du dictionnaire en liste triée de position
    sortedDict = sorted(constraintsCount.items(), key=lambda n: n[1])

    # Création de la liste finale des valeurs à tester
    for i in range(len(sortedDict)):
        orderedValues.append(sortedDict[i][0])
    return orderedValues
