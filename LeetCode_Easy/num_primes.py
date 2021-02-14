# Count the number of prime numbers less than a non-negative number, n.

# Example 1:
# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

# Example 2:
# Input: n = 0
# Output: 0

# Example 3:
# Input: n = 1
# Output: 0 

# Constraints:
# 0 <= n <= 5 * 10^6

# Link to problem:
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/744/

class Solution:
    def countPrimes(self, n):
        def isPrime(n):
            if n==2 or n==3: return True
            if n%2==0 or n<2: return False
            for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
                if n%i==0:
                    return False    

            return True
        total = 0
        for j in range(n):
            if isPrime(j) is True:
                total +=1
        return total