"""
Problem: Maximun Subarray
Difficulty: Medium

Approach:
- Used Kadane's Algorithm 

Time Complexity: O(n)
Space Complexity: O(1)

LeetCode:
https://leetcode.com/problems/maximum-subarray/
"""
class Solution:
    def maxSubArray(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum
