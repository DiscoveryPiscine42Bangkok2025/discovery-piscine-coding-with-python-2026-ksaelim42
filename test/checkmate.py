def get_king_pos(rows):

    for r, row in enumerate(rows):
        c = row.find('K')
        if c != -1:
            return r, c
    return -1, -1

def checkmate(board):
    if not board:
        print("ฺBoard is Empty")
        return
    rows = board.strip().splitlines()

    kr, kc = get_king_pos(rows)

    print(kc, kr)
    if kr == -1:
        print("Fail")
        return


    
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)
    ]

    for dr, dc in directions:
        dist = 1
        
        while True:
            
            nr, nc = kr + (dr * dist), kc + (dc * dist)

      
            if not (0 <= nr < len(rows) and 0 <= nc < len(rows[0])):
                break

            piece = rows[nr][nc]

            if piece == '.':
                dist += 1
                continue

            if piece == 'R' and (dr == 0 or dc == 0):
                print("Success")
                return

            if piece == 'B' and (dr != 0 and dc != 0):
                print("Success")
                return

            if piece == 'Q':
                print("Success")
                return
            
            if piece == 'P' and dist == 1 and dr == 1 and (dc == -1 or dc == 1):
                print("Success")
                return

            break 

    print("Fail")

