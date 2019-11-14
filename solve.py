import os
import json
import numpy as np
from bisect import bisect_left
from dlmatrix import DancingLinksMatrix
from alg_x import AlgorithmX
from data import SHAPE_SLOT, SHAPE_CHIP, SHAPE_M2


def rotated_shapes(shape: np.ndarray) -> list:
    # Rotate the shape by 90 degree for 3 times, and leave unique shapes
    all_shapes = [shape]
    for _ in range(3):
        prev = all_shapes[-1]
        # Rotate 90 degree
        curr = np.rot90(prev, 1, (1, 0))
        all_shapes.append(curr)
    # Remove equal shapes after rotation
    # 4 shapes are equal
    if np.array_equal(all_shapes[0], all_shapes[1]):
        return [shape]
    # 2 shapes are equal
    if np.array_equal(all_shapes[0], all_shapes[2]):
        return [shape, all_shapes[1]]
    # No shapes are equal
    return all_shapes


def gen_rows(slot: np.ndarray, shape: np.ndarray) -> list:
    r1, c1 = shape.shape
    r2, c2 = slot.shape
    rows = []
    # Iterates on all sub slots
    for r in range(0, r2 - r1 + 1):
        for c in range(0, c2 - c1 + 1):
            sub_slot = slot[r:r + r1, c:c + c1]
            # Could be inserted
            if (sub_slot[shape > 0] > 0).all():
                filled = slot.copy()
                filled[r:r + r1, c: c + c1] -= shape
                rows.append(filled.reshape(-1))
    return rows


def gen_mat(slot: np.ndarray, shapes: list) -> tuple:
    matrix = []
    row_index = []
    # Use -1 to represent invalid cells
    slot[slot == 0] = -1
    # Iterates on all shapes to generate filled rows
    for shape in shapes:
        for rotated in rotated_shapes(np.array(shape)):
            matrix.extend(gen_rows(slot, rotated))
        row_index.append(len(matrix) + 1)
    return np.array(matrix), row_index


# Simple Depth-first-search: would cost too much time and not feasible
# def dfs(matrix: np.ndarray, mask_rows: np.ndarray, mask_cols: np.ndarray,
#         curr_select: list, all_solutions: list, index: int):
#     # Check if empty columns
#     if (mask_cols == 1).all():
#         # Check if selected rows is a solution
#         test_row = np.full(matrix.shape[1], 1)
#         for row_idx in curr_select:
#             # Collect all 0 columns
#             test_row[matrix[row_idx] == -1] = -1
#             test_row[matrix[row_idx] == 0] = 0
#         # All columns are covered
#         if (test_row == 0).all():
#             all_solutions.append(curr_select)
#     else:
#         for curr_idx in range(index, len(matrix)):
#             # Select available row
#             if not mask_rows[curr_idx]:
#                 # Store masked rows and cols to recover
#                 curr_mask_rows = np.full_like(mask_rows, False)
#                 curr_mask_cols = np.full_like(mask_cols, False)
#                 # Choose row and mask out current row
#                 curr_row = matrix[curr_idx]
#                 mask_rows[curr_idx] = True
#                 curr_mask_rows[curr_idx] = True
#                 curr_select.append(curr_idx)
#                 # Mask out conflict rows
#                 for row_idx in np.where(mask_rows[curr_idx:] == 0)[0]:
#                     row = matrix[row_idx]
#                     # Check whether conflicts
#                     if (row[curr_row == 0] == 0).any():
#                         mask_rows[row_idx] = True
#                         curr_mask_rows[row_idx] = True
#                 # Mask out conflict columns
#                 for col_idx in np.where(curr_row == 0):
#                     mask_cols[col_idx] = True
#                     curr_mask_cols[col_idx] = True
#                 dfs(matrix, mask_rows, mask_cols, curr_select, all_solutions,
#                     curr_idx + 1)
#                 # Unmask conflicted rows and columns, and undo row selection
#                 curr_select.pop()
#                 mask_rows[curr_idx] = False
#                 mask_rows[curr_mask_rows == 1] = False
#                 mask_cols[curr_mask_cols == 1] = False


def find_solution(directory: str, limit: int):
    def collect(row_dict: dict) -> bool:
        # Parse row dict and record all chips used
        count = {}
        for idx in row_dict.keys():
            n = chip_names[bisect_left(row_index, idx)]
            if n not in count:
                count[n] = 0
            count[n] += 1
        # Append solution
        solution_list.append({
            'count': count,
            'fill': list(row_dict.values())
        })
        return len(solution_list) >= limit

    # Aggregate all shapes & unique name for shapes
    chip_names = list(SHAPE_CHIP.keys())
    chip_shapes = list(SHAPE_CHIP.values())
    # For all slots, try to find an exact cover
    for name, slot in SHAPE_SLOT.items():
        print('Generating matrix for {}...'.format(name))
        slot = np.array(slot)
        if name == 'm2':
            m2_chips = list(SHAPE_M2.values())
            m2_chips.extend(chip_shapes)
            matrix, row_index = gen_mat(slot, chip_shapes)
        else:
            matrix, row_index = gen_mat(slot, chip_shapes)

        # I used 0 to represent occupied and 1 to represent empty, so...
        matrix = 1 - matrix

        print('Calculating exact cover for {}...'.format(name))

        # DFS version(deprecated): not feasible
        # row, col = matrix.shape
        # all_solutions = []
        # row_mask, col_mask = np.full(row, False), np.full(col, False)
        # dfs(matrix, row_mask, col_mask, [], all_solutions, 0)

        # Dancing Links X version
        solution_list = []
        # Remove those unfillable cells
        fillable_cols = np.where(slot.reshape(-1) == 1)[0]
        matrix = matrix[:, fillable_cols]
        # Solving...
        d = DancingLinksMatrix([int(val) for val in fillable_cols])
        for row in matrix:
            d.add_dense_row(row)
        d.end_add()
        AlgorithmX(d, callback=collect)()
        with open(os.path.join(directory, '{}.json'.format(name)), 'w') as f:
            json.dump(solution_list, f, indent=2, separators=(',', ':'))
        print('Successfully saved solution data for {}.'.format(name))
