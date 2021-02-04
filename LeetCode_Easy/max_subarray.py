# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Example 2:
# Input: nums = [1]
# Output: 1

# Example 3:
# Input: nums = [0]
# Output: 0

# Example 4:
# Input: nums = [-1]
# Output: -1

# Example 5:
# Input: nums = [-100000]
# Output: -100000

# Constraints:
# 1 <= nums.length <= 3 * 10^4
# -10^5 <= nums[i] <= 10^

# Link to problem:
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/566/

class Solution:
    def maxSubArray(self, nums):
        curr_sum, max_sum = 0, -10**6
        for num in nums:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)
        return max_sum