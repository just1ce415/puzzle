"""
Main module
GitHub: https://github.com/just1ce415/puzzle.git
"""

def check_range(board:list) -> bool:
    '''
    Checking if all the numbers on the board are in range from 1 to 9.
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
        for i in range(len(line)):
            if line[i].isdigit():
                if int(line[i]) not in range(1, 10):
                    return False
    return True


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
        raw_line = line.replace('*', '')
        raw_line = raw_line.replace(' ', '')
        set_line = set(raw_line)
        if len(set_line) != len(raw_line):
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
    >>> check_colors(["**** ****",\
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
    # START INDICES OF ROW AND COLOMN TO INSPECT
    start_row = 4
    start_col = 0
    for k in range(5):
        # STRING TO CHECK FOR REPETITIONS
        str_tocheck = []
        # ADD DIGITS FROM COLOMNS
        for i in range(start_row, start_row+5):
            str_tocheck.append(board[i][start_col])
        # ADD DIGITS FROM ROWS
        for i in range(start_col, start_col+5):
            str_tocheck.append(board[start_row+4][i])
        # CHECKING VIA SETS
        str_tocheck = ''.join(str_tocheck)
        str_tocheck = str_tocheck.replace(' ', '')
        if len(str_tocheck) != len(set(str_tocheck)):
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
    >>> validate_board(["****1****",\
 "*** 2****",\
 "**  3****",\
 "*   4****",\
 "    56781",\
 "        *",\
 "2      **",\
 "      ***",\
 "3 4  ****"])
    False
    '''
    if check_colomns(board) and check_rows(board) and check_colors(board) and check_range(board):
        return True
    return False


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
