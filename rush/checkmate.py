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
    rows_list = board.strip().splitlines()

    k_r, k_c = get_king_pos(rows)

    print(k_c, k_r)
    if k_r == -1:
        print("Fail")
        return


    
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)
    ]

    for dr, dc in directions:
        dist = 1
        
        while True:
            
            nr, nc = king_r + (dr * dist), king_c + (dc * dist)

      
            if not (0 <= nr < len(rows) and 0 <= nc < len(rows[0])):
                break

            piece = rows[nr][nc]

            if piece == '.':
                dist += 1
                continue

            # C. ถ้าเจอ "ตัวหมาก" (ไม่ว่าจะมิตรหรือศัตรู) เลเซอร์จะหยุดตรงนี้!
            # เราต้องมาเช็คว่า ตัวที่เจอเนี่ย มันกินเราได้ไหม?
            
            # --- เช็คศัตรู ---
            
            # 1. ถ้าเจอ Rook (R)
            # R กินได้เฉพาะแนวตรง (dr หรือ dc ต้องเป็น 0)
            if piece == 'R' and (dr == 0 or dc == 0):
                print("Success")
                return

            # 2. ถ้าเจอ Bishop (B)
            # B กินได้เฉพาะแนวทแยง (dr และ dc ต้องไม่เป็น 0)
            if piece == 'B' and (dr != 0 and dc != 0):
                print("Success")
                return

            # 3. ถ้าเจอ Queen (Q)
            # Q กินได้ทุกทิศ (น่ากลัวสุด)
            if piece == 'Q':
                print("Success")
                return

            # 4. ถ้าเจอ Pawn (P) **จุดปราบเซียน**
            # P กินได้เฉพาะ "แนวทแยง" และต้องอยู่ห่างแค่ "1 ช่อง" (dist == 1)
            # และ P ต้องอยู่ "ข้างล่าง" King (เพราะ P กินขึ้นบน) -> แปลว่า King มองลงมาเจอ (dr เป็น +1)
            if piece == 'P' and dist == 1 and dr == 1 and (dc == -1 or dc == 1):
                print("Success")
                return

            # ถ้าเจอตัวอื่น (เช่นตัวบล็อก) หรือเงื่อนไขข้างบนไม่จริง ให้หยุดเช็คทิศนี้
            break 

    # ถ้าวนครบ 8 ทิศแล้วไม่ตาย
    print("Fail")

