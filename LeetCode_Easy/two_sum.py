# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 103
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

# Link to problem:
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/

class Solution:
    def twoSum(self, nums, target):
        possible_answers = dict()
        for i in range(len(nums)):
            x = target - nums[i]
            if x in possible_answers:
                return [possible_answers[x], i]
            possible_answers[nums[i]] = i