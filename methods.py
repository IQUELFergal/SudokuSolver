import sudoku as s

def initAssignment(sudoku: s):
    assignment = {} # Dictionnaire contenant chaque valeur de la grille associée a sa position
    for x in range(len(sudoku.grid)):
        for y in range(len(sudoku.grid[x])):
            if sudoku.grid[x][y] != 0:
                assignment[(x, y)] = sudoku.grid[x][y]
    return assignment

def backtrackingSearch(sudoku: s, initial_assignment: dict, use_ac3: bool, deg_h: bool) -> s:
    assignment_final = recursive_backtracking(sudoku, initial_assignment, use_ac3, deg_h)

    for pos in assignment_final.keys():
        x = pos[0]
        y = pos[1]
        sudoku.grid[x][y] = assignment_final.get(pos)

    return sudoku

def recursive_backtracking(sudoku: s, assignment: dict, useAC3: bool, degH: bool) -> dict:
    if len(assignment) == 81:
        print("Sudoku solved !\n")
        return assignment

    # Choisit la variable avec le plus petit nombre de valeurs légales
    positions = MRV(sudoku)

    if degH:
        if len(positions) > 1:
            # si plusieurs variables sont choisies via le MRV on les départage avec degree heuristic
            position = degreeHeuristic(sudoku, positions)
        else:
            position = positions[0]
    else:
        position = positions[0]

    value = sudoku.get(position[0], position[1])

    domain = leastConstrainingValue(sudoku, value)

    for value in domain:
        if sudoku.all_constraint(position, value):
            # les contraintes sont respectées
            # on met à jour assignement
            assignment[(position[0], position[1])] = value
            #assign(sudoku, position, value)

            # AC3
            if useAC3:
                AC3(sudoku)

            # on applique la récursivité
            result = recursive_backtracking(sudoku, assignment, useAC3, degH)
            if result != {}:
                return result

            # on remet tout comme avant
            del assignment[(position[0], position[1])]
            #unassign(sudoku, position, domain)

    return {}

def MRV(sudoku: s) -> list:
    domain = 10
    position = []
    for x in range(len(sudoku.grid)):
        for y in range(len(sudoku.grid[x])):
            val = sudoku.get(x, y)
            if val == 0:
                domainLength = len(s.grid.domains[x][y])
                if domainLength == domain:
                    position.append((x,y))
                else:
                    domain = domainLength
                    position = [val.position]


def AC3(sudoku: s) -> None:
    print("AC3")

def degreeHeuristic(sudoku: s, positions: list) -> list:
    print("degH")

def leastConstrainingValue(sudoku: s) -> list:
    print("leastConstrainingValue")