def checkmate(board):

    rows = board.split("\n")

    
    king_r = -1
    king_c = -1

    for r in range(len(rows)):
        for c in range(len(rows[r])):
            if rows[r][c] == "K":
                king_r = r
                king_c = c

    
    if king_r == -1:
        print("Fail")
        return

    
    for r in range(len(rows)):
        for c in range(len(rows[r])):
            if rows[r][c] == "P":

                
                if r - 1 == king_r and abs(c - king_c) == 1:
                    print("Success")
                    return

    
    if check_bishop(rows, king_r, king_c):
        print("Success")
        return

    
    if check_rook(rows, king_r, king_c):
        print("Success")
        return

    
    if check_queen(rows, king_r, king_c):
        print("Success")
        return

    
    print("Fail")


def check_bishop(board, kr, kc):

    
    directions = [
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1)
    ]

    for dr, dc in directions:

        r = kr + dr
        c = kc + dc

        while 0 <= r < len(board) and 0 <= c < len(board[r]):

            
            if board[r][c] in "PBRQK":

                
                if board[r][c] == "B":
                    return True

                
                break

            r += dr
            c += dc

    return False


def check_rook(board, kr, kc):

    
    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dr, dc in directions:

        r = kr + dr
        c = kc + dc

        while 0 <= r < len(board) and 0 <= c < len(board[r]):

            
            if board[r][c] in "PBRQK":

                
                if board[r][c] == "R":
                    return True

                
                break

            r += dr
            c += dc

    return False


def check_queen(board, kr, kc):

    
    directions = [
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1),
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dr, dc in directions:

        r = kr + dr
        c = kc + dc

        while 0 <= r < len(board) and 0 <= c < len(board[r]):

            
            if board[r][c] in "PBRQK":

            
                if board[r][c] == "Q":
                    return True

                
                break

            r += dr
            c += dc

    return False
