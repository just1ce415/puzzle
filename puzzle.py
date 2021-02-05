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
    pass


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
    pass


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
    pass


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
    pass


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
