# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
# Example 4:

# Input: x = 0
# Output: 0
 

# Constraints:

# -231 <= x <= 231 - 1

# Link to problem:
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/

class Solution(object):
    def reverse(self, x):
        if x >= 2**31 - 1 or x <= -2**31:
            return 0
        else:
            stringify = str(x)
            if x >= 0:
                rev = stringify[::-1]
            else:
                temp = stringify[1:]
                temp2 = temp[::-1]
                rev = "-" + temp2
        if int(rev) >= 2**31 - 1 or int(rev) <= -2**31:
            return 0
        else:
            return int(rev)
        """
        :type x: int
        :rtype: int
        """
   