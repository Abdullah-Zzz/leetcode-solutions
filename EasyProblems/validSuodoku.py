#we create array of sets for row,col and each 3*3 box. we go through every box checking its number and checking whether it exists in the row col and the 3*3 box 
#if it doesnot exist in the row, col and 3*3 box we simply add the number into its row,col and box array and move on.


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                box_index=(i//3)*3+(j//3)
                if num == ".":
                    continue
                else:
                    if num in row[i] or num in col[j] or num in box[box_index]:
                        return False
                    else:
                        row[i].add(num)
                        col[j].add(num)
                        box[box_index].add(num)
        return True