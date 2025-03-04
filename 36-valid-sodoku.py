def isValidSudoku(board):
    rows = [None] * 9 # initialize a set for every row
    cols = [None] * 9 # initialize a set for every colum
    boxes = [None] * 9 # initialize a set for every 3x3 box
    for i in range(9):
        rows[i] = set()
        cols[i] = set()
        boxes[i] = set() 
    
    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num == '.':
                continue
          
            # check rows
            if num in rows[r]:
                print('row', r, rows[r])
                return False
                
            # check cols
            if num in cols[c]:
                print('col', c, cols[c])
                return False
            
            # check boxes
            idx = (r // 3 ) * 3 + (c // 3)
            if num in boxes[idx]:
                print('box', idx, boxes[idx])
                return False
            
            rows[r].add(num)
            cols[c].add(num)
            boxes[idx].add(num)
    return True
                
            

board = [
 ["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","5","2",".",".",".",".","6","."]
,["0",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".","9",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))