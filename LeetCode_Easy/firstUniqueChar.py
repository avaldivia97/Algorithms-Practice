# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode"
# return 2.
 

# Note: You may assume the string contains only lowercase English letters.

# Link to problem:
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/

class Solution(object):
    def firstUniqChar(self, s):
        counts = collections.Counter(s)
        for index, chars in enumerate(s):
            if counts[chars] == 1:
                return index
        return -1