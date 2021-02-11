# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

# Link to problem:
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/601/

class Solution:
    def generate(self, numRows):
        if numRows <= 0:
            return []
        answer = []
        for i in range(numRows):
            row = []
            for j in range(i+1):
                row.append(None)
            row[0], row[-1] = 1, 1
            for k in range(1, i):
                row[k] = answer[i-1][k-1] + answer[i-1][k]
            answer.append(row)
        return answer
