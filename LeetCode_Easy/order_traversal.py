# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# Link to problem:
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/628/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root):
        order_traversal = []
        if root is None:
            return order_traversal
        queue = []
        queue.append(root)
        while (len(queue) != 0):
            current_level = []
            size = len(queue)
            for i in range(size):
                current_node = queue.pop(0)
                current_level.append(current_node.val)
                print(current_level)
                if current_node.left is not None:
                    queue.append(current_node.left)
                if current_node.right is not None:
                    queue.append(current_node.right)
            order_traversal.append(current_level)
        return order_traversal