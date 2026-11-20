class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check all rows
        for row in board:
            hashmap = {}
            for item in row:
                if item == '.': continue
                if item in hashmap:
                    return False
                hashmap[item] = True
        
        # check all columns
        for i in range(9):
            hashmap = {}
            for j in range(9):
                if board[j][i] == '.':
                    continue
                if board[j][i] in hashmap:
                    return False
                hashmap[board[j][i]] = True

        # check all 3x3s
        hashmaps = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        for row in range(9):
            for col in range(9):
                item = board[row][col]
                if item == '.':
                    continue
                hashnum = (row // 3) * 3 + (col // 3)
                # print(f"{row=}, {col=}, {hashnum=}")
                if item in hashmaps[hashnum]:
                    # print('hey!')
                    return False
                hashmaps[hashnum][item] = True
                # print(hashmaps)

        return True