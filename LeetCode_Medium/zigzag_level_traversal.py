# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

# Link to problem:
# https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/787/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root):
        if root is None:
            return None
        res = []
        queue = []
        curr = root
        queue.append(curr)
        left_to_right = True
        while len(queue) > 0:
            current_level = []
            length = len(queue)
            for i in range(length):
                curr = queue.pop(0)
                if left_to_right:
                    current_level.append(curr.val)
                else:
                    current_level.insert(0, curr.val)
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
            left_to_right = not left_to_right
            res.append(current_level)
        print(res)
        return res