# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([)]"
# Output: false

# Example 5:
# Input: s = "{[]}"
# Output: true

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

# Link to problem:
# https: // leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/721/


class Solution:
    def isValid(self, s):
        if len(s) % 2 != 0:
            return False
        stack = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            elif s[i] == ")":
                if len(stack) != 0 and stack[-1] == "(":
                    stack.pop(-1)
                else:
                    return False
            elif s[i] == "]":
                if len(stack) != 0 and stack[-1] == "[":
                    stack.pop(-1)
                else:
                    return False
            elif s[i] == "}":
                if len(stack) != 0 and stack[-1] == "{":
                    stack.pop(-1)
                else:
                    return False
        if len(stack) != 0:
            return False
        return True
