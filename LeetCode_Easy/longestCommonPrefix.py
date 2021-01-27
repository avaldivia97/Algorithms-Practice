# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 0 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.

# Link to problem:
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        prefix = strs[0]
        for i in range(1, len(strs)):
            while True:
                try:
                    x = strs[i].index(prefix)
                    if x == 0:
                        break
                    if x != 0:
                        prefix = prefix[:-1]
                except ValueError:
                    prefix = prefix[:-1]
                    if len(prefix) == 0:
                        return ""
        return prefix