"""
Main module
GitHub: https://github.com/just1ce415/puzzle.git
"""

def check_rows(board: list) -> bool:
    '''
    Checking if there's no repititons in rows. Returns True - no repetitions.
    >>> check_rows(["**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  **",\
 "  8  2***",\
 "  2  ****"])
    True
    '''
    for line in board:
        for i in range(1, 9):
            counter = 0
            # ALL THE POSSIBLE DIGITS: RANGE 1-9
            for j in range(len(line)):
                # USING COUNTER TO TRACK REPETITONS
                if line[j].isdigit():
                    if int(line[j]) == i:
                        counter += 1
                if counter > 1:
                    return False
    return True


def check_colomns(board: list) -> bool:
    '''
    Checking if there's no repititons in colomns. Returns True - no repetitions.
    >>> check_colomns(["**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  **",\
 "  8  2***",\
 "  2  ****"])
    False
    '''
    # THE SAME AS PREVIOUS FUNC, HOWEVER, IT GOES THROUGH COLOMNS
    for k in range(len(board)):
        for i in range(1, 9):
            counter = 0
            for j in range(len(board)):
                if board[j][k].isdigit():
                    if int(board[j][k]) == i:
                        counter += 1
                if counter > 1:
                    return False
    return True


def check_colors(board: list) -> bool:
    '''
    Checking if there's no repititons in blocks of colors. Returns True - no repetitions.
    However, it the result of this function may intersect with a result of others. This
    functions just guaranties that all the rules regarding color blockes are sticked to.
    >>> check_colors(["**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  **",\
 "  8  2***",\
 "  2  ****"])
    False
    '''
    # CHECKING SUB-BOARDS 5X5 WITH COLOR BLOCK INVOLVED
    start_row = 4
    start_col = 0
    # ACTUALLY, THERE 5 SQUARES 5X5
    for _ in range(5):
        # FORMAING NESTED SUB-BOARD
        nest_board = board[start_row:start_row+5]
        for i in range(len(nest_board)):
            nest_board[i] = str(nest_board[start_col: start_col+5])
        # WE SHOULD CHECK BOTH COLOMNS AND ROWS TO COVER THE COLOR BLOCK
        if not check_rows(nest_board) or not check_colomns(nest_board):
            return False
        start_row -= 1
        start_col += 1
    return True


def validate_board(board: list) -> bool:
    '''
    Returns True if the board is suitable for starting the game.
    Otherwise False.

    >>> validate_board(["**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  **",\
 "  8  2***",\
 "  2  ****"])
    False
    '''
    if check_colomns(board) and check_rows(board) and check_colors(board):
        return True
    return False


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
