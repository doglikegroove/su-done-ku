from itertools import combinations

basic_grid = [['5', '_', '_', '_', '9', '7', '_', '_', '1'],
              ['_', '_', '_', '_', '6', '3', '_', '9', '4'],
              ['_', '_', '_', '_', '1', '2', '_', '_', '_'],
              ['_', '3', '_', '_', '4', '_', '5', '_', '_'],
              ['9', '4', '_', '_', '2', '_', '_', '3', '6'],
              ['_', '_', '6', '_', '5', '_', '_', '8', '_'],
              ['_', '_', '_', '1', '3', '_', '_', '_', '_'],
              ['1', '7', '_', '2', '8', '_', '_', '_', '_'],
              ['3', '_', '_', '9', '7', '_', '_', '_', '5']]


class Cell:
    def __init__(self, init_value):
        if init_value == '_':
            self.possible = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
        else:
            self.possible = set(init_value)


def build_thought_grid(basic_grid):
    thought_grid = []
    for row in range(9):
        thought_grid.append([])
        for col in range(9):
            thought_grid[row].append(Cell(basic_grid[row][col]))
    return thought_grid


def print_grid(printable_grid):
    for row in range(9):
        for col in range(9):
            print(printable_grid[row][col], end='')
        print('\n')


def print_thought_grid(thought_grid):
    for row in range(9):
        for col in range(9):
            num_string = ''
            for num in sorted(thought_grid[row][col].possible):
                num_string += num
            print("%9s" % num_string, end='')
            print('|', end='')
        print('\n')


def eliminate_from_col(num, row, col):
    for scan_row in range(9):
        if scan_row == row:
            pass
        else:
            thought_grid[scan_row][col].possible.discard(num)


def eliminate_from_row(num, row, col):
    for scan_col in range(9):
        if scan_col == col:
            pass
        else:
            thought_grid[row][scan_col].possible.discard(num)


def eliminate_from_box(num, row, col):
    base_row = (row // 3) * 3
    base_col = (col // 3) * 3
    for box_row in 0, 1, 2:
        scan_row = base_row + box_row
        for box_col in 0, 1, 2:
            scan_col = base_col + box_col
            if (scan_row == row) and (scan_col == col):
                pass
            else:
                thought_grid[scan_row][scan_col].possible.discard(num)


def perform_basic_eliminations():
    for row in range(9):
        for col in range(9):
            if len(thought_grid[row][col].possible) == 1:
                fixed_num = sorted(thought_grid[row][col].possible)[0]
                eliminate_from_col(fixed_num, row, col)
                eliminate_from_row(fixed_num, row, col)
                eliminate_from_box(fixed_num, row, col)


def look_for_row_must_haves():
    for row in range(9):
        for num in range(1, 10):
            num = str(num)
            possible_spots = []
            for col in range(9):
                if num in thought_grid[row][col].possible:
                    possible_spots.append(col)
            if len(possible_spots) == 1:
                fixed_col = possible_spots[0]
                thought_grid[row][fixed_col].possible.clear()
                thought_grid[row][fixed_col].possible.add(num)
            if len(possible_spots) == 0:
                print("Grid row %d has no place for %s!\n" % (row, num))
                print_thought_grid(thought_grid)
                exit(1)


def look_for_col_must_haves():
    for col in range(9):
        for num in range(1, 10):
            num = str(num)
            possible_spots = []
            for row in range(9):
                if num in thought_grid[row][col].possible:
                    possible_spots.append(row)
            if len(possible_spots) == 1:
                fixed_row = possible_spots[0]
                thought_grid[fixed_row][col].possible.clear()
                thought_grid[fixed_row][col].possible.add(num)
            if len(possible_spots) == 0:
                print("Grid column %d has no place for %s!\n" % (col, num))
                print_thought_grid(thought_grid)
                exit(1)


def look_for_box_must_haves():
    for base_row in 0, 1, 2:
        for base_col in 0, 1, 2:
            for num in range(1, 10):
                num = str(num)
                possible_spots = []
                for box_row in 0, 1, 2:
                    for box_col in 0, 1, 2:
                        row = (base_row * 3) + box_row
                        col = (base_col * 3) + box_col
                        if num in thought_grid[row][col].possible:
                            possible_spots.append([row, col])
                if len(possible_spots) == 1:
                    coords = possible_spots[0]
                    thought_grid[coords[0]][coords[1]].possible.clear()
                    thought_grid[coords[0]][coords[1]].possible.add(num)
                if len(possible_spots) == 0:
                    print("Grid box %d,%d has no place for %s!\n" % (base_row, base_col, num))
                    print_thought_grid(thought_grid)
                    exit(1)


def look_for_must_haves():
    look_for_row_must_haves()
    look_for_col_must_haves()
    look_for_box_must_haves()


def look_for_row_unions():
    for row in range(9):
        multichoice = []
        for col in range(9):
            if len(thought_grid[row][col].possible) > 1:
                multichoice.append(col)
        combos = []
        for i in range(1, len(multichoice)):
            combos.extend(combinations(multichoice, i + 1))
        for group in combos:
            union_set = set([])
            for col in group:
                union_set = union_set.union(thought_grid[row][col].possible)
            if len(union_set) == len(group):
                for col in range(9):
                    if col in group:
                        pass
                    else:
                        for num in union_set:
                            thought_grid[row][col].possible.discard(num)


def look_for_col_unions():
    for col in range(9):
        multichoice = []
        for row in range(9):
            if len(thought_grid[row][col].possible) > 1:
                multichoice.append(row)
        combos = []
        for i in range(1, len(multichoice)):
            combos.extend(combinations(multichoice, i + 1))
        for group in combos:
            union_set = set([])
            for row in group:
                union_set = union_set.union(thought_grid[row][col].possible)
            if len(union_set) == len(group):
                for row in range(9):
                    if row in group:
                        pass
                    else:
                        for num in union_set:
                            thought_grid[row][col].possible.discard(num)


def look_for_unions():
    look_for_row_unions()
    look_for_col_unions()


def count_possibilities():
    count = 0
    for row in range(9):
        for col in range(9):
            count += len(thought_grid[row][col].possible)
    return count


thought_grid = build_thought_grid(basic_grid)
changed = True
while changed:
    starting_possibilities = count_possibilities()
    perform_basic_eliminations()
    look_for_must_haves()
    look_for_unions()
    if starting_possibilities == count_possibilities():
        changed = False

print_grid(basic_grid)
print('\n\n')
print_thought_grid(thought_grid)
