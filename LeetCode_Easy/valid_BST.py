# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Example 1:

# Input: root = [2,1,3]
# Output: true

# Example 2:

# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1

# Link to problem:
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/625/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# You do not need to import math in the leetcode code editor
import math

class Solution:
    def isValidBST(self, root):
        def valid(current_node, low = -math.inf, high = math.inf):
            if current_node is None:
                return True
            if current_node.val <= low or current_node.val >= high:
                return False
            return (valid(current_node.left, low, current_node.val) and valid(current_node.right, current_node.val, high))
        
        return valid(root)