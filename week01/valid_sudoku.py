def is_valid_sudoku(board):
    seen = set()
    
    for i in range(9):
        for j in range(9):
            val = board[i][j]
            if val != '.':
                row_key = f"{val} in row {i}"
                col_key = f"{val} in col {j}"
                box_key = f"{val} in box {i // 3}-{j // 3}"
                
                if row_key in seen or col_key in seen or box_key in seen:
                    return False
                    
                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)
                
    return True

valid_board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

invalid_board = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

empty_board = [["." for _ in range(9)] for _ in range(9)]
assert is_valid_sudoku(valid_board) == True
assert is_valid_sudoku(invalid_board) == False
assert is_valid_sudoku(empty_board) == True

# Time and space complexity are both O(1) because of the size of the board is 9x9
# I first tried to traverse through all rows, columns, and the 9 3x3 boxes separately. Then, I realized it was more efficient to just combine them in one double for loop that only iterates through the 81 boxes.