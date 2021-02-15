# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
 

# Constraints:
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lower-case English letters.

# Link to problem:
# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/778/

import collections # import collections so VS Code does not give an error. This is not needed in the leetcode editor

class Solution:
    def groupAnagrams(self, strs):
        size = len(strs)
        if size == 0:
            return [[""]]
        elif size == 1:
            return [[strs[0]]]
        else:
            dictionary = collections.defaultdict(list)
            for string in strs:
                dictionary[tuple(sorted(string))].append(string)
            return dictionary.values()