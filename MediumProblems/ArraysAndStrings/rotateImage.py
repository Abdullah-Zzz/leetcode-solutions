#Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]:Output: [[7,4,1],[8,5,2],[9,6,3]],( this method is quite weired.). to rotate the image we change the first row to 
#the first elements of each row starting from the last element. for example input : [[1,2,3],[4,5,6],[7,8,9]] output: [[7,4,1],[8,5,2],[9,6,3]] the first row 
#is changed into [7,4,1] which are the first elements of each row starting from the last one. for the other row we do the same. for second row we change
# it to the second element of each row starting from the last element and same for the last row.

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        out = []
        for i in range(len(matrix)):
            value = []
            for j in range(len(matrix[0])-1,-1,-1):
                value.append(matrix[j][i])
            out.append(value)
            
        for i in range(len(out)):
            matrix[i] = out[i]