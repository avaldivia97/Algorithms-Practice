# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, calculate the Hamming distance.

# Note:
# 0 ≤ x, y < 2 ^ 31.

# Example:
# Input: x = 1, y = 4

# Output: 2

# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
# ↑   ↑

# The above arrows point to positions where the corresponding bits are different.

# Link to problem:
# https: // leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/762/

class Solution:
    def hammingDistance(self, x, y):
        bin_x = '{:032b}'.format(x)
        bin_y = '{:032b}'.format(y)
        count = 0
        for i in range(32):
            if bin_x[i] != bin_y[i]:
                count += 1
        return count
