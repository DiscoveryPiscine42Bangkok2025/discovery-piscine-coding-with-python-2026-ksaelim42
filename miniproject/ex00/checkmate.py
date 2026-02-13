def check_char(board):
    allowed_chars = "KQBRP."

    for r in range(len(board)):
        for c in range(len(board[r])):
            char = board[r][c]
            if char not in allowed_chars:
                print(f"Error! Invalid character {char}")
                return False
    return True


def condition_game(board_str):

    board = [line.strip() for line in board_str.strip().splitlines()]

    if not board:
        print("Error! Board is empty ....")
        print("Please enter a value")
        return
        

    if not check_char(board):
        return
    
    size = len(board)
    for row in board:
        if len(row) != size:
            print("Error! Not a square board")
            return

    rows = len(board)
    cols = len(board[0])

    position_K = []
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "K":
                position_K.append((r, c))

    if len(position_K) == 0:
        print("Not have king !!")
        return
    if len(position_K) > 1:
        print("Error! Multiple kings found")
        return

    kx, ky = position_K[0]

    def check_direction(dx, dy, enemy):
        x = kx + dx
        y = ky + dy 

        while 0 <= x < rows and 0 <= y < cols:
            piece = board[x][y]
            if piece != ".":
                if piece in enemy:
                    return True
                else:
                    return False
            x += dx
            y += dy
        return False

    straight = [(-1,0),(1,0),(0,-1),(0,1)]
    for dx, dy in straight:
        if check_direction(dx, dy, ["R","Q"]):
            print("Success")
            return

    diagonal = [(-1,-1),(-1,1),(1,-1),(1,1)]
    for dx, dy in diagonal:
        if check_direction(dx, dy, ["B","Q"]):
            print("Success")
            return
        
    pawn = [(-1,1),(1,1)]
    for dx, dy in pawn:
        sx, sy = kx + dx, ky + dy
        if 0 <= sx < rows and 0 <= sy < cols:
            if board[sx][sy] == "P":
                print("Success")
                return

    print("Fail")