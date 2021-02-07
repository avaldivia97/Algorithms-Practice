# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3x.

# Example 1:
# Input: n = 27
# Output: true

# Example 2:
# Input: n = 0
# Output: false

# Example 3:
# Input: n = 9
# Output: true

# Example 4:
# Input: n = 45
# Output: false

# Constraints:
# -2 ^ 31 <= n <= 2 ^ 31 - 1

# Link to problem:
# https: // leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/745/

class Solution:
    def isPowerOfThree(self, n):
        if n < 1:
            return False
        while n % 3 == 0:
            n = n / 3
        if n == 1:
            return True
        else:
            return False
