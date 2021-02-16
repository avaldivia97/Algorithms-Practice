# Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"

# Example 3:
# Input: s = "a"
# Output: "a"

# Example 4:
# Input: s = "ac"
# Output: "a"

# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters (lower-case and/or upper-case)

# Link to problem:
# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/780/

class Solution:
    def longestPalindrome(self, s):
        answer = ""
        longest = 0
        s_length = len(s)
        for i in range(s_length):
            left = i
            right = i
            while left >= 0 and right < s_length and s[left] == s[right]:
                if (right - left + 1) > longest:
                    answer = s[left:right+1]
                    longest = right - left + 1
                left-=1
                right+=1
            left = i
            right = i+1
            while left >= 0 and right < s_length and s[left] == s[right]:
                if (right - left + 1) > longest:
                    answer = s[left:right+1]
                    longest = right - left + 1
                left-=1
                right+=1
        return answer