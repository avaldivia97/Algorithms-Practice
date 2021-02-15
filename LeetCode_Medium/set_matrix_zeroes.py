# Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

# Follow up:
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?
 
# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Example 2:
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

# Constraints:
# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -2^31 <= matrix[i][j] <= 2^31 - 1

# Link to problem:
# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/777/

class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        record = []
        x_length = len(matrix[0])
        y_length = len(matrix)
        for i in range(y_length):
            for j in range(x_length):
                if matrix[i][j] == 0:
                    record.append([i, j])
        for pair in record:
            for array in matrix:
                array[pair[1]] = 0
            for x in range(x_length):
                matrix[pair[0]][x] = 0