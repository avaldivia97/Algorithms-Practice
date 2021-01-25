# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:

# Input: "race a car"
# Output: false
 

# Constraints:

# s consists only of printable ASCII characters.

# Link to problem:
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/

class Solution(object):
    def isPalindrome(self, s):
        clean = ''
        for i in s:
            if i.isalnum():
                clean +=i
        clean = clean.lower()
        return clean == clean[::-1]