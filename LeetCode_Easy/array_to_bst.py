# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Example:

# Given the sorted array: [-10,-3,0,5,9],

# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

#       0
#      / \
#    -3   9
#    /   /
#  -10  5

#  Link to problem:
#  https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/631/

# We import math so the file doesnt have errors, in the leetcode code editor you do not need to import
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        if len(nums) == 0:
            return None
        def construct_tree(nums, left, right):
            if left > right:
                return None
            middle = math.floor(left + (right - left) / 2)
            current = TreeNode(nums[middle])
            current.left = construct_tree(nums, left, middle - 1)
            current.right = construct_tree(nums, middle + 1, right)
            return current
        return construct_tree(nums, 0, len(nums) - 1)