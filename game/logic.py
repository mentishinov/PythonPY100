def get_first_player():
    ...

def init_field(size=3):
    empty_cell = '-'
    field = [
        [empty_cell for _ in range(size)]
        for _ in range(size)
    ]

    return field

def get_cell(field, row_index, col_index)

def is_win(field) -> bool:
    win_condition = ...


def is_available_cell(field) -> bool:
    win_combinations = [
        [(1, 1), (1, 2), (1, 3)],
        [(2, 1), (2, 2), (2, 3)],
        [(3, 1), (3, 2), (3, 3)],

        [(1, 1), (2, 1), (3, 1)],
        [(1, 2), (2, 2), (3, 2)],
        [(1, 3), (2, 3), (3, 3)],

        [(1, 1), (2, 2), (3, 3)],
        [(1, 3), (2, 2), (3, 1)],
    ]

    for win_comb in win_combinations:
        row_index = win_comb[0][0]
        col_index = win_comb[0][1]
        cell_1 = field[row_index][col_index]
        cell_1 = field[win_comb[0][0]][win_comb[0][1]]

        cell_2 = field[win_comb]




    for row in field:
        for cell in row:
            if cell == EMPTY_CELL:
                return True
        return False

def is_empty_cell(field: list, x: int, y: int) -> bool:
    cell = field[x][y]
    # if cell == EMPTY_CELL:
    #     return True
    # else:
    #     return False
    return True if cell == EMPTY_CELL else False