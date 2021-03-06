# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Example 4:
# Input: s = ""
# Output: 0

# Constraints:
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.

# Link to problem:
# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/779/

class Solution:
    def lengthOfLongestSubstring(self, s):
        length = len(s)
        if length == 0:
            return 0
        elif length == 1:
            return 1
        else:
            sub = ""
            high = 0
            for char in s:
                index = sub.find(char)
                print(index)
                if index == -1:
                    sub+=char
                else:
                    sub = sub[index+1:]
                    sub+=char
                print(sub)
                new_length = len(sub)
                if new_length > high:
                    high = new_length
            return high