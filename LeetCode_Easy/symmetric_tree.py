# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
 

# But the following [1,2,2,null,3,null,3] is not:

#     1
#    / \
#   2   2
#    \   \
#    3    3

# Link to problem:
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/627/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root):
        def isMirror(left, right):
            if(left is None and right is None):
                return True
            if(left is None or right is None):
                return False
            return left.val == right.val and isMirror(left.right, right.left) and isMirror(left.left, right.right)
        if root is None:
            return True
        return isMirror(root.left, root.right)